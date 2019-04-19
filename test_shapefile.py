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
    except FileNotFoundError as e:
        print("The shapefile (", filename, ") was not found.")
        print(e.args)
    except TypeError as e:
        print("The shapefile (", filename, ") is the wrong type (", type(filename), ").")
        print(e.args)
    except ValueError as e:
        print("The shapefile (", filename, ") has a badly formatted filename.")
        print(e.args)
    except OSError as e:
        print("The shapefile (", filename, ") caused an OS error.")
        print(e.args)
    except Exception as e:      # pylint: disable=broad-except
        print("The shapefile (", filename, ") caused an unknown error.")
        print(e.args)
    else:
        print("Reading shapefile (", filename, ") of type (", type(filename), ").")
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


if __name__ == "__main__":
    """ Tests for shapefile module (if run from CLI) """
    test_file: str = 'shapefile.shp'
    test_reader: sh.Reader = init_shapefile(test_file)
    print("Encoded name of shapefile: ", test_reader.shapeName)
    print("Number of records: ", test_reader.numRecords)
    print()
    print("Record at index[0]: ", test_reader.record(0))
    print("Shape at index[0]: ", test_reader.sh)
    test_shapes: sh.Reader.iterShapes = test_reader.iterShapes
    test_records: sh.Reader.iterRecords = test_reader.iterRecords
    print(len(test_shapes))
    # if reader.
    # continue ...
