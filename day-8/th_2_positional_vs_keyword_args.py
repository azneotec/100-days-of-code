# Functions with more than 1 input
def greet_with(name: str, location: str) -> None:
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Azad", "Singapore")
greet_with("Singapore", "Ruhan")  # Positional Arguments
greet_with(location="Singapore", name="Ruhan")  # Keyword Arguments
