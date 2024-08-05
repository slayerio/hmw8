def my_avg(a, b: int) -> float:
    return (a+b) / 2

def my_headline(c: str) -> str:
    c = c + "!"
    return c.upper()

def concat_list(lst1, lst2, lst3: list[int]) -> list[int]:
    lst1 = lst1 + lst2 + lst3
    return lst1
