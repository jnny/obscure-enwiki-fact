import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="obscure-enwiki-fact",
    version="0.0.2",
    author="Jenny Ryan",
    author_email="jenny@peoplesopen.net",
    description="This simple command-line script uses Python and the requests library to give you a random sentence or two from an English Wikipedia page.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jnny/obscure-enwiki-fact",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
