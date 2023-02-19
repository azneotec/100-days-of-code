names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)