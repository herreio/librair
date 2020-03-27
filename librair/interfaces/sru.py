#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..schemas import xml
from ..protocols import sru

from tqdm import tqdm


class Client:
    """
    sru client for database given by url
    """

    def __init__(self, URL, token=None):
        self.URL = URL
        self.explain = None
        self.schemas = []
        self.version = ""
        self.token = token
        self._explain()

    def _explain(self):
        """
        load infos about SRU interface from its explain response
        """
        self.explain = Explain(self.URL, load=True)
        self.version = self.explain.version
        self.database = self.explain.meta
        self.indexes = self.explain.indexes
        self.schemas = list(self.explain.schemas.keys())

    def secret(self, token):
        """
        set access token for sru endpoint
        """
        self.token = token

    def address(self, query, schema, records=10, operation="searchRetrieve"):
        """
        generate request url for given query and schema
        """
        return sru.address(self.URL, query, schema=schema, records=records,
                           version=self.version, operation=operation)

    def search(self, query, schema, records=1):
        """
        search items matching given query, request given schema and
        return number of items given by records
        """
        url = self.address(query, schema, records=records,
                           operation="searchRetrieve")
        if self.token is not None:
            url += "&accessToken=" + self.token
        response = Response(sru.retrieve(url))
        return response.items()

    def total(self, query, schema):
        """
        determine total number of results for given query
        """
        url = self.address(query, schema, records=1,
                           operation="searchRetrieve")
        if self.token is not None:
            url += "&accessToken=" + self.token
        response = Response(sru.retrieve(url))
        return response.total()

    def scroll(self, query, schema, size=100):
        """
        scroll items matching given query, request given schema and
        in steps given by size, return all collected records
        """
        result = []
        total = self.total(query, schema)
        for i in tqdm(range(1, total+1, size)):
            url = sru.address(self.URL, query=query, schema=schema,
                              records=size, version=self.version,
                              operation="searchRetrieve") \
                              + "&startRecord=" + str(i)
            if self.token is not None:
                url += "&accessToken=" + self.token
            response = Response(sru.retrieve(url))
            items = response.items()
            if items is not None:
                result += items
            else:
                return result
        return result


class Response(xml.Element):
    """
    wrapper for xml response from sru interface
    """

    def __init__(self, element, ns=None):
        super().__init__(element, ns=ns)

    def total(self):
        numrec = self.find("numberOfRecords")
        if numrec is not None:
            return int(numrec.text)
        else:
            return self.diagnostics()

    def items(self):
        """
        get record data from response
        """
        data = self.findall("recordData")
        if data != []:
            items = [d[0] for d in data]
            return items if len(items) > 1 else items[0]
        else:
            return self.diagnostics()

    def diagnostics(self):
        diag = self.find("diagnostics")
        if diag is not None:
            diag_ns = diag[0].nsmap["diag"]
            diag = xml.Element(diag, ns=diag_ns)
            print("DIAGNOSTICS")
            uri = diag.find("uri")
            if uri is not None:
                print("URI:", uri.text)
            message = diag.find("message")
            if message is not None:
                print("Message:", message.text)
            details = diag.find("details")
            if details is not None:
                print("Details:", details.text)
        return None


class Explain:
    """
    fetch and process explain response from given URL

    request is sent if load=True otherwise via self.load()
    """

    def __init__(self, URL, load=False):
        self.URL = URL
        self.ns = "http://explain.z3950.org/dtd/2.0/"
        self.raw = None
        self.root = None
        self.meta = {}
        self.sets = []
        self.indexes = {}
        self.schemas = {}
        self.version = ""
        self.read = False
        if load:
            self.load()
            self.read = True

    def __repr__(self):
        if self.read and self.root is not None:
            return str(self.root)
        elif not self.read:
            self.load()
            if self.root is not None:
                return str(self.root)
        return ""

    def store(self, db, path=""):
        """
        write explain xml to file at path
        """
        file = xml.filepath("sru", db, "", "")
        xml.writer(self.root.raw, file, path=path)

    def load(self):
        """
        general routine to load data
        """
        self.load_raw()
        self.load_root()
        self.load_version()
        if self.root:
            self.load_database()
            self.load_schemas()
            self.load_indexes()

    def load_raw(self):
        """
        load sru explain response
        """
        response = sru.retrieve(self.URL)
        self.raw = Response(response)

    def load_root(self):
        """
        load explain element from response
        """
        root = self.raw.items()
        if root is not None:
            self.root = xml.Element(root, ns=self.ns)

    def load_version(self):
        """
        load version of interface given in sru explain response
        """
        version = self.raw.find("version")
        if version is not None:
            self.version = version.text
        else:
            print("could not determine SRU version!")

    def load_database(self):
        """
        load info about schemas given in sru explain response
        """
        meta = {}
        db_info = self.root.find("databaseInfo")
        if db_info is not None:
            db_info = xml.Element(db_info, ns=self.ns)
            title = db_info.find("title")
            if title is not None:
                meta["title"] = title.text
            author = db_info.find("author")
            if author is not None:
                meta["author"] = author.text
            extent = db_info.find("extent")
            if extent is not None:
                meta["extent"] = extent.text
        self.meta = meta

    def load_schemas(self):
        """
        load info about schemas given in sru explain response
        """
        schemas = {}
        schema_info = self.root.find("schemaInfo")
        if schema_info is not None:
            schema_info = xml.Element(schema_info, ns=self.ns)
            s = schema_info.findall("schema")
            for schema in s:
                name = schema.attrib["name"]
                title = schema.find(self.root.xpath("title"))
                if title is not None:
                    schemas[name] = title.text
                else:
                    schemas[name] = ""
        self.schemas = schemas

    def load_config(self):
        """
        config_info = self.root.find("configInfo", relative=False)
        """
        pass

    def load_server(self):
        """
        server_info = self.root.find("serverInfo")
        """
        pass

    def load_indexes(self):
        """
        load info about indexes given in sru explain response
        """
        sets = []
        indexes = {}
        index_info = self.root.find("indexInfo")
        if index_info is not None:
            index_info = xml.Element(index_info, ns=self.ns)
            index_sets = index_info.findall("set")
            for i in index_sets:
                sets.append(i.attrib['name'])
            index_name = self.root.xpath("name")
            index_title = self.root.xpath("title")
            index_elements = index_info.findall("index")
            for i in index_elements:
                title = i.find(index_title)
                name = i.find(index_name)
                s = name.attrib["set"]
                n = name.text
                if s + "." not in n:
                    n = s + "." + n
                indexes[n] = title.text
        self.sets = sets
        self.indexes = indexes
