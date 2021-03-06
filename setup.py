"""Setup module"""

import os
import codecs
from setuptools import setup, find_packages

parent_dir = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(parent_dir, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='monitoring-scripts',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='Carpe Noctem Tactical Operations Services monitoring scripts',
    long_description=long_description,

    author='CNTO Research and Development branch',

    license='BSD 3-Clause License',

    classifiers=[],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'requests>=2.18.4,<3',
        'python-valve>=0.2.1,<1',
        'python-cachetclient>=0.2.4,<1',
    ],

    extras_require={
        'test': [
            'tox>=2.9,<3',
        ],
    },

    entry_points={
        'console_scripts': [
            'cnto-http-monitor=monitoring_scripts.http_monitor:http_entry_point',
            'cnto-ts3-monitor=monitoring_scripts.ts3_monitor:ts3_entry_point',
            'cnto-arma3-monitor=monitoring_scripts.arma3_monitor:arma3_entry_point',
            'cnto-check-runner=monitoring_scripts.check_runner:runner_entry_point',
        ],
    },
)
