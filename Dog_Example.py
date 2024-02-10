class Dog:
    def __init__(self, name, breed, age, feed):
        self.name = name
        self.breed = breed
        self.age = age
        self.feed = feed
        
    def service_dog(self):
        print(f"{self.name}. is a service dog")
        
    def bark(self):
        print(f"{self.name}. says Woof!")
    
    def fast(self):
        print(f"{self.name} is one of the fastest dogs among my breeds")

# Instances
dog1 = Dog("Rex", "German Shepherd", 4, "fish filets")
dog2 = Dog("Oscar", "Golden Retriever", 3, "finger-links")
dog3 = Dog("Sparky", "Labrador", 4, "meat-stew")

# Activities
dog1.bark()
dog1.service_dog()
dog3.fast()
dog2.bark()

