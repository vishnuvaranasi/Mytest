x = ["a", "b", "c"] 
y = x
y[1] = "z"
print(y)
print(x)
print("\n")
x = ["a", "b", "c"]
y = list(x)
y[1] = "z"
print(y)
print(x)
print("\n")
x = ["a", "b", "c"]
y = x[:]
y[1] = "z"
print(y)
print(x)

