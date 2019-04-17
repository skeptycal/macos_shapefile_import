#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" test_shapefile.py - test for shapefile import
"""
try:
    import shapefile as sh
except ImportError as e:
    print("Error importing 'shapefile' module. ")
    print(e.args)
else:
    print("Successfully imported 'shapefile' module. ")

def read_shapefile(filename: str = 'shapefile.shp', shape_test: sh.Reader = sh_reader) -> sh.Reader:
    """ read_shapefile - open and read a shapefile

    Keyword Arguments:
        filename {str} -- file name (default: {'shapefile.shp'})

    Returns:
        {shapefile} -- returns the shapefile that was read
    """

    try:
        shape_test = sh.Reader(filename)
    except FileNotFoundError:
        print("The shapefile (", filename, "was not found.")
    except TypeError:
        print("The shapefile (", filename, "is the wrong type (", type(filename), ").")
    except ValueError:
        print("The shapefile (", filename, "has a badly formatted filename.")
    else:
        print("Reading shapefile (", filename, ") of type (", type(filename), ".")
        return shape_test


if __name__ == "__main__":
    """ Tests for shapefile module (if run from CLI) """
    test_file: str = 'shapefile.shp'

    shape_test: sh.Reader


    reader = read_shapefile(test_file)
    # continue ...
