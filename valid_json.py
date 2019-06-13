#! /usr/bin/env python3

"""\
Check JSON file for errors.

    usage: valid_json.py filename

Check if the contents of a file are valid JSON and print an error
message if they are not.
"""


import sys
import json


def main():
    if len(sys.argv) != 2:
        print('usage', sys.argv[0], 'filename', file=sys.stderr)
        return
    filename = sys.argv[1]

    try:
        with open(filename, encoding='utf-8') as f:
            _ = json.load(f)
    except IOError as error:
        print('{}: {}'.format(sys.argv[0], str(error), file=sys.stderr))
        return
    except json.JSONDecodeError as error:
        print('Invalid JSON:', error)
        return

    print('Valid JSON.')


if __name__ == '__main__':
    main()
