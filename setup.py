from setuptools import setup, find_packages

setup(
    name="credit-scoring",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.1.0",
        "numpy>=1.24.3",
        "scikit-learn>=1.3.0",
        "xgboost>=2.0.0",
        "fastapi>=0.103.0",
        "uvicorn>=0.23.2",
        "pydantic>=2.3.0",
    ],
    python_requires=">=3.11",
)
