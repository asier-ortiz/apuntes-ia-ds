class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass


print("child hereda de la clase Child", issubclass(Child, Child))
print("child hereda de la clase Mother", issubclass(Child, Mother))
print("child hereda de la clase Father", issubclass(Child, Father))

# al reves NO

print("mother hereda de la clase Child", issubclass(Mother, Child))
print("father hereda de la clase Child", issubclass(Father, Child))

if issubclass(Child, Child):
    pass
elif issubclass(Child, Mother):
    pass
