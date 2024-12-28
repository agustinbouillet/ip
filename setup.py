# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='ip',
    version='0.0.1',
    # py_modules = ['cuit'],
    author='Agustin Bouillet',
    author_email='agustin.bouillet@gmail.com',
    url='https://www.bouillet.com.ar/',
    long_description_content_type="text/markdown",
    description='Obtención de IP',
    long_description='Permite obtener una ip pública, local o de una red.',
    keywords = ['ip', 'network', 'public',],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8",
)