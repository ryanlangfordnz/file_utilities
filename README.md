# file_utilities

A collection of file utilities I made in my spare time.
These are written in Python, so at this time you will need Python 3.X installed on your machine.
When specifying any path, use the -p flag.

## Deduplicator

Run from the command line with a file path as an argument, will leave only one copy of each file.
Uses a hash of the file contents, so differently named files with identical contents will be removed

Example, assuming you are in the directory containing deduplicator.py:

```
$ D:\python\file_utilities\deduplicator> python deduplicator -p *path to folder I want to clean up*
```
