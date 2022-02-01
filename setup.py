import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="perp-cex-api",
    version="0.0.1",
    author="wrnj43",
    author_email="wrnj43@gmail.com",
    description="Python API for perp.fi similar to centralized exchange APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wrnj43/perp-cex-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    python_requires='>=3.6',
    install_requires=[
        'web3 >= 5.12.2',
    ],
)