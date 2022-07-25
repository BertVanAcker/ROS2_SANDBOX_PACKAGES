from setuptools import setup

package_name = 'ros2_publisher_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Van Acker Bert',
    author_email='bva.bmkr@gmail.com',
    maintainer='Van Acker Bert',
    maintainer_email='bva.bmkr@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A getting started ROS2 Python package',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ros2_publisher_py.Main:main'
        ],
    },
)
