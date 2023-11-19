"""
URL     :https://adventofcode.com/2022/day/2
Author  :benni347:
"""


def read_file():
    """
    This reads the file.
    :return: a list of all ints in the given file.
    """
    # filename: str = "input-test"
    filename: str = "input"

    local_content = []
    with open(filename, encoding="UTF-8") as file:
        for line in file:
            local_content.append(str(line.strip("\n")))
        file.close()

    return local_content


def find_common(rucksack_param):
    """
    THis checks the list to find the biggest.
    :type rucksack_param: list
    :param rucksack_param: a list where every item in the rucksack is in.
    :return: a list with every common char in.
    """
    common = []
    first_part = ""
    second_part = ""

    for _, data in enumerate(rucksack_param):
        len_of_data = len(data)
        first_part = data[:int(len_of_data / 2)]  # Same len as second_part
        second_part = data[int(len_of_data / 2):]  # Same len as first_part
        current_len_of_common = len(common)
        for _, data_first_part in enumerate(first_part):
            for _, data_second_part in enumerate(second_part):
                # print(f"first_part = {data_first_part}\nsecond_part = {data_second_part}")
                if data_first_part == data_second_part:
                    common.append(data_first_part)
                    print(common)
                if current_len_of_common != len(common):
                    break
            if current_len_of_common != len(common):
                break

    return common


def value_common(common_characters):
    # a-z lowercase have values from 1-26
    # A-Z uppercase have values from 27-52
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_value = 0
    for _, data in enumerate(common_characters):
        total_value += alphabet.rfind(data) + 1
    return total_value


if __name__ == "__main__":
    content = read_file()
    common_characters = find_common(content)
    # print(common_characters)
    value_of_common_characters = value_common(common_characters)
    print(value_of_common_characters)
