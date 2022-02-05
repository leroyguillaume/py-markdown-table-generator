from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="markdown_table_generator",
    version="1.0.1",
    author="Guillaume Leroy",
    author_email="pro.guillaume.leroy@gmail.com",
    description="Library to generate Markdown table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leroyguillaume/py-markdown-table-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["typing"],
    entry_points={
        "console_scripts": [
            "csv-to-md = markdown_table_generator:__csv_to_md"
        ]
    }
)
