from setuptools import setup

setup(
    name='configsaver',
    version='0.0.1',
    author='Blackwell',
    author_email='friendlyblackwell@example.com',
    url='https://github.com/friendlyblackwell/configsaver',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    description='Common Config Reader',
    packages=['configsaver'],
    install_requires=[
        "PyYAML",
    ]
)
