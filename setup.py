import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytest-greendots',
    license='MIT',
    description='Green progress dots',
    long_description=read("README.rst"),
    version='0.1',
    py_modules=['pytest_greendots'],
    entry_points={'pytest11': ['greendots = pytest_greendots']},
    install_requires=['pytest>=2.0', 'blessings'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ]
)
