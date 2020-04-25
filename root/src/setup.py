import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="primes-TomasZilinek",
    version="0.0.1",
    author="Tomas Zilinek",
    author_email="tomas.zilinek@gmail.com",
    description="small python package for computing primes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TomasZilinek/ossdev-02-485115",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

