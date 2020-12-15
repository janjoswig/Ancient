from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f_:
    long_description = f_.read()

setup(
    name='ancient',
    version="1.0.0",
    author="Jan-Oliver Joswig",
    author_email="jan.joswig@fu-berlin.de",
    description="Convert between integers and Roman numerals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janjoswig/Ancient",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
