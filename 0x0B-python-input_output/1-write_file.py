#!/usr/bin/python3
"""
Module contains function
that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    function writes string to a text file
    """
    if filename == False or filename == NULL:
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(text)
