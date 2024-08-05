import func_without_return
func_without_return.ascending_my(-12, 7)
func_without_return.my_details("Ai is the best")
func_without_return.say_bool(True)
func_without_return.say_bool(False)
func_without_return.print_zugi([14, 14, 15, 10, 2, 3, 5,])
print()
# 3c
func_without_return.say_bool2(False)
# 4d
func_without_return.print_zugi2([14, 14, 15, 10, 2, 3, 5,], [])

grade = None
grades_lst: list[int] = []
while not grade:
    try:
        while True:
            grade = int(input("enter grade"))
            if grade == -99:
                break
            elif 0 <= grade <= 100:
                grades_lst.append(grade)
            else:
                continue
    except ValueError:
        print("enter a number")

func_without_return.my_statistics(grades_lst)


help(func_without_return.say_bool())
help(func_without_return.print_zugi())
help(func_without_return.ascending_my())
help(func_without_return.my_details())
help(func_without_return.my_statistics())