#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" test_shapefile.py - test for shapefile import
"""
from typing import List, Dict, Any
# may help when swapping virtual environments
import importlib
importlib.invalidate_caches()

# catch the wierd python import issues
try:
    import shapefile as sh
except ImportError as e:
    print("Import Error: ", e.args[0])
    quit()
else:
    print("Successfully imported 'shapefile' module. ")

def init_shapefile(filename: str = 'shapefile.shp') -> sh.Reader:
    """ read_shapefile - open and read a shapefile

        Keyword Arguments:
            filename {str} -- file name (default: {'shapefile.shp'})

        Returns:
            {shapefile} -- returns the reader object for the
                           shapefile that was initialized
        """
    init_shape: sh.Reader = None
    try:
        init_shape = sh.Reader(filename)
    except Exception as e:      # pylint: disable=broad-except
        print("Error opening {0}: {1}".format(filename, e.args[0]))
        quit()
    else:
        print("Reading shapefile {0} (filetype {1})".format(filename, type(init_shape)))
    return init_shape

def load_shapes(load_shape):
    """ read_shapefile - open and read a shapefile

        Keyword Arguments:
            filename {str} -- file name (default: {'shapefile.shp'})

        Returns:
            {shapefile} -- returns the reader object for the
                           shapefile that was initialized
        """
    load_result = load_shape
    return load_result

def wrap_count(wrap_dict: Dict, template: str = 'Key[{k}] : Count({v})') -> str:
    """ count_items - count occurrences of items in a list

        Keyword Arguments:
            wrap_dict {Dict[Any]}   -- input Dict
            template {str}          -- template for .format;
                use {k} for keys and {v} for values;
                default = 'Key[{k}] : Count({v})'

        Returns:
            {str} -- return formatted lines separated by \n
        """
    # https://realpython.com/python-string-formatting/
    # Changed in version 3.7: A format string argument is now positional-only.
    # https://docs.python.org/3/library/string.html#string-formatting

    template += ' % ('
    s = [template.format(k, v) for k, v in wrap_dict]
    s = '\n'.join()

def count_items(count_list: List[Any]) -> Dict[Any, int]:
    """ count_items - count occurrences of items in a list

        Keyword Arguments:
            count_list {List[Any]} -- input List

        Returns:
            {Dict} -- returns dictionary of counts for each item
        """
    # this is 2x slower than counter or create dict
    #  ... not good for large data sets
    #  ... just wanted to try it ...
    # https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item

    dict_count = dict([(j, count_list.count(j)) for j in set(count_list)])


if __name__ == "__main__":
    """ Tests for shapefile module (if run from CLI) """
    test_file: str = 'data/shapefile.shp'
    test_reader: sh.Reader = init_shapefile(test_file)
    test_shapes: sh.Reader.shapes = test_reader.shapes
    test_records: sh.Reader.records = test_reader.records
    nr: int = test_reader.numRecords

    print()
    print("Running shapefile checks ...")
    print()
    print(test_shapes)
    print("Name of shapefile: ", test_reader.shapeName)
    print("Number of records: ", nr)
    print("Encoding for shapefile: ", test_reader.encoding)
    print()
    test_record: sh.Reader.record = test_reader.record(0)
    test_shape: sh.Reader.shape = test_reader.shape(0)

    print("Record at index[0]: ", test_record)
    print("Info for shape object at index[0]")
    # print("  name: ", test_shape.shapeName)
    print("  type: ", test_shape.shapeType)
    print("  points: ", test_shape.points)
    print("  parts: ", test_shape.parts)
    print("  object type: ", type(test_shape))

    test_types: List[str] = [test_reader.shape(i).shapeTypeName for i in range(0, nr)]
    print()
    print()
    print()

    def countElement(a):
        g = {}
        for i in a:
            if i in g:
                g[i] += 1
            else:
                g[i] = 1
        return g

    l = [1, 2, 2, 5, 4, 3, 6, 6, 6, 4, 3, 8, 3, 3, 2, 1, 1, 1]
    l = ['a', 'b', 'c', 'b', 'a', 'c', 'a', 'b', 'd', 'f', 'e', 'j', 'e', 'a', 'v', 'e', 'w', 'f', 'd']
    print(countElement(l))

    wrap_count(l, p)
    print(q)

    p = '\n'.join(q)
    print(p)

    # print(test_types)
