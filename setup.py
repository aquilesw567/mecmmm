from setuptools import setup, find_packages

setup(
    name='your_package_name',  # Replace with your package name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyQt6',
        'Pygments',
        'GitPython',
    ],
)