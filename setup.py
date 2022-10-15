from setuptools import find_packages, setup

setup(
    name="launchbox-plugin",
    description="A python helper class for integrating Launchbox plugins",
    author="NASA-JPL",
    author_email="dl-webdev@jpl.nasa.gov",
    url="https://github.com/nasa-jpl/launchbox-plugin",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["bottle==0.12.20"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
