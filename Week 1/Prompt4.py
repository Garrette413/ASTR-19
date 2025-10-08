
class FavoriteAnimal:
    def __init__ (self, arm, leg, eye, tail, furry): #similar to java however an init func is needed to declare class parameters rather that js simply having it next to the class
        
        self.arm = arm
        self.leg = leg          # these are for initializing the instance values by using parameters. Basically allows
        self.eye = eye          # me to set values for these class variables later on
        self.tail = tail        
        self.furry = furry       # class parameters take in values, and then class variables(to the left) configure and become these values

    def Print(self):
        
        print("Arm length is " + str(self.arm) + " ft.")
        print("Leg length is " + str(self.leg) + " ft.")
        print("Eye count is " + str(self.eye) + ".")    #by putting self it knows to find these values in its self since itself has access to these values
        print("Tail? " + str(self.tail))
        print("Furry? " + str(self.furry))
        

Dog = FavoriteAnimal(1.2, 1.2, 2, True, True)

Dog.Print()



    