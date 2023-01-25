import random
import th_1_random_mdl_my_module

# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.
random_integer = random.randint(1, 10)
print(random_integer)

print(th_1_random_mdl_my_module.pi)

# Returns the next random floating point number between [0.0 to 1.0) exclusive of 1.0
random_float = random.random()
print(random_float)

# 0.0000 .... 4.9999
random_float = random_float * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
