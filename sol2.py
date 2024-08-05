import func_with_return
avg1 = func_with_return.my_avg(3, 7)
print(f"the avg is {avg1}")

head1 = func_with_return.my_headline("python has concurred the world")
print(head1)

res_con = func_with_return.concat_list([1, 2], [3, 4, 5, 6],[7, 8, 9])
print(res_con)
print(f"there are {len(res_con)} numbers in the list")

help(func_with_return.my_avg(3, 7))
help(func_with_return.concat_list([1, 2], [3, 4, 5, 6],[7, 8, 9]))
help(func_with_return.my_headline("python has concurred the world"))

# 6
# because there will be no output without the (return), the output will be 'None'
# same with 'return none'- the output will be 'None'
# return - exits the function and the code proceeds to the next line
# break - exits the loop and the code proceeds to the next line

