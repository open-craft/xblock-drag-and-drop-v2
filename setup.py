# -*- coding: utf-8 -*-

# Imports ###########################################################

import os
from setuptools import setup


# Functions #########################################################

def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


# Main ##############################################################

setup(
    name='xblock-drag-and-drop-v2-new',
    version='2.1.3',
    description='XBlock - Drag-and-Drop v2',
    packages=[],
    install_requires=[
        'xblock-drag-and-drop-v2',
    ],
    entry_points={
        'xblock.v1': 'drag-and-drop-v2-new = drag_and_drop_v2:DragAndDropBlock',
    },
)
