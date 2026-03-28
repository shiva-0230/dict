std={"name":"siva",
    "age":20,
    "course":"B.TECH"}
print(std.keys())
print(std.values())
print(std.items())
std.pop("age")
print(std)
del std["course"]
print("after delet",std)
