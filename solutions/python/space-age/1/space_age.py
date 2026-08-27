class SpaceAge:
    def __init__(self, seconds):
        self.orbital_time = {"mercury" : 0.2408467,
                        "venus"	: 0.61519726,
                        "earth" : 1.0,
                        "mars": 1.8808158,
                        "jupiter":11.862615,
                        "saturn" :29.447498,
                        "uranus" :84.016846,
                        "neptune" :164.79132}
        self.seconds = seconds
        self.earth_second = 31557600.0
    def calculate_age(self,planet):
        earth_age = self.seconds/self.earth_second
        planet_age = earth_age/self.orbital_time[planet]
        return round(planet_age,2)
    def on_mercury(self):            
        return self.calculate_age('mercury')
    def on_venus(self):
        return self.calculate_age('venus')
    def on_earth(self):
        return self.calculate_age('earth')
    def on_mars(self):
         return self.calculate_age('mars')
    def on_jupiter(self):
         return self.calculate_age('jupiter')
    def on_saturn(self):
        return self.calculate_age('saturn')
    def on_uranus(self):
        return self.calculate_age('uranus')
    def on_neptune(self):
        return self.calculate_age('neptune')