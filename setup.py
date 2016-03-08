from setuptools import setup

setup(
    name='lint',
    version='0.1',
    py_modules=['lint'],
    entry_points='''
        [console_scripts]
        lint=lint:lint
    ''',
)
