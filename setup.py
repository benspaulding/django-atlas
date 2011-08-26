from distutils.core import setup


setup(
    name='django-atlas',
    version='0.1',
    description='Ghetto-style geo app for Django.',
    url='http://github.com/benspaulding/django-atlas/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.com',
    license='BSD',
    packages = ['atlas'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP :: Site Management'],
)
