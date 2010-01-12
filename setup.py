import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-atlas',
    version='0.8.0',
    description='Ghetto-style geo app for Django.',
    url='http://github.com/benspaulding/django-atlas/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.com',
    license='BSD',
    download_url='http://github.com/benspaulding/django-atlas/tarball/v0.8.0',
    long_description = read('README'),
    packages = ['atlas'],
    package_data = {'atlas': ['locale/*/LC_MESSAGES/*']},
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP :: Site Management'],
)
