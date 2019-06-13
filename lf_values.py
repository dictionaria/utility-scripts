#! /usr/bin/env python3

r"""\
Show values of `\lf` markers.

    usage: lf_values.py [sfm-database ...]

FLEx uses the `\lf`, `\lv`, and `\le` markers to store cross-references
in a SFM database.  This script outputs a list of all unique values for
`\lv` in one or more databases, along with a number, how often the value
occurs.

If no database is given, the SFM data is read from standard input.
"""


import fileinput
import re

from collections import Counter


def main():
    markers = Counter(
        line.split(maxsplit=1)[1].strip()
        for line in fileinput.input(openhook=fileinput.hook_encoded('utf-8'))
        if re.match(r'\\lf\s+\w', line))
    for marker, count in markers.most_common():
        print('{}\t{}'.format(count, marker))


if __name__ == '__main__':
    main()
