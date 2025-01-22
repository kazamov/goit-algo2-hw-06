from setuptools import setup, find_packages

setup(
    name='goit-algo2-hw-06',
    version='0.1.0',
    author='Zakir Nuriiev',
    author_email='kazamov@gmail.com',
    description='Go IT algorithms homework 06',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kazamov/goit-algo2-hw-06',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)