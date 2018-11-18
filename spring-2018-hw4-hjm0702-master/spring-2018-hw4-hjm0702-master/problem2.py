import csv
import webbrowser
import math

class School:
    city = "Chicago"
    state = "IL"

    def __init__(self,id,name,network,address,zip,phone,grade,location):
        self.id = id
        self.name = name
        self.network = network
        self.address = address
        self.zip = zip
        self.phone = phone
        self.grades = grade
        self.location = location
        self.latitude = location.latitude
        self.longitude = location.longitude

    def open_website(self):
        return webbrowser.open_new_tab(f'http://schoolinfo.cps.edu/schoolprofile/SchoolDetails.aspx?SchoolId={self.id}')

    def distance(self, coord):
        '''return distance in miles'''
        Radius_Earth = 3961
        dif_latitude = self.location.latitude-coord.latitude
        dif_longitude = self.location.longitude-coord.longitude
        return 2*Radius_Earth*math.asin(math.sqrt((math.sin(dif_latitude/2))**2+math.cos(self.latitude)*math.cos(coord.latitude)*((math.sin(dif_longitude/2))**2)))

    def full_address(self):
        '''a multi-line string
         (that is, a string with a newline character within it)
         with the street address, city, state, and ZIP code of the school.'''
        return f'{self.address}\n{School.city}, {School.state} {self.zip}'

    def __repr__(self):
        return f'{self.id, self.name}'

class Coordinate:
    def __init__(self, latitude, longitude):
        '''Accept two floats'''
        self.latitude = float(latitude)*math.pi/180
        self.longitude = float(longitude)*math.pi/180

    @classmethod
    def fromdegrees(cls, latitude, longitude):
        '''return instance of Coordinate'''
        return Coordinate(latitude, longitude)

    def distance(self, coord):
        '''calculate a distance from accpeted instance to the current instance'''
        Radius_Earth = 3961
        dif_latitude = self.latitude-coord.latitude
        dif_longitude = self.longitude-coord.longitude
        return 2*Radius_Earth*math.asin(math.sqrt((math.sin(dif_latitude/2))**2+math.cos(self.latitude)*math.cos(coord.latitude)*((math.sin(dif_longitude/2))**2)))

    def as_degrees(self):
        '''return a tuple of the latitude and longitude in degrees'''
        return self.latitude*180/math.pi, self.longitude*180/math.pi

    def show_map(self):
        '''http://maps.google.com/maps?q=<latitude>,<longitude>'''
        return webbrowser.open_new_tab(f'http://maps.google.com/maps?q={self.latitude*180/math.pi},{self.longitude*180/math.pi}')

    def __repr__(self):
        return f'{self.latitude*180/math.pi, self.longitude*180/math.pi}'

class CPS:
    def __init__(self, filename):
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            self.school = [School(row['School_ID'],row['Short_Name'],row['Network'],row['Address'],
            row['Zip'],row['Phone'],row['Grades'].replace(" ","").split(","), Coordinate(row['Lat'], row["Long"])) for row in reader]

    def nearby_schools(self, coord, radius=1.0):
        ''' accepts an instance of Coordinate and
        returns a list of School instances that are within
        radius miles of the given coordinate.'''
        nearby = [i for i in self.school if i.distance(coord) <= radius]
        return nearby

    def get_schools_by_grades(self, *grades):
        '''accepts one or more grades as strings
        ('K', '3', etc.) and returns a list of School instances
         that teach all of the given grades.'''
        gradelist = [i for i in grades]
        schoollist = []
        for j in self.school:
            checker = True
            for i in gradelist:
                if i not in j.grades:
                    checker = False
            if checker == True:
                schoollist.append(j)
        return schoollist

    def get_schools_by_networks(self, network):
        '''accepts the network name as a string (e.g., 'Charter')
        and returns a list of School instances in that network'''
        net_schoollist = [j for j in self.school if j.network == network]
        return net_schoollist

if __name__ == "__main__":

    cps = CPS("schools.csv")
    print(cps.school[:5])
    print([s for s in cps.school if s.name.startswith('OR')])
    ace = cps.school[1]
    ace.open_website()
    print(ace.full_address())
    the_bean = Coordinate.fromdegrees(41.8821512, -87.6246838)
    print(ace.distance(the_bean))
    print(the_bean.as_degrees())
    print(cps.nearby_schools(the_bean, radius = 0.5))
    the_bean.show_map()
    print(cps.get_schools_by_grades('12', '9', 'K'))
    print(cps.get_schools_by_networks('Contract'))
    hi = Coordinate(41, -87)
    print(hi.distance(the_bean))
