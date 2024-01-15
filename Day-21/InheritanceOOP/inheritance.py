def breath():
    print("Inhale, Exhale.")


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale , Exhale.")


def swim():
    print("Moving in water.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breath()
        print("doing this underwater.")

nemo = Fish()
nemo.breathe()
