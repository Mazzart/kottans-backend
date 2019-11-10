"""
Given a .txt file that has a list of a bunch of names, count how many
of each name there are in the file, and print out the results to the screen.
"""

names_count = {}

with open("namelist.txt", "r") as names:
    name = names.readline()
    while name:
        name = name.strip()
        if name in names_count:
            names_count[name] += 1
        else:
            names_count[name] = 1

        name = names.readline()


if __name__ == "__main__":
    for name in names_count:
        print(f"{name}: {names_count[name]}")
