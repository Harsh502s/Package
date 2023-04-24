from setuptools import setup

setup(
    name="Astras",
    version="0.1",
    packages=setup.find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "xgboost",
        "catboost",
    ],
    author="Harshit Singh",
    author_email="harsh502singh@gmail.com",
    url='https://github.com/Harsh502s/Astras',
    description="Package for Classification and Regression",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10"
    )
