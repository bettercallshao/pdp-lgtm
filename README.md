# pdp-lgtm
party of dope pajamas looks good to me.

# summary
this package provides a cli tool `pdp`, it composes commands from predefined words and arguments

# example
## compose from predefined words
    echo "google.com amazon.ca host" >> ~/.pdp
    pdp
you can click on words in the order you would type in bash then press <Enter>, observe that that command is run.

## compose from argument
    pdp github.com
you can also click on github.com now as a word.

## compose from stdin
    history | pdp -

## adjust numbers
    pdp expr 5 + 5
after adding all words in arguments, press + / = / - / _ to observe the first integer word increment / decrement.

## adjust height
    export NROWS=20
    pdp

# develop
make a tag like v0.1 that matches package version
    python3 setup.py sdist
    python3 -m twine upload dist/*
