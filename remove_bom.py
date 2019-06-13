#! /usr/bin/env python3

"""\
Remove byte order mark from a UTF-8-encoded text file.

    usage: remove_bom.py filename

Remove the byte order mark (U+FEFF) from the beginning of a
UTF-8-encoded text file, as it may occasionally confuse text
processing software.

Warning:  This changes the text file *in place*!
"""


import sys


def main():
    if len(sys.argv) != 2:
        print('usage', sys.argv[0], 'filename', file=sys.stderr)
        return

    try:
        filename = sys.argv[1]
        with open(filename, 'rb') as f:
            bom = f.read(3)
            if bom != b'\xef\xbb\xbf':
                print("File does not use byte order marker")
                return
            content = f.read()

        with open(filename, 'wb') as f:
            f.write(content)
        print("Byte order marker removed")

    except IOError as error:
        print(error, file=sys.stderr)
        return


if __name__ == '__main__':
    main()
