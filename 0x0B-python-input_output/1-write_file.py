#!/usr/bin/python3
"""
Module contains function
that writes a string to a text file
"""


def write_file(filename="", text=""):
    i = 0
    """
    function writes string to a text file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        for word in text:
            for char in word:
                i += 1
    return (i) 
