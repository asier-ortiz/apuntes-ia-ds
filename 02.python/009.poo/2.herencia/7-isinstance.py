class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass

child = Child()
mother = Mother()
father = Father()

print("child hereda de la clase Child", isinstance(child, Child))
print("child hereda de la clase Mother", isinstance(child, Mother))
print("child hereda de la clase Father", isinstance(child, Father))

# al reves NO

print("mother hereda de la clase Child", isinstance(mother, Child))
print("father hereda de la clase Child", isinstance(father, Child))

if isinstance(child, Child):
    pass
elif isinstance(child, Mother):
    pass
