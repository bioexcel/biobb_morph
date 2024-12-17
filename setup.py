import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_morph",
    version="4.1.0",
    author="Biobb developers",
    author_email="mferri@bsc.es",
    description="Biobb_Morph is a wrapped version of a Python- and Abaqus-based code for producing patien-specific 3D meshes from IVD template examples.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_template",
    project_urls={
        "Documentation": "http://biobb-template.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['docs']),
    package_data={'biobb_morph': ['py.typed']},
    install_requires=['biobb_common==4.1.0'],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "template = biobb_morph.biobb_morph.morph:main"
        ]
    },
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix"
    ),
)
