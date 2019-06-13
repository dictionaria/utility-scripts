#! /usr/bin/env python3

r"""\
Show all SFM markers.

    usage: sfm_markers.py [sfm-database ...]

Show a list of all SFM markers used in one or more SFM database.  This
script outputs a list of all markers, along with a number, how often
the value occurs.

If no database is given, the SFM data is read from standard input.
"""


import fileinput

from collections import Counter


def main():
    markers = Counter(
        line.split(maxsplit=1)[0]
        for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8'))
        if line.startswith('\\'))
    for marker, count in markers.most_common():
        print('{}\t{}'.format(count, marker))


if __name__ == '__main__':
    main()
