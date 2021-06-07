from typing import List, Tuple


def read_txt(path: str) -> List[str]:
    with open(path, "r") as f:
        raw = f.read()

    return raw.split("\n")[:-1]


def parse_line(line: str) -> Tuple[int, int, str, str]:
    nums_part, char_part, password = tuple(line.split(" "))
    num1, num2 = tuple(nums_part.split("-"))
    char = char_part[0]
    return int(num1), int(num2), char, password


def check_password_q1(minn: int, maxx: int, char: str, password: str) -> bool:
    return minn <= password.count(char) <= maxx


def check_password_q2(pos1: int, pos2: int, char: str, password: str) -> bool:
    return (password[pos1-1] == char) + (password[pos2-1] == char) == 1


if __name__ == "__main__":
    lines = read_txt("input.txt")

    q1_answer = sum([check_password_q1(*parse_line(line)) for line in lines])
    print(q1_answer)

    q2_answer = sum([check_password_q2(*parse_line(line)) for line in lines])
    print(q2_answer)
