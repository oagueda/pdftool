from setuptools import setup
setup(
    name = 'pdftool',
    version = '0.0.1',
    packages = ['pdftool'],
    entry_points = {
        'console_scripts': [
            'pdftool = pdftool.__main__:main'
        ]
    })
