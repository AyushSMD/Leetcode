class boobs:
    def __init__(self, cup_size="D"):
        self.cup_size = cup_size

    def print_boob_size(self):
        print(f"boob size is: {self.cup_size}")

def main():
    boob1 = boobs()
    boob2 = boobs("Z")

    print(boob1.cup_size, boob2.cup_size)
    boob1.print_boob_size()


if __name__ == "__main__":
    main()
