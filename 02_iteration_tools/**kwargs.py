def print_kwargs(**kwargs):
  for key , value in kwargs.items():
    print(f"{key} : {value}")

print_kwargs(power = "pig" , name="suar")
print_kwargs(power = "pig2" , name="suar2" , enemy = "dog")