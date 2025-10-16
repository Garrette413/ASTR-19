#create a class about my favorite planet

class Planet:
    def __init__(self, name, temp, num_moons, rings):
        self.name = name
        self.temp = temp
        self.num_moons = num_moons
        self.rings = rings


    def describe(self):
        print(f"Planet Name: {self.name}")
        print(f"Avg Temp: {self.temp}")
        print(f"Number of moons: {self.num_moons}")
        print(f"Rings {self.rings}")
    
def main():
    Saturn = Planet("Saturn", "100K", 2, True)
    
    Saturn.describe()

if __name__ == "__main__":
        main()

