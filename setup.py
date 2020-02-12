import os
import setuptools

ROOT = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(ROOT, 'README.rst')).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="librair",
    version="2020.02.12",
    author="Donatus Herre",
    author_email="pypi@herre.io",
    license="MIT",
    description="library information retrieval client (under development)",
    long_description=README,
    url="https://github.com/herreio/librair",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=required,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
)
