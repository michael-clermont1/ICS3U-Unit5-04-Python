#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: May 2022
# This program uses user defined functions

import math


def volume_of_cylinder(height, radius):
    # calculate volume

    volume = math.pi * (radius**2) * height

    return volume


def main():
    # this function gets the height and radius

    # input
    height_as_string = input("Enter the height of the cylinder(mm): ")
    radius_as_string = input("Enter the radius of the cylinder(mm): ")
    print("")

    try:
        height_as_float = float(height_as_string)
        radius_as_float = float(radius_as_string)
        # call functions
        calculated_volume = volume_of_cylinder(height_as_float, radius_as_float)
        print(
            "The volume of this cylinder with the radius of {0} mm and height of {1} mm is {2} mm².".format(
                radius_as_float, height_as_float, calculated_volume
            )
        )
    except Exception:
        print("That is not an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
