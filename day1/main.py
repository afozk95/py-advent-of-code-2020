from typing import List, Optional, Tuple


def read_txt(path: str) -> List[int]:
    with open(path, "r") as f:
        raw = f.read()

    lines = raw.split("\n")
    numbers = [int(line) for line in lines if line.isnumeric()]
    return numbers


def find_pair(numbers: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    numbers_so_far = set()
    for n in numbers:
        if (target_sum - n) in numbers_so_far:
            return n, target_sum - n
        numbers_so_far.add(n)
    return None


def find_triple(numbers: List[int], target_sum: int) -> Optional[Tuple[int, int, int]]:
    for n in numbers:
        numbers.remove(n)
        pair = find_pair(numbers, target_sum=target_sum-n)
        if pair is not None:
            return n, *pair
    return None

if __name__ == "__main__":
    numbers = read_txt("input.txt")

    pair = find_pair(numbers, target_sum=2020)
    q1_answer = pair[0] * pair[1] if pair else None
    print(q1_answer)

    triple = find_triple(numbers, target_sum=2020)
    q2_answer = triple[0] * triple[1] * triple[2] if triple else None
    print(q2_answer)
