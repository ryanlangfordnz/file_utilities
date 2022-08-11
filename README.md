# file_utilities

A collection of file utilities I made in my spare time.
These are written in Python, so at this time you will need Python 3.X installed on your machine.
When specifying any path, use the -p flag.

## Deduplicator

Run from the command line with a file path as an argument, will leave only one copy of each file.
Uses a hash of the file contents, so differently named files with identical contents will be removed.  
Example:

```
$ D:\python\file_utilities> python deduplicator -p *path to folder I want to clean up*
```

## Renamer

Run from the command line with a file path as an argument, and an additional flag to specify the mode.

-a: All files mode, all files at the location specified by the -p flag will be renamed to the argument given in the -a flag, keeping their file extensions.  
Example:

```
$ D:\python\file_utilities> python deduplicator -p *path to folder* -a *what to rename everything to*
```

-s: Single mode, all copies of the file specified by the -s flag will be renamed, the new name can be entered at the prompt.  
Example:

```
$ D:\python\file_utilities> python deduplicator -p *path to folder* -s *name of file you want to rename*
There are X copies of that file
Enter what you want to rename the files to. Copies will be in the format X_01,X_02 etc
New name: *new name here*
Renamed X files
```

## Timestamper

Run from the command line with a file path as an argument,a format for the time stamp, and an additional flag to specify the mode.

-f: Set the format of the timestamp using strftime conventions.

-c: Time stamp the files with the creation time of each file.  
Example:

```
$ D:\python\file_utilities> python timestamper -p *path to folder* -f *format e.g. %Y/%m/%d* -c
```

-m: Time stamp the files with the modificaction time of each file.  
Example:

```
$ D:\python\file_utilities> python timestamper -p *path to folder* -f *format e.g. %Y/%m/%d* -m
```

If you want to have spaces in your timestamp format rember to enclose the format argument in quotes.  
Example:

```
$ D:\python\file_utilities> python timestamper -p *path to folder* -f "%Y %m %d" -m
```
