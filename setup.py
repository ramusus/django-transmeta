from setuptools import setup
from setuptools import find_packages

version = '0.2'

setup(
    name='django_transmeta',
    version=version,
    description="Model translation for Django",
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers = ['Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Internationalization',
        ],
    keywords='django i18n translation',
    author='Marc Garcia',
    author_email='garcia.marc@gmail.com',
    url='http://code.google.com/p/django-transmeta/',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
)
