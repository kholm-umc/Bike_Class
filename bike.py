# Ken Holm
# Purpose:  The Bike class
# Class declaration


class Bike:
    # Private properties
    __numberOfGears = 1
    __currentGear = 3
    __numberOfWheels = 3
    __brakeType = "hand"

    # Class instantiator
    def __init__(self, numberOfGears=1, numberOfWheels=2, brakeType="hand"):
        # Set all our properties
        self.setNumberOfGears(numberOfGears)
        self.setNumberOfWheels(numberOfWheels)
        self.setBrakeType(brakeType)

        self.setCurrentGear(1)

    # Getter for the __numberOfGears property
    def getNumberOfGears(self):
        return (self.__numberOfGears)

    # Setter for the __numberOfGears property
    #  Valid values are integers from 1 to 15
    def setNumberOfGears(self, numberOfGears):
        try:
            # Is the argument an integer?
            if int(numberOfGears):
                pass

        except Exception as e:
            raise TypeError(f"{numberOfGears} is not an integer")

        # It is an integer, is it between 1 and 15?
        if numberOfGears > 0 and numberOfGears < 16:
            self.__numberOfGears = numberOfGears
        else:
            raise ValueError(f"{numberOfGears} is not between 1 and 15")

    # Getter for the __currentGear property
    def getCurrentGear(self):
        return (self.__currentGear)

    # Setter for the __currentGear property
    #  Valid values are integers from 1 to 15
    def setCurrentGear(self, currentGear):
        try:
            # Is the argument an integer?
            if int(currentGear):
                pass

        except Exception as e:
            raise TypeError(f"{currentGear} is not an integer")

        # It is an integer, is it between 1 and self.__numberOfGears?
        if currentGear > 0 and currentGear <= self.__numberOfGears:
            self.__currentGear = currentGear
        else:
            raise ValueError(f"{currentGear} is not between 1 and {self.__numberOfGears}")

    # Getter for the __numberOfWheels property
    def getNumberOfWheels(self):
        return (self.__numberOfWheels)

    # Setter for the __numberOfWheels property
    #  Valid values are integers from 1 to 4
    def setNumberOfWheels(self, numberOfWheels):
        try:
            # Is the argument an integer?
            if int(numberOfWheels):
                pass

        except Exception as e:
            raise TypeError(f"{numberOfWheels} is not an integer")

        # It is an integer, is it between 1 and 4?
        if numberOfWheels > 0 and numberOfWheels <= 5:
            self.__numberOfWheels = numberOfWheels
        else:
            raise ValueError(f"{numberOfWheels} is not between 1 and 4")

    # Getter for the __brakeType property
    def getBrakeType(self):
        return (self.__brakeType)

    # Setter for the __brakeType property
    #  Valid values are integers from 1 to 15
    def setBrakeType(self, brakeType):
        try:
            # Is the argument an integer?
            if str(brakeType):
                pass

        except Exception as e:
            raise TypeError(f"{brakeType} is not an string")

        # It is a string, is it either "hand" or "foot"?
        if brakeType == "hand" or brakeType == "foot":
            self.__brakeType = brakeType
        else:
            raise ValueError(f"{brakeType} is not either 'hand' or 'foot'")

    # Increase the gear
    #  Do not allow gear to be over the __numberOfGears
    def increaseGear(self):
        if self.getCurrentGear() < self.__numberOfGears:
            self.setCurrentGear(self.getCurrentGear() + 1)

    # Decrease the gear
    #  Do not allow gear to be below 1
    def decreaseGear(self):
        if self.getCurrentGear() > 1:
            self.setCurrentGear(self.getCurrentGear() - 1)
