from setuptools import find_packages, setup

setup(
    name='optimizedselenium',
    packages=find_packages(),
    version='0.1.6',
    description='generate selenium driver and common action based on selenium',
    author='ntony',
    license='GPL',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='test',

)