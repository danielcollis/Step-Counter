def steps_to_miles(steps):
    if (steps < 0):
        raise ValueError ('Exception: Negative step count entered.')
    miles = steps / 2000
    return miles


steps = int(input('Enter number of steps: '))
try:
    miles = steps_to_miles(steps)
    print(f'{miles:.2f}')
except ValueError as excpt:
    print(excpt)