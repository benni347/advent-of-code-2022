"""
URL     :https://adventofcode.com/2022/day/2
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


def check(rock_paper_sciccors_param):
    """
    THis checks the list to find the biggest.
    :type rock_paper_sciccors_param: list
    :param rock_paper_sciccors_param: a list where every calorie is in
    :return: the most calories
    """
    score = 0
    loose_worth = 0
    draw_worth = 3
    win_worth = 6
    rock_worth = 1
    paper_worth = 2
    scissors_worth = 3
    for _, data in enumerate(rock_paper_sciccors_param):
        if data[0] == "A" and data[2] == "X":  # draw and one point for rock
            score += loose_worth + scissors_worth
        elif data[0] == "A" and data[2] == "Y":
            score += draw_worth + rock_worth
        elif data[0] == "A" and data[2] == "Z":
            score += win_worth + paper_worth
        elif data[0] == "B" and data[2] == "X":  # draw and one point for rock
            score += loose_worth + rock_worth
        elif data[0] == "B" and data[2] == "Y":
            score += draw_worth + paper_worth
        elif data[0] == "B" and data[2] == "Z":
            score += win_worth + scissors_worth
        elif data[0] == "C" and data[2] == "X":  # draw and one point for rock
            score += loose_worth + paper_worth
        elif data[0] == "C" and data[2] == "Y":
            score += draw_worth + scissors_worth
        elif data[0] == "C" and data[2] == "Z":
            score += win_worth + rock_worth
    return score


if __name__ == "__main__":
    content = read_file()
    part_1 = check(content)
    print(part_1)
