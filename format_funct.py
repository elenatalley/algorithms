name = "Bob"
greeting = "Hello " + name

print(greeting)

# OR

name = "Ralf"
print(f"Hello, {name}")

# OR

longer_phrase = "hello {}. Today is {}."

formated = longer_phrase.format("Rolf", "Monday")
print(formated)