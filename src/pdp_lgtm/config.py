import os

import yaml

config_path = os.path.expanduser('~/.pdpconfig.yaml')

default_config = {
    'options': {
        'width': 1000,
        'height': 500,
        'history_size': 5,
    },
    'sections': [
        {
            'name': 'git',
            'words': [
                ['git', 'fetch --prune', 'branch -D', 'rebase -i'],
            ],
        },
    ],
}


def get_config():
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f, default_flow_style=False)
    with open(config_path) as f:
        config = yaml.safe_load(f)
        config['options'] = dict(
            default_config['options'], **config['options'])
        return config
