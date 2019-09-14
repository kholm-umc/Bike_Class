# Ken Holm
# Puropse: Demonstrate how to use a class
#  we created

from bike import Bike

try:

    # Instantiate our new Bike
    #  Number of gears: 12
    #  Number of gears: 2
    #  Brake type: hand
    b = Bike(12, 2, "hand")

    # Print our some bike info
    print("Our new bike")
    print(f"Gears: {b.getNumberOfGears()}")
    print(f"Number of Wheels: {b.getNumberOfWheels()}")
    print(f"Brake Type: {b.getBrakeType()}")
    print(f"Current Gear: {b.getCurrentGear()}")
    input("Continue")
    print()

    # Set our current gear to 10
    print("Setting the current gear to 10")
    b.setCurrentGear(10)
    print(f"Current Gear: {b.getCurrentGear()}")
    input("Continue")
    print()

    print("Increasing the current gear")
    b.increaseGear()
    print(f"Current Gear: {b.getCurrentGear()}")
    input("Continue")
    print()

    print("Increasing the current gear, again")
    b.increaseGear()
    print(f"Current Gear: {b.getCurrentGear()}")
    input("Continue")
    print()

    print("Trying to go past the max gear")
    b.increaseGear()
    print(f"Current Gear: {b.getCurrentGear()}")
    print("NOTE: We do not allow that to happen")
    input("Continue")
    print()

    print("Resetting our gear to 2")
    b.setCurrentGear(2)
    print(f"Current Gear: {b.getCurrentGear()}")
    input("Continue")
    print()

    print("Decreasing our current gear")
    b.decreaseGear()
    print(f"Current Gear: {b.getCurrentGear()}")
    input("Continue")
    print()

    print("Trying to decrease our current gear below 1")
    b.decreaseGear()
    print(f"Current Gear: {b.getCurrentGear()}")
    print("NOTE: We do not allow that to happen")
    print()

except Exception as e:
    print(f"Error message: {e}")
