#!/usr/bin/env python

from distutils.core import setup
setup(
  name = 'jargparse',
  packages = ['jargparse'], # this must be the same as the name above
  version = '0.0.4',
  description = 'A tiny super-dumb module just because I like to see the usage info on stdout on an error.  jargparse.ArgParser just wraps argparse.ArgParser',
  author = 'Justin Clark-Casey',
  author_email = 'justincc@justincc.org',
  url = 'https://github.com/justinccdev/jargparse', # use the URL to the github repo
  keywords = ['logging'], # arbitrary keywords
)
