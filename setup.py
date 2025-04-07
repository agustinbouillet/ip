# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='ip',
    version='0.0.3',
    author='Agustin Bouillet',
    author_email='agustin.bouillet@gmail.com',
    url='https://www.bouillet.com.ar/',
    long_description_content_type="text/markdown",
    description='Obtención de IP',
    long_description='Permite obtener una ip pública, local o de una red.',
    keywords = ['ip', 'network', 'public',],
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    install_requires=[
        'setuptools==66.1.1',
    ],
    entry_points={
        'console_scripts': [
            'ip = ip.__main__:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Bug Tracker": "hhttps://github.com/agustinbouillet/ip/issues",
        "Source Code": "https://github.com/agustinbouillet/ip",
    },

)