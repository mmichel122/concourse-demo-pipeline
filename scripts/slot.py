import random


def display(word):
    version_num = random.randint(0, 500)
    final = f"{word}-{version_num}"
    return final


if __name__ == "__main__":
    wd = display("ModusMitch")
    print(wd)
