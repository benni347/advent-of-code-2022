"""
URL     :https://adventofcode.com/2022/day/1
Author  :benni347:
"""


def read_file():
    """
    This reads the file.
    :return: a list of all ints in the given file.
    """
    filename: str = "input"
    local_content = []
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            local_content.append(str(line.strip("\n")))
        file.close()

    return local_content


def check(calorie_param):
    """
    THis checks the list to find the biggest.
    :type calorie_param: list
    :param calorie_param: a list where every calorie is in
    :return: the most calories
    """
    current_elf = 0
    current_highest = 0
    for i, calorie_data in enumerate(calorie_param):
        if calorie_data in ("\n", ""):
            i += 1
            current_highest = max(current_highest, current_elf)
            current_elf = 0
        else:
            current_elf += int(calorie_data)
    return current_highest


if __name__ == "__main__":
    content = read_file()
    part_1 = check(content)
    print(part_1)
