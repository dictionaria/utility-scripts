Dictionaria Tiny Utils
======================


Introduction
------------

This repository contains a small collection of utility scripts for working with
SFM dictionaries.  These scripts are probably most useful for Windows users.  On
Unix-like systems most of these tasks can be accomplished directly on the
command-line using [sed][sed], [awk][awk], [grep][grep], etc.

[awk]: https://man.openbsd.org/POSIX-2013/awk
[grep]: https://man.openbsd.org/POSIX-2013/grep
[sed]: https://man.openbsd.org/POSIX-2013/sed


Included programs
-----------------

## `cdstar_files.py`

Output all media files attached to a submission.

    usage: cdstar_files.py [cdstar json file] submission-id

If the first argument is omitted the program will look for a file called
`cdstar.json` in the current working directory.


## `lf_values.py`

Show values of `\lf` markers.

    usage: lf_values.py [sfm-database ...]

FLEx uses the `\lf`, `\lv`, and `\le` markers to store cross-references
in a SFM database.  This script outputs a list of all unique values for
`\lv` in one or more databases, along with a number, how often the value
occurs.

If no database is given, the SFM data is read from standard input.


## `remove_bom.py`

Remove byte order mark from a UTF-8-encoded text file.

    usage: remove_bom.py filename

Remove the byte order mark (U+FEFF) from the beginning of a
UTF-8-encoded text file, as it may occasionally confuse text
processing software.

Warning:  This changes the text file *in place*!


## `sfm_markers.py`

Show all SFM markers.

    usage: sfm_markers.py [sfm-database ...]

Show a list of all SFM markers used in one or more SFM database.  This
script outputs a list of all markers, along with a number, how often
the value occurs.

If no database is given, the SFM data is read from standard input.


## `unique_glosses.py`

Show all gloss abbreviations.

    usage: unique_glosses.py [sfm-database ...]

Output a list of all abbreviations used in glosses (i.e. `\gl` and `\xeg`
markers).

If no database is given, the SFM data is read from standard input.


## `valid_json.py`

Check JSON file for errors.

    usage: valid_json.py filename

Check if the contents of a file are valid JSON and print an error
message if they are not.
