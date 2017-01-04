# Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# Although you can include files like this:
#
#  .. include _includes/common_includes.txt
#
# Adding this to the rst_prolog/rst_epilog would break includes for topics that exist in
# subdirectories of the 'source' directory.
#
# Instead, we simply gather the information that exists in the default include locations and make
# *that* the rst_epilog.

import os, codecs

# start with a newline, in case the file doesn't end with one...
rst_epilog = '\n'

common_includes = [
    '_includes/common_includes.txt',
    '_includes/guide_links.txt',
    '_includes/service_links.txt',
    '_includes/region_includes.txt',
    '_includes.txt'
    ]

for i in common_includes:
    if os.path.exists(i):
        f = codecs.open(i, 'r', 'utf-8')
        rst_epilog += f.read()
        f.close()

if 'exclude_patterns' not in vars():
    exclude_patterns = []

exclude_patterns.append('README.*')

