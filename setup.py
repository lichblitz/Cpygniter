#!/usr/bin/env python
"""
Setup for SQLAlchemy backend for Apache Ignite
"""

from setuptools import find_packages, setup
import os

setup(
        name="cpygniter"
        verion="0.0.1"
        author="Carlos Cortes"
        author_email="carloscortespa@gmail.com"
        url="https://github.com/lichblitz/Cpygniter"
        project_urls={
            "Documentation": "",
            }
        description="Pure python SqlAlchemy dialect for Apache Ignite"
        packages=find_packages(),
        python_require=">=3.6",
        extras_require={
            "pyignite"
            }
        entry_points={
            "sqlalchemy.dialects": [
                "cpygniter = cpygniter.connections::Connection"
                ]
            }
    )
