import pathlib
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


# This call to setup() does all the work
setuptools.setup(
    name="tpyfilestructure",
    version="0.0.1",
    description="Python package to read and display the file/folder names present in a directory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tarun571999/tpyfilestructure",
    author="Tharun Kumar T",
    author_email="tarunkumar571999@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "tpyfilestructure=tpyfilestructure.__main__:main",
        ]
    },
    python_requires ='>=3.7',
)