import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='sqlshards',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',  # example license
    description='SQL sharding implementation in Django.',
    long_description=README,
    url='https://github.com/gojohnkevin/sqlshards',
    author='John Kevin Go',
    author_email='kevin@thekevingo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.4',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
