#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
     packages=['ros_package_a', 'package_bar', 'package_foo'],
     package_dir={'': 'src'}
)

setup(**setup_args)
