# pdp-lgtm
party of dope pajamas looks good to me.

# summary
this package provides a cli tool `pdp`, it composes commands from predefined words and arguments

# install
    pip install pdp-lgtm
needs tk to run, make sure os specific python-tk connector is installed.

# example
![demo](https://media.giphy.com/media/MFNwY4VbCfHWnxZYjp/giphy.gif)

- run `pdp`
- flip to git tab, press `git` then `fetch --prune`
- press enter

# configuration

edit `~/.pdpconfig.yaml` to add tabbed sections and change width / height. config file is auto generated after first run. history is saved as `~/.pdphistory.yaml`.

# actions

- click a word to append it to the entries.
- `enter`: print and run command.
- `esc`: print command but don't run.
- `backspace`: on an empty entry to remove it.
- `tab`: on an entry to move to the next one.
- `up`: on an entry to increment if it's an integer.
- `down`: on an entry to decrement if it's an integer.
- `shift` or other special keys: flip tab.

# develop
to release make a tag like v0.1 that matches package version

    python3 setup.py sdist
    python3 -m twine upload dist/*
