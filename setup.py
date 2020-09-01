# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

with open("requirements.txt","r",encoding="utf-8") as f:
    requirements = [i.strip() for i in f.readlines()]

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='thaidp',
    version='0.1dev0',
    description="ThaiDP = Thai Data Privacy Tool For Python",
    author='Wannaphong Phatthiyaphaibun',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='wannaphong@kkumail.com',
    url='https://github.com/wannaphong/Thai-Data-Privacy',
    packages=find_packages(),
    package_data={'': ['LICENSE','README.md']},
    include_package_data=True,
    test_suite="tests",
    install_requires=requirements,
    license='Apache Software License 2.0',
    zip_safe=False,
    keywords='Data Privacy',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: Implementation'],
)
