import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name="RegexPicker plugin",
    version="0.1",
    author="Greg L. Turnquist",
    author_email="Greg.L.Turnquist@gmail.com",
    description="Pick test methods based on a regular expression",
    license="Apache Server License 2.0",
    py_modules=["recipe13_plugin"],
    entry_points = {
        'nose.plugins': [
            'recipe13_plugin = recipe13_plugin:RegexPicker'
            ]
    }
)

setup(
    name="CSV report plugin",
    version="0.1",
    author="Greg L. Turnquist",
    author_email="Greg.L.Turnquist@gmail.com",
    description="Generate CSV report",
    license="Apache Server License 2.0",
    py_modules=["recipe14_plugin"],
    entry_points = {
        'nose.plugins': [
            'recipe14_plugin = recipe14_plugin:CsvReport'
            ]
    }
)

