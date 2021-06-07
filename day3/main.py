from typing import List
from math import prod


def read_txt(path: str) -> List[str]:
    with open(path, "r") as f:
        raw = f.read()

    return raw.split("\n")[:-1]


def q1(lines: List[str], right: int, down: int) -> int:
    modulo = len(lines[0])
    start = 0
    count = 0
    for i_line in range(0, len(lines), down):
        line = lines[i_line]
        start = start % modulo
        if line[start] == "#":
            count += 1
        start += right
    return count


if __name__ == "__main__":
    lines = read_txt("input.txt")

    q1_answer = q1(lines, right=3, down=1)
    print(q1_answer)

    q2_answer = prod([
        q1(lines, 1, 1),
        q1(lines, 3, 1),
        q1(lines, 5, 1),
        q1(lines, 7, 1),
        q1(lines, 1, 2),
    ])
    print(q2_answer)
