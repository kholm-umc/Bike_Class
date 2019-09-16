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
    print(f"Gears: {b.getnumberofgears()}")
    print(f"Number of Wheels: {b.getnumberofwheels()}")
    print(f"Brake Type: {b.getbraketype()}")
    print(f"Current Gear: {b.getcurrentgear()}")
    input("Continue")
    print()

    # Set our current gear to 10
    print("Setting the current gear to 10")
    b.setcurrentgear(10)
    print(f"Current Gear: {b.getcurrentgear()}")
    input("Continue")
    print()

    print("Increasing the current gear")
    b.increasegear()
    print(f"Current Gear: {b.getcurrentgear()}")
    input("Continue")
    print()

    print("Increasing the current gear, again")
    b.increasegear()
    print(f"Current Gear: {b.getcurrentgear()}")
    input("Continue")
    print()

    print("Trying to go past the max gear")
    b.increasegear()
    print(f"Current Gear: {b.getcurrentgear()}")
    print("NOTE: We do not allow that to happen")
    input("Continue")
    print()

    print("Resetting our gear to 2")
    b.setcurrentgear(2)
    print(f"Current Gear: {b.getcurrentgear()}")
    input("Continue")
    print()

    print("Decreasing our current gear")
    b.decreasegear()
    print(f"Current Gear: {b.getcurrentgear()}")
    input("Continue")
    print()

    print("Trying to decrease our current gear below 1")
    b.decreasegear()
    print(f"Current Gear: {b.getcurrentgear()}")
    print("NOTE: We do not allow that to happen")
    print()

except Exception as e:
    print(f"Error message: {e}")
