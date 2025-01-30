class Holiday:
    def __init__(self, Destination, Days, Name):
        self.Destination = Destination
        self.Days = Days
        self.Name = Name
        self.Price = 55.00
    def CalculationCost(self):
        return self.Days * self.Price

    def DisplaySummary(self):
        print("Destination: " + self.Destination, "\nDays: " + self.Days, "\nName: " + self.Name, "\nPrice: " + str(self.CalculationCost()))

class Cruise(Holiday):
    def __init__(self, Destination, Days, Name, CabinType):
        super().__init__(Destination, Days, Name)
        self.CabinType = CabinType
        if CabinType == 'Standard':
            self.Price = 55.00
        elif CabinType == 'Premium':
            self.Price = 80.00
        elif CabinType == 'Premium +':
            self.Price = 105.00
    def CalculationCost(self):
        return self.Days * self.Price

    def DisplaySummary(self):
        print("Destination: " + self.Destination, "\nDays: " + str(self.Days), "\nName: " + self.Name, "\nPrice: " + str(self.CalculationCost()))

class CityTour(Holiday):
    def __init__(self, Destination, Days, Name, IncludesGuides):
        super().__init__(Destination, Days, Name)
        self.IncludesGuides = IncludesGuides
        if IncludesGuides:
            self.Price = 75.00
        elif not IncludesGuides:
            self.Price = 55.00

    def CalculationCost(self):
        return self.Days * self.Price

    def DisplaySummary(self):
        print("Destination: " + self.Destination, "\nDays: " + str(self.Days), "\nName: " + self.Name, "\nPrice: £" + str(self.CalculationCost()))

class AdventureTrek(Holiday):
    def __init__(self, Destination, Days, Name, Difficulty, Participants):
        super().__init__(Destination, Days, Name)
        self.Difficulty = Difficulty
        self.Participants = Participants
    def CalculationCost(self):
        self.Price = self.Participants * 12.50
    def DisplaySummary(self):
        print("Destination: " + self.Destination, "\nDays: " + str(self.Days), "\nName: " + self.Name, "\nDifficulty: " + self.Difficulty, "\nParticipants: " + str(self.Participants), "\nPrice: " + str(self.CalculationCost()))

destination = input("What is the destination you would like to go to? ")
days = int(input("How many days do you wish to travel? "))
name = input("What is your name? ")
while True:
    type = input("""What type of holiday would you like to have?
    a) Cruise Holiday
    b) City Tour Holiday
    c) Adventure Trek Holiday
    (input a, b or c) """).lower()
    holiday = None
    if type == "a":
        cabin = input("""What cabin would you like to use? 
    a) Standard
    b) Premium
    c) Premium +
    (input a, b or c) """).lower()
        while True:
            if cabin == "a":
                cabin = "Standard"
                break
            elif cabin == "b":
                cabin = "Premium"
                break
            elif cabin == "c":
                cabin = "Premium +"
                break
            else:
                continue
        holiday = Cruise(destination, days, name, cabin)
        break
    elif type == "b":
        guide = input("Would you like a guide? ").lower()
        holiday = CityTour(destination, days, name, guide)
        break
    elif type == "c":
        participants = input("How many participants would you like to have? ")
        while True:
            difficulty = input("""What difficulty would you like to have? 
a) Easy
b) Medium
c) Hard
(input a, b or c) """).lower()
            if difficulty == "a":
                difficulty = "Easy"
                break
            elif difficulty == "b":
                difficulty = "Medium"
                break
            elif difficulty == "c":
                difficulty = "Hard"
                break
            else:
                continue
        holiday = AdventureTrek(destination, days, name, participants, difficulty)
        break
    else:
        continue
holiday.DisplaySummary()

