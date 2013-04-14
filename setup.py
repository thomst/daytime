from distutils.core import setup

VERSION = "0.1"

setup(
    name = "daytime", 
    version = VERSION, 
    author = "Thomas Leichtfuss", 
    author_email = "thomaslfuss@gmx.de",
    url = "https://github.com/thomst/daytime",
    download_url = "https://pypi.python.org/packages/source/t/daytime/daytime-{version}.tar.gz".format(version=VERSION),
    description = 'has to be written...',
    long_description = "This module extends the datetime.time-module and makes it more handy respectivly to comparison, addition and substraction. You can compare, add and substract a daytime-object with other daytime-objects or with an integer as the amount of seconds. You can also compare a daytime- with a datetime.time-object.",
    py_modules = ["daytime"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
    license='GPL',
    keywords='datetime time daytime comparison',
)
