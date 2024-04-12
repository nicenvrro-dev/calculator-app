num = 4.21
num_list = [i for i in str(num)]

decimal_pos = num_list.index(".")
nums_after_decimal = num_list[decimal_pos+1:]
all_zeros_after_decimal = all(x == "0" for x in nums_after_decimal)

# if all_zeros_after_decimal:
# 	print(int(num))
# else:
# 	print(num)

print(3 + 1.5)