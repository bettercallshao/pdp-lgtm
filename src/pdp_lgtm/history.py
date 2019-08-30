# -*- coding: utf-8 -*-
"""History management routines."""

import os

import yaml

from .config import get_config

history_path = os.path.expanduser('~/.pdphistory.yaml')
size = get_config()['options']['history_size']


def get_history():
    if os.path.exists(history_path):
        with open(history_path) as f:
            return yaml.safe_load(f)[-size:]
    else:
        return []


def put_history(l):
    h = [a for a in get_history() if a != l]
    h.append(l)
    h = h[-size:]
    with open(history_path, 'w') as f:
        yaml.dump(h, f, default_flow_style=False)
