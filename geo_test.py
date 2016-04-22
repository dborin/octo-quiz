#! /usr/bin/env python

import json
import os
import unittest
import urllib2


class GeoTestCase(unittest.TestCase):

    # Addresses or locations can't have spaces (replace with + )
    location = os.getenv('GEO_API_TEST_LOCATION', '88+Colin+P+Kelly+Jr+St,+San+Francisco,+CA')
    # Coordinates can't have spaces
    coordinates = os.getenv('GEO_API_TEST_COORDINATES', '37.779263,-122.419729')
    key = os.getenv('GEO_API_TEST_KEY')

    def get_result_count(self, req):
        myresponse = urllib2.urlopen(req)
        myjson = json.loads(myresponse.read())
        count = 0
        for result in myjson['results']:
            if result['geometry']:
                count += 1

        return count

    def test_human_readable(self):
        req = urllib2.Request(url="https://maps.googleapis.com/maps/api/geocode/json?address=" + self.location +
                                  "&key=" + self.key)

        # There should be only 1 'geometry' entry when using a location
        self.assertEqual(self.get_result_count(req), 1)

    def test_latlng(self):
        req = urllib2.Request(url="https://maps.googleapis.com/maps/api/geocode/json?latlng=" + self.coordinates +
                                  "&key=" + self.key)

        # There should be > 1 'geometry' entry when using coordinates
        self.assertGreater(self.get_result_count(req), 1)

def suite():
    tests = ['test_human_readable', 'test_latlng']
    return unittest.TestSuite(map(GeoTestCase, tests))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
