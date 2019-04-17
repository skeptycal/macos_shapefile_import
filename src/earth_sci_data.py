#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" intro_vector_data_py - test using the tutorial at :
    https://www.earthdatascience.org/workshops/gis-open-source-python/intro-vector-data-python/
"""
# import necessary packages
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

# plot data inline
plt.ion()

# set working directory
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
