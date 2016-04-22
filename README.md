# octo-quiz
Otherwise known as the Github coding challenge for David Borin

###Initial Notes
A decent amount of time was spent investigating different approaches:

* Use of a BDD framework was considered (`behave` or `pytest-bdd`)
* Use of pre-written tools to test (REST) APIs (i.e. `pyresttest`)
* Using `argparse` or `optparse` to pass in test data (`unittest` doesn't play well with competing command-line args)

**As someone who has had to grade code challenges, based upon my  experience of being forced to jump through too many hoops to get a code challenge installed and running, I opted to use only native Python modules.** 

This resulted in a much simpler test tool, but it should mean that a basic Python 2.7 install is all that is required.

If this were an actual scalable test harness, external tools and modules, which probably would have greatly increased installation overhead and complexity, would have been used.

I learned a great deal about what and how I wanted to test in the API through a few hours of experimentation.  Given more time, I'm sure that other avenues of testing would be exposed.

For purposes of this challenge, we can assume that Google is getting the actual conversion(s) correct, and that trying to find a third party to spot check their mapping "math" is way beyond the scope of this exercise (but an interesting test case).

This was written / tested using Python 2.7.3 on Ubuntu 15.10

###Test Plan
The following is for testing the [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro).  It tests two major pieces of the API's basic functionality.

* Validate that if a human readable address (location) is used, the returned JSON contains at just one (1) `geometry` entry.
* Validate that if latitude and longitude are used, the returned JSON contains > 1 `geometry` entries.

###Running the tests

	    $ ./geo_test.py

This will run tests with default data:

		location = 88+Colin+P+Kelly+Jr+St,+San+Francisco,+CA
		coordinates = 37.779263,-122.419729

These are the Github corporate office address and San Francisco City Hall, respectively.

You can use env vars to specify different test data:

		GEO_API_TEST_LOCATION
		GEO_API_TEST_COORDINATES

###More Notes

* I only tested JSON responses.  
* I linted against 120 char length lines.  (80 was nice when we didn't have 1440 x 900 resolution laptops.  Now it just makes things hard to read IMHO)
* The `results` from either a location (address) or lat/long query provide the same data (`geometry`, `address_components` and `formatted_address`), so testing the number of instances of these data is a better metric for the respective query.
* I used env vars as a fast way to allow for testing other places and bad data.  Given a refactor, I might add the ability to read in a config file.
* Since this is a private repo and a code challenge I want to keep simple, I was "ok" leaving the throw-away API key in the codebase.  This is **NOT** my regular practice (and the key will get deleted on Tuesday afternoon).
* I am not a performance test engineer.  I'll refrain from presenting perf test cases beyond the obvious "it should be fast".

####TODO List
*(AKA The tests I'd write if I had 3 months to really put the API under test and I still worked at Google)*

This is by no means an exhaustive list. It is implied that most (all) tests will be run against the "regular" Geocoding (location) and "reverse" (lat / long) (where applicable).

* There should be some repeat testing to ensure that the XML responses contain the correct information and are well formed.
* Validate that the returned data contains all the designed, intended structures
* Using coordinates can return different amounts of `geometry`, `address_components` and `formatted_address` sets, so validating that the right amount and "depth" of these sets would be useful.  Depth means `address_components` that range from "country" to "street number" and combinations therein.
* The list of options, parameters, filters and modifiers is enormous and not useful to list here, but ideally most (all) of these would be tested.
* Making sure that bad data requests are handled gracefully.  This could be in conjunction with the previous bullet point.
* Validate the various payment plan access limits.
* Validate status codes.

</br>
</br>
</br>
</br>
</br>
</br>
<hr>
> Written with [StackEdit](https://stackedit.io/).
