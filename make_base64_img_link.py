#!/usr/bin/env python3

"""
Create base64 links from image files, suitable for
embedding in an html file.

Takes a directory name as an argument. For each
PNG file, creates a
text file called <infile name>_base64.txt, containing
an img tag suitable for pasting into html code.

Copyright 2019 by Tony Rein

uses:
base64
pathlib.Path
sys (for argv)
"""
import base64
from pathlib import Path 
import sys

def get_image_file_list(dirpath):
    hits = []
    suffixes = [ '.png' ]
    for suffix in suffixes:
        for subpath in dirpath.glob('*'):
            ext = subpath.suffix
            if ext.lower() == suffix:
                hits.append(dirpath / subpath.name)
    return hits

def make_outfile_name(infile):
    return f"{infile}_base64.txt"

def make_encoded_string(infile):
    with open(infile, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

def write_to_outfile(outfile_name, encoded_string):
    stem = '<img src="data:image/png;base64,'.encode('utf-8')
    tail = '">'.encode('utf-8')
    bytes_to_write = stem + encoded_string + tail
    with open(outfile_name, "wb") as f:
        f.write(bytes_to_write)

def make_outfile(infile):
    outfile_name = make_outfile_name(infile)
    print(f"Processing {outfile_name}...")
    encoded_string = make_encoded_string(infile)
    write_to_outfile(outfile_name, encoded_string)

def make_outfiles(infiles):
    outfile_count = 0
    for infile in infiles:
        make_outfile(infile)
        outfile_count += 1
    return outfile_count

def main():
    if len(sys.argv) != 2:
        print("Please supply a directory name.")
        sys.exit(1)
    dirpath = Path(sys.argv[1])
    if not dirpath.is_dir():
        print(f"{dirpath.name} is not a directory.")
        sys.exit(2)
    
    infiles = get_image_file_list(dirpath)
    files_made = make_outfiles(infiles)
    print(f"{files_made} files created.")
    sys.exit(0)

if __name__=="__main__":
    main()
