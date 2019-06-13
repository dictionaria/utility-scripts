#! /usr/bin/env python3

r"""\
Show all gloss abbreviations.

    usage: unique_glosses.py [sfm-database ...]

Output a list of all abbreviations used in glosses (i.e. `\gl` and `\xeg`
markers).

If no database is given, the SFM data is read from standard input.
"""


import fileinput
import re

GLOSS_MARKERS = {'\\gl', '\\xeg'}


def is_glossed(s):
    try:
        return s.split()[0] in GLOSS_MARKERS
    except IndexError:
        return False


def main():
    lines = fileinput.input(openhook=fileinput.hook_encoded('utf-8'))
    glosses = {
        morpheme
        for line in filter(is_glossed, lines)
        for morpheme in re.split(r'(\s|[.-])+', line)
        if re.search('[A-Z][A-Z]', morpheme)}

    print('\n'.join(sorted(glosses)))


if __name__ == '__main__':
    main()
