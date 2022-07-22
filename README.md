# file_utilities

A collection of file utilities I made in my spare time.
These are written in Python, so at this time you will need Python 3.X installed on your machine.

## Deduplicator

Run from the command line with a file path as an argument, will leave only one copy of each file.
Uses a hash of the file contents, so differently named files with identical contents will be removed

Example, assuming you are in the directory containing deduplicator.py:
```python
$ D:\python\file_utilities\deduplicator> python deduplicator *path to folder I want to clean up*
```
