class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"Cat's name is {self.name}"
            f"Cat's age is {self.age}"
        )


Tina = Cat("Tina", 1)
print(Tina)

