# MPCS 51042, Python Programming

**Homework 4**

**Due**: April 23 at 12:00pm CT

For each problem, you are to submit a file named `problem<N>.py` where `<N>` is the number of the problem (e.g. `problem1.py`).

## Problem 1

In JavaScript, the Array datatype (somewhat equivalent to Python's `list`) has a number of methods which `list` in Python does not have. For this problem, you are to write a subclass of `list` that provides some of these methods.

### Specifications

- The class should be named `ESArray` and should inherit from the built-in `list` class.
- The `join` method should accept a string, `s` as its only argument (other than `self`) and return a string that results from joining each item in the list by the string `s`.
- The `every` method tests whether all items in the list pass a test implemented by a provided function.
- The `for_each` method executes a provided function function once for each item in the list.
- The `flatten` method returns a new `ESArray` with all list-like items in the original list flattened. That is, calling `flatten()` on a nested list returns a single list with all items appearing the their original order but with no nesting.

### Example Interaction

```pycon
>>> x = ESArray([1, -3, 10, 5])
>>> x.join('**')
'1**-3**10**5'
>>> x.every(lambda v: v > 0)
False
>>> x.every(lambda v: isinstance(v, int))
True
>>> x.for_each(print)
1
-3
10
5
>>> y = ESArray([[3, 4], [5], 6, [7, [8, [9, 10]]]])
>>> y.flatten()
[3, 4, 5, 6, 7, 8, 9, 10]
```

## Problem 2

In this problem, we're going to continue exploring [open data](https://data.cityofchicago.org) from the City of Chicago, except this time we're going to take advantage of object-oriented programming to build the foundation for a hypothetical "Chicago Public Schools application". We have provided you with a CSV file with data on each public school in Chicago including its name, location, address, what grades are taught, and what network it is part of. You are asked to write three classes that will allow a user to easily interact with this data.

### Specifications

The specifications below indicate what classes/methods/functions must be implemented to receive full credit. However, you should feel free to implement helper methods/functions if you find doing so to be useful.

#### School Class

- Write a class named `School`, each instance of which represents a single public school in Chicago.
- The `__init__(self, data)` method should receive a dictionary corresponding to a row in the CSV file (see suggested CSV reading code in [CPS Class](#cps-class)). In its body, it should create the following attributes:

  - `self.id` -- the unique ID of the school (`School_ID` column) stored as an int
  - `self.name` -- short name of the school (`Short_Name` column)
  - `self.network` -- the network the school is in (`Network` column)
  - `self.address` -- street address of the school
  - `self.zip` -- the ZIP code of the school
  - `self.phone` -- the phone number of the school
  - `self.grades` -- a list of grades taught at the school (must be an actual `list`, not just the string that appears in the CSV)
  - `self.location` -- the location of the school as an instance of
    `Coordinate` (see specifications in [Coordinate Class](#coordinate-class))

- The `open_website(self)` method should open a website showing information about the school using the [webbrowser.open_new_tab()](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new_tab) function from the standard library. The URL you can use for this is `http://schoolinfo.cps.edu/schoolprofile/SchoolDetails.aspx?SchoolId=<id>` where `<id>` is the unique ID of the school as listed in the spreadsheet.
- The `distance(self, coord)` method should accept an instance of `Coordinate` and return the distance in miles "as the crow flies" from the specified location to the school. See the [description below](#calculating-distance-between-points) for how to calculate distances using latitudes/longitudes.
- The `full_address(self)` method should return a multi-line string (that is, a string with a newline character within it) with the street address, city, state, and ZIP code of the school.

#### Coordinate Class

- The `Coordinate` class stores a latitude/longitude pair indicating a physical location on Earth.
- The `__init__(self, latitude, longitude)` method should accept two floats that represent the latitude and longitude in radians.
- `Coordinate.fromdegrees(cls, latitude, longitude)` should be a `@classmethod` that accepts two floats representing the latitude and longitude in degrees and returns an instance of `Coordinate`.
- The `distance(self, coord)` method should accept another instance of `Coordinate` and calculate the distance in miles to it from the current instance.
- The `as_degrees(self)` method should return a tuple of the latitude and longitude in degrees.
- The `show_map(self)` method should open up Google Maps on a web browser with a point placed on the latitude/longitude. The URL you can use for this is `http://maps.google.com/maps?q=<latitude>,<longitude>` where `<latitude>` and `<longitude>` have been replaced by the corresponding decimal degrees.

#### CPS Class

- The `CPS` class stores a list of public schools in the city.
- The `__init__(self, filename)` method accepts a filename for the CSV file in which our school data is stored. It should create an attribute called `schools` that is a list of `School` instances. To iterate over the rows in the CSV file, you can use the following code:

```python
import csv

with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ...
```

- The `nearby_schools(self, coord, radius=1.0)` method accepts an instance of `Coordinate` and returns a list of `School` instances that are within `radius` miles of the given coordinate.
- The `get_schools_by_grade(self, *grades)` method accepts one or more grades as strings ('K', '3', etc.) and returns a list of `School` instances that teach all of the given grades.
- The `get_schools_by_network(self, network)` method accepts the network name as a string (e.g., 'Charter') and returns a list of `School` instances in that network.

#### Calculating distance between points

Since the school locations are given as latitude/longitude coordinates, we need a way to calculate distance given two such pairs. One recommended way to do this is using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula), which is

<img src="http://latex2png.com/output//latex_864209a59a6d48323e698d6899ee6f06.png" width="600px" />

where `d` is the distance between the two points, `r` is the radius of the Earth (use 3961 miles), <img src="http://latex2png.com/output//latex_a4acc5e8a6c299501f90c28a2ddee69a.png" width="20px" /> and <img src="http://latex2png.com/output//latex_7256d5a2af8a38823209a802a4b923ab.png" width="20px" /> are the latitudes of the two points in radians, and <img src="http://latex2png.com/output//latex_3b3fb8151d8990dfafdc7954410136ff.png" width="15px" /> and <img src="http://latex2png.com/output//latex_e3ca12d2ef3a5f3b30188840c05480c7.png" width="15px" /> are the longitudes of the two points in radians. Note that the data you are given is in degrees, not radians, so make sure you [convert it](https://en.wikipedia.org/wiki/Radian#Conversion_between_radians_and_degrees) first.

### Example Interaction

The example below shows an example interaction with these classes at a Python console. Note that for this example, I've implemented a [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__) method in the `School` and `Coordinate` classes to get a nice string representation (we will discuss this further in week 5); feel free to do the same if you wish.

```pycon
>>> cps = CPS('libraries.csv')
>>> cps.schools[:5]
[School(GLOBAL CITIZENSHIP),
 School(ACE TECH HS),
 School(LOCKE A),
 School(ASPIRA - EARLY COLLEGE HS),
 School(ASPIRA - HAUGAN)]
>>> [s for s in cps.schools if s.name.startswith('OR')]
[School(ORTIZ DE DOMINGUEZ),
 School(ORIOLE PARK),
 School(OROZCO),
 School(ORR HS)]
>>> ace_tech = cps.schools[1]
>>> ace_tech.location
Coordinate(41.7961215104, -87.6258490365)
>>> print(ace_tech.full_address())
5410 S STATE ST
Chicago, IL 60609
>>> the_bean = Coordinate.fromdegrees(41.8821512, -87.6246838)
>>> cps.nearby_schools(the_bean, radius=0.5)
[School(NOBLE - MUCHIN HS),
 School(YCCS - INNOVATIONS)]
>>> cps.get_schools_by_grade('PK', '12')
[School(FARRAGUT HS)]
>>> cps.get_schools_by_network('Contract')
[School(CHIARTS HS),
 School(HOPE INSTITUTE),
 School(PLATO),
 School(CHICAGO TECH HS)]
```
