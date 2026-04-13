# Uncomment this when you reach the "Use the Force" section
# train_mass = 22680
# train_acceleration = 10
# train_distance = 100
# bomb_mass = 1
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 
#task 1 F to C

def f_to_c(f_temp):
    return (f_temp - 32) * 5/9

# Task 2: test f to c with 100F
f100_in_celsius = f_to_c(100)

# Task 3: c_to_f

def c_to_f(c_temp):
    return c_temp * (9/5) + 32

# Task 4: test c_to_f with 0C
c0_in_fahrenheit = c_to_f(0)

# Task 5: get_force

def get_force(mass, acceleration):
    return mass * acceleration

# Task 6: test get_force
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Task 7: print force message
print(f"The GE train supplies {train_force} Newtons of force.")

# Task 8: get_energy

def get_energy(mass, c=3*10**8):
    return mass * (c**2)

# Task 9: test get_energy on bomb_mass
bomb_energy = get_energy(bomb_mass)

# Task 10: print energy message
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Task 11: get_work

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Task 12: test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)

# Task 13: print work message
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
