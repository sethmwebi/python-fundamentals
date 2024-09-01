from typing import List, Tuple

famous_people: List[Tuple[str, int]] = [
    ("Joe Rogan", 56),
    ("Abigail Salome", 22),
    ("Barrack Obama", 52),
    ("Monica Lewinsky", 36),
    ("Lex Fridman", 41),
    ("Joe Diaz", 66),
    ("Donal Trump", 78),
    ("Benjamin Netanyahu", 63),
    ("George Soros", 91),
]


def sort_by_age(arr: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    return sorted(arr, key=lambda person: person[1])


print(sort_by_age(famous_people))
