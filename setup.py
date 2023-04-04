from setuptools import setup, find_packages
from setuptools_cythonize import get_cmdclass


with open('README.rst', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    license_ = f.read()

setup(
    cmdclass=get_cmdclass(),
    name='priori',
    version='0.0.1',
    description='scientific calculation toolkit',
    long_description=long_description,
    author='ChenZHANG',
    author_email='chen.zhang_06sept@foxmail.com',
    maintainer='ChenZHANG',
    maintainer_email='chen.zhang_06sept@foxmail.com',
    url='https://github.com/CubicZebra/priori',
    license=license_,
    # install_requires=['typing'],
    setup_requires=['setuptools', 'setuptools_cythonize'],
    test_requires=['pytest'],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(),
    options={
        'build_py': {'exclude_cythonize': ['src.docs*']}
    }
)
