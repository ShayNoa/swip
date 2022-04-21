from setuptools import setup, find_packages

setup(
    name='swip',
    package_dir={"": "swip"},
    packages=find_packages(where='swip'),
    include_package_data=True,
    license='MIT',
    version='0.0.1',
    description='A basic implementation of the version control system Git ',
    author='Noa Shay',
    author_email='nogaos97@gmail.com',
    url='https://github.com/ShayNoa/swip',
    install_requires=[
        'loguru',
        'graphviz',
        'colorama',
	    'termcolor',
        'wheel'
    ],
    entry_points={
        'console_scripts': ['swip=swip:main'],
    }
)