from setuptools import setup, find_packages

setup(
    name="py-fst",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "rpy2>=3.4.0",
    ],
    author="transparentlyadmin",
    author_email="mauro@sauco.net",
    description="Python wrapper for the R fst package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/transparentlyadmin/py-fst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)