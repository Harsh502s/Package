from setuptools import setup

setup(
    name="Astras",
    version="0.1",
    packages=setup.find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn"
    ],
    author="Your Name",
    description="Package for Classification and Regression",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
