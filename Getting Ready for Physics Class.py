  # Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8


# Write your code below:
  
f_temp = 100
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)

c_temp = f_to_c(100)
print(c_temp)

def c_to_f(c_temp):
  f_temp = (c_temp * (9/5) + 32)
  return f_temp 
c0_in_fahrenheit = c_to_f(0)


def get_force(train_mass,train_acceleration):
  return train_mass * train_acceleration
train_force = (get_force(train_mass, train_acceleration))
print(train_force)

print("The GE train supplies",train_force, "Newtons of force")

def get_energy(bomb_mass, c):
  return (bomb_mass * c**2)
bomb_energy = (get_energy(bomb_mass, c))



print("A 1kg bomb supplies", bomb_energy, "Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(train_mass, acceleration)
  force = get_force(train_mass, train_acceleration)
  return force * distance
get_force(train_mass, train_acceleration)

train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does ",train_work, "Joules of work over ", train_distance , "meters" )


 






