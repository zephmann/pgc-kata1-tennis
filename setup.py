# :coding: utf-8

import os.path
import setuptools

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_PATH = os.path.join(ROOT_PATH, "source")
README_PATH = os.path.join(ROOT_PATH, "README.rst")

# with open(README_PATH, "r") as fh:
#     long_description = fh.read()
long_description = "Placeholder"

# Compute dependencies.
INSTALL_REQUIRES = []

APP_REQUIRES = [
    "flask >= 1, < 2",
]

TEST_REQUIRES = [
    "pytest >= 4, < 5",
]


setuptools.setup(
    name="tennis",
    version="0.1.0",
    author="Zephyr Mann",
    author_email="zephmann@gmail.com",
    description="Tennis score keeper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zephmann/pgc_kata1_tennis",
    packages=setuptools.find_packages(SOURCE_PATH),
    package_dir={
        "": "source"
    },
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    extras_require={
        "test": TEST_REQUIRES,
        "app": APP_REQUIRES,
        "dev": TEST_REQUIRES + APP_REQUIRES,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    # entry_points={
    #     "console_scripts": [
    #         "synes = synes.command_line:main"
    #     ]
    # },
)
