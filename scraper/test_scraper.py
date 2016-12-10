#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Scraper module

@ase4156-backend: Ian
"""
#pylint: disable=E1101, E1120


# Code coverage start
from coverage import coverage
cov = coverage(branch=True, omit=['/Library/*',
                                  '/usr/local/lib/python2.7/site-packages/*',
                                  # 'scraper/test_scraper.py',
                                  'server/*'])
cov.start()


import unittest
from test_events_scraper import *
from test_data_importer import *
from test_data_cleaner import *


unittest.main()
cov.stop()
cov.save()
print("\n\nCoverage Report:\n")
cov.report()

cov.html_report(directory='scraper/coverage_report')
cov.erase()