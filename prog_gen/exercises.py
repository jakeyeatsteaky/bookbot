from enum import Enum, auto

class Exercise(Enum):
    BackSquat = auto()
    Snatch = auto()
    Jerk = auto()
    BenchPress = auto()
    DumbellPress = auto()
    Pullup = auto()

member_names = []

for sets in range(1, 7):
    for reps in range(12, 0, -1):
        member_names.append(f"S{sets}_R{reps}")

Scheme = Enum("Scheme", member_names)

def test():
    count = 1
    for scheme in Scheme:
        if (count == 32):
            print(scheme)
        count += 1
    for e in Exercise:
        print(e)

if __name__ == "__main__":
    test()
