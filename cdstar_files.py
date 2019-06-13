#! /usr/bin/env python3

"""\
Output all media files attached to a submission.

    usage: cdstar_files.py [cdstar json file] submission-id

If the first argument is omitted the program will look for a file called
`cdstar.json` in the current working directory.
"""


import json
import sys


def main():
    if len(sys.argv) == 2:
        cdstar_file = 'cdstar.json'
        lang = sys.argv[1]
    elif len(sys.argv) == 3:
        cdstar_file = sys.argv[1]
        lang = sys.argv[2]
    else:
        print('usage:', sys.argv[0], 'submission-id', file=sys.stderr)
        return

    try:
        with open(cdstar_file, encoding='utf-8') as f:
            db = json.load(f)
    except (IOError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return

    filenames = {
        entry['fname']
        for entry in db.values()
        if 'fname' in entry and entry.get('sid') == lang}
    filenames = sorted(filenames)

    for filename in filenames:
        print(filename)


if __name__ == '__main__':
    main()
