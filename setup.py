#!/usr/bin/env python

METADATA = dict(
    name='django-transmeta',
    version='0.1',
    author='msaelices, fidelramos, ramusus',
    description='Tracks the official SVN repository at Google Code',
    long_description=open('README').read(),
    url='http://github.com/ramusus/django-transmeta',
)

if __name__ == '__main__':
    try:
        import setuptools
        setuptools.setup(**METADATA)
    except ImportError:
        import distutils.core
        distutils.core.setup(**METADATA)
