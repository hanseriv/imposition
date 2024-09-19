#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:42:30 2024
@author: jean.troussier
obj : test des fonctions principales
"""

import fonctioncalendrier as fc

print(fc.readingdate("hello i'm happy with my life"))
print(fc.readingdate("01/15/225"))
print(fc.readingdate("22/45/1965"))
print(fc.is_your_year_bisextil(1900))