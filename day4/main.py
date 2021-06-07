from typing import Dict, List


def read_txt(path: str) -> List[str]:
    with open(path, "r") as f:
        raw = f.read()

    return raw.strip()


def split_passports(raw: str) -> List[str]:
    return raw.split("\n\n")


def check_passport(passport: str) -> bool:
    FIELDS = [
        "byr",
        "eyr",
        "iyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]

    return all([x in passport for x in FIELDS])


def parse_passport(passport: str) -> Dict[str, str]:
    passport = passport.replace("\n", " ")
    return dict([kv.split(":") for kv in passport.split(" ")])


def check_passport_2(passport: Dict[str, str]) -> bool:
    FIELDS = [
        "byr",
        "eyr",
        "iyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]

    if not all([f in passport for f in FIELDS]):
        return False

    if not passport["byr"].isnumeric():
        return False
    
    if not (1920 <= int(passport["byr"]) <= 2002):
        return False
    
    if not passport["iyr"].isnumeric():
        return False
    
    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False

    if not passport["eyr"].isnumeric():
        return False
    
    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False


if __name__ == "__main__":
    raw = read_txt("input.txt")
    passports = split_passports(raw)

    q1_answer = sum([check_passport(p) for p in passports])
    print(q1_answer)
