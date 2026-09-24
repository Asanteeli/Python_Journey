"""
Author: Elijah ASante
Purpose: Water Pressure Dispenser
"""

inner_diameter1 = 0.28687 # (meters)  11.294 inches
friction_factor1 = 0.013  # (unitless)
s_velocity = 1.65               # (meters / second)
inner_diameter2 = 0.048692 # (meters)  1.917 inches
friction_factor2 = 0.018   # (unitless)
H_Hold_Velocity = 1.75            # (meters / second)
H2O_Density=998.2                  # density of water (998.2 kilogram / meter^3)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))


    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = inner_diameter1
    friction = friction_factor1
    velocity = s_velocity
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
    velocity, reynolds, inner_diameter2)
    pressure += loss
    diameter = inner_diameter2
    friction = friction_factor2
    velocity = H_Hold_Velocity
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")

# Formular to calculate Water Column Height
def water_column_height(tower_height, tank_height):
    """
    The following formula details will be used to calculate the function's return value.
    h - is height of the water column
    t - is the height of the tower (tower_height)
    w - is the height of the walls of the tank that is on top of the tower (tank_height)
    """

    result = tower_height + (3 * tank_height) / 4
    return result

# Function to calculate Pressure gain from height
def pressure_gain_from_water_height(height):
    """
    Pressure gain from height
    The following formula details will be used to calculate 
    the function's return value.

    P - is the pressure in kilopascals
    ρ - is the density of water 998.2 (kilogram / meter3)
    g - is the acceleration from Earths gravity 9.80665 (meter / second2)
    h - is the height of the water column inmeters (height)
    """
    result_2 = (H2O_Density * 9.80665 * height()) / 1000
    return result_2

# Function to Calculate pressure loss from pipes
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    The following details is used to calculate the function's return value.

    P is the lost pressure in kilopascals
    f is the pipe’s friction factor (friction_factor)
    L is the length of the pipe in meters (pipe_length)
    ρ is the density of water 998.2 (kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
    d is the diameter of the pipe in meters (pipe_diameter)
    """
    result_3 = (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)    
    return result_3

# Function to Calculate the Pressure loss from fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    
    The following formula details is to calculate the function's return value.
    P is the lost pressure in kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
    n is the quantity of fittings (quantity_fittings)
    """
    result_4 = (-0.04 * H2O_Density * (fluid_velocity * 2) * quantity_fittings) / 2000

    return result_4

# Function to calculate Reynolds Number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Use the following formula details to calculate the function's return value.
    R is the Reynolds number
    ρ is the density of water (998.2 kilogram / meter3)
    d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter. (hydraulic_diameter)
    v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
    μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    """
    result_5 = H2O_Density * hydraulic_diameter * fluid_velocity

    return result_5
# This function calculates Pressure loss from pipe reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    result_6 = (0.1 + (50/reynolds_number) * ((larger_diameter / smaller_diameter) ** 4) - 1)
    result_7 = (- result_6 * 998.2 * (fluid_velocity ** 2)) / 2000
    return result_7

main()