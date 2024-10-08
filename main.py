# Ken Holm
# Puropse: Demonstrate how to use a class
#  we created

from bike import Bike

try:

    # Instantiate our new Bike
    #  Number of gears: 12
    #  Number of gears: 2
    #  Brake type: hand
    myBike = Bike(12, 2, "hand")

    # Print our some bike info
    print("Our new bike")
    print(f"Gears: {myBike.getnumberofgears()}")
    print(f"Number of Wheels: {myBike.getnumberofwheels()}")
    print(f"Brake Type: {myBike.getbraketype()}")
    print(f"Current Gear: {myBike.getcurrentgear()}")
    input("Continue")
    print()

    # Set our current gear to 10
    print("Setting the current gear to 10")
    myBike.setcurrentgear(10)
    print(f"Current Gear: {myBike.getcurrentgear()}")
    input("Continue")
    print()

    # Increase the gear (to 11)
    print("Increasing the current gear")
    myBike.increasegear()
    print(f"Current Gear: {myBike.getcurrentgear()}")
    input("Continue")
    print()

    # Increase the gear, again (to the max: 12)
    print("Increasing the current gear, again")
    myBike.increasegear()
    print(f"Current Gear: {myBike.getcurrentgear()}")
    input("Continue")
    print()

    # Increase the gear, once more, past the max
    print("Trying to go past the max gear")
    myBike.increasegear()
    print(f"Current Gear: {myBike.getcurrentgear()}")
    print("NOTE: We do not allow that to happen")
    input("Continue")
    print()

    # Prepare to go below the minimum gear
    print("Resetting our gear to 2")
    myBike.setcurrentgear(2)
    print(f"Current Gear: {myBike.getcurrentgear()}")
    input("Continue")
    print()

    # Decrease the gear (to 1)
    print("Decreasing our current gear")
    myBike.decreasegear()
    print(f"Current Gear: {myBike.getcurrentgear()}")
    input("Continue")
    print()

    # Try to bypass the minimum gear
    print("Trying to decrease our current gear below 1")
    myBike.decreasegear()
    print(f"Current Gear: {myBike.getcurrentgear()}")
    print("NOTE: We do not allow that to happen")
    print()

    # Set the brake type to "electric"
    print("Trying to set the brake type to 'electric'")
    myBike.setbraketype("electric")
    print("NOTE: We do not allow that to happen")
    print()

except Exception as e:
    print(f"Error message: {e}")
