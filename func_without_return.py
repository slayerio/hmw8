# a
def ascending_my(a: int, b: int):
    if a > b:
        print(b, a)
    else:
        print(a, b)
# b
def my_details(a: str):
    print(a[0], a[int((len(a)-1)/2)], a[-1])
# c
def say_bool(a: bool = ""):
    print('yes' if a == True else 'no')
# 3c
def say_bool2(a: bool = "") -> str:
    print('yes' if a == True else 'no')
    return a
# d
def print_zugi(a: list[int]):
    for i in a:
        print('odd' if i % 2 else 'even', end=" ")
# 4d
def print_zugi2(a: list[int], b: list[str]) -> list[str]:
    for i in a:
        b.append('odd' if i % 2 else 'even')
    print(b)
    return b
def my_statistics(grades = list[int]):
    print(f"there were {len(grades)} grades")
    print(f"lowest score is {min(grades)}")
    print(f"highest score is {max(grades)}")
    print(f"avg of grades is {sum(grades) // len(grades)}")
    best = 0
    worst = 0
    for i in grades:
        if i > 90:
            best += 1
        elif i < 55:
            worst += 1
        else:
            continue
    print(f"there were {best} grades over 90, {worst} below 55")






