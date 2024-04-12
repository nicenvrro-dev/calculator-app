from tkinter import *
THEME_COLOR = "#202020"


# -------------------------------------------- OPERATION FUNCTIONS ----------------------------------------- #
def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	return n1 / n2


# -------------------------------------------- BUTTONS FUNCTIONS ------------------------------------------- #
def format_num(num):
	num_list = [i for i in str(num)]
	decimal_pos = num_list.index(".")
	nums_after_decimal = num_list[decimal_pos + 1:]
	all_zeros_after_decimal = all(x == "0" for x in nums_after_decimal)

	if all_zeros_after_decimal:
		return int(num)
	else:
		return float(num)


def add_num():
	global num1_as_str, num1_real_num, num2_real_num, operator, result
	num1_as_str.set(output.get())
	num1_real_num = format_num(float(num1_as_str.get()))

	operator = "+"
	output.delete(0, END)

	if num1_real_num is not None and num2_real_num is not None:
		equation.delete(0, END)
		equation.insert(END, f"{result} {operator} ")

	else:
		equation.insert(END, f" {num1_real_num} {operator} ")


def subtract_num():
	global num1_as_str, num1_real_num, num2_real_num, operator, result
	num1_as_str.set(output.get())
	num1_real_num = format_num(float(num1_as_str.get()))
	operator = "-"
	output.delete(0, END)

	if num1_real_num is not None and num2_real_num is not None:
		equation.delete(0, END)
		equation.insert(END, f"{result} {operator} ")

	else:
		equation.insert(END, f" {num1_real_num} {operator} ")


def multiply_num():
	global num1_as_str, num1_real_num, num2_real_num, operator, result
	num1_as_str.set(output.get())
	num1_real_num = format_num(float(num1_as_str.get()))
	operator = "*"
	output.delete(0, END)

	if num1_real_num is not None and num2_real_num is not None:
		equation.delete(0, END)
		equation.insert(END, f"{result} x ")

	else:
		equation.insert(END, f" {num1_real_num} x ")


def divide_num():
	global num1_as_str, num1_real_num, num2_real_num, operator, result
	num1_as_str.set(output.get())
	num1_real_num = format_num(float(num1_as_str.get()))
	operator = "/"
	output.delete(0, END)

	if num1_real_num is not None and num2_real_num is not None:
		equation.delete(0, END)
		equation.insert(END, f"{result} ÷ ")

	else:
		equation.insert(END, f" {num1_real_num} ÷ ")


def all_clear():
	global num1_real_num, num2_real_num, operator, result
	num1_real_num = None
	num2_real_num = None
	operator = ""
	result = None
	output.delete(0, END)
	equation.delete(0, END)

	# ENABLED ALL BUTTONS
	for button in calculator_buttons:
		button.config(state=NORMAL)


def calculation_result():
	global num2_as_str, num2_real_num, operator, result
	num2_as_str.set(output.get())
	num2_real_num = format_num(float(num2_as_str.get()))

	# Check ZeroDivisionError
	if operator == "/" and num2_real_num == 0:
		output.delete(0, END)
		error_msg = "Cannot divide by zero"
		output.insert(0, error_msg)

		# DISABLE ALL BUTTONS EXCEPT CLEAR BUTTON
		for button in calculator_buttons:
			if button["text"] != "C":
				button.config(state=DISABLED)

	else:
		calculate = operations[operator]
		result = calculate(num1_real_num, num2_real_num)
		output.delete(0, END)
		output.insert(0, result)

		equation.insert(END, f"{num2_real_num} =")


def backspace_handler():
    current_text = output.get()
    if current_text:
        output.delete(len(current_text) - 1, END)


# -------------------------------------------- OUTPUT ENTRY ------------------------------------------------ #
window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20, bg="#202020")

equation = Entry(font=("Arial", 15, "bold"), bg=THEME_COLOR, border=0, fg="#848484")
equation.grid(column=0, row=0, columnspan=4, pady=10, sticky="EW")

output = Entry(font=("Arial", 20, "bold"), bg=THEME_COLOR, border=0, fg="white")
output.grid(column=0, row=1, columnspan=4, pady=10, sticky="EW")

num1_as_str = StringVar()
num1_as_str.set(output.get())

num2_as_str = StringVar()
num2_as_str.set(output.get())

num1_real_num = None
num2_real_num = None
result = None

operator = ""

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# ---------------------------------------------- CALCULATOR UI SETUP -------------------------------------------- #
percent_img = PhotoImage(file="images/percent.png")
percent_button = Button(image=percent_img, border=0, highlightthickness=0, bg=THEME_COLOR)
percent_button.grid(column=0, row=2)

ce_img = PhotoImage(file="images/ce.png")
ce_button = Button(image=ce_img, border=0, highlightthickness=0, bg=THEME_COLOR)
ce_button.grid(column=1, row=2)

clear_img = PhotoImage(file="images/clear.png")
clear_button = Button(text="C", image=clear_img, border=0, highlightthickness=0, bg=THEME_COLOR)
clear_button.config(command=all_clear)
clear_button.grid(column=2, row=2)

back_img = PhotoImage(file="images/back.png")
back_button = Button(image=back_img, border=0, highlightthickness=0, bg=THEME_COLOR)
back_button.config(command=backspace_handler)
back_button.grid(column=3, row=2)

fraction_img = PhotoImage(file="images/1_x.png")
fraction_button = Button(image=fraction_img, border=0, highlightthickness=0, bg=THEME_COLOR)
fraction_button.grid(column=0, row=3)

squared_img = PhotoImage(file="images/squared.png")
squared_button = Button(image=squared_img, border=0, highlightthickness=0, bg=THEME_COLOR)
squared_button.grid(column=1, row=3)

root_img = PhotoImage(file="images/root.png")
root_button = Button(image=root_img, border=0, highlightthickness=0, bg=THEME_COLOR)
root_button.grid(column=2, row=3)

divide_img = PhotoImage(file="images/divide.png")
divide_button = Button(image=divide_img, border=0, highlightthickness=0, bg=THEME_COLOR)
divide_button.config(command=divide_num)
divide_button.grid(column=3, row=3)

num_7_img = PhotoImage(file="images/num_7.png")
num_7_button = Button(image=num_7_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_7_button.config(command=lambda: output.insert(END, "7"))
num_7_button.grid(column=0, row=4)

num_8_img = PhotoImage(file="images/num_8.png")
num_8_button = Button(image=num_8_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_8_button.config(command=lambda: output.insert(END, "8"))
num_8_button.grid(column=1, row=4)

num_9_img = PhotoImage(file="images/num_9.png")
num_9_button = Button(image=num_9_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_9_button.config(command=lambda: output.insert(END, "9"))
num_9_button.grid(column=2, row=4)

multiply_img = PhotoImage(file="images/multiply.png")
multiply_button = Button(image=multiply_img, border=0, highlightthickness=0, bg=THEME_COLOR)
multiply_button.config(command=multiply_num)
multiply_button.grid(column=3, row=4)

num_4_img = PhotoImage(file="images/num_4.png")
num_4_button = Button(image=num_4_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_4_button.config(command=lambda: output.insert(END, "4"))
num_4_button.grid(column=0, row=5)

num_5_img = PhotoImage(file="images/num_5.png")
num_5_button = Button(image=num_5_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_5_button.config(command=lambda: output.insert(END, "5"))
num_5_button.grid(column=1, row=5)

num_6_img = PhotoImage(file="images/num_6.png")
num_6_button = Button(image=num_6_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_6_button.config(command=lambda: output.insert(END, "6"))
num_6_button.grid(column=2, row=5)

subtract_img = PhotoImage(file="images/minus.png")
subtract_button = Button(image=subtract_img, border=0, highlightthickness=0, bg=THEME_COLOR)
subtract_button.config(command=subtract_num)
subtract_button.grid(column=3, row=5)

num_1_img = PhotoImage(file="images/num_1.png")
num_1_button = Button(image=num_1_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_1_button.config(command=lambda: output.insert(END, "1"))
num_1_button.grid(column=0, row=6)

num_2_img = PhotoImage(file="images/num_2.png")
num_2_button = Button(image=num_2_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_2_button.config(command=lambda: output.insert(END, "2"))
num_2_button.grid(column=1, row=6)

num_3_img = PhotoImage(file="images/num_3.png")
num_3_button = Button(image=num_3_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_3_button.config(command=lambda: output.insert(END, "3"))
num_3_button.grid(column=2, row=6)

add_img = PhotoImage(file="images/add.png")
add_button = Button(image=add_img, border=0, highlightthickness=0, bg=THEME_COLOR)
add_button.config(command=add_num)
add_button.grid(column=3, row=6)

plus_minus_img = PhotoImage(file="images/plus_minus.png")
plus_minus_button = Button(image=plus_minus_img, border=0, highlightthickness=0, bg=THEME_COLOR)
plus_minus_button.grid(column=0, row=7)

num_0_img = PhotoImage(file="images/num_0.png")
num_0_button = Button(image=num_0_img, border=0, highlightthickness=0, bg=THEME_COLOR)
num_0_button.config(command=lambda: output.insert(END, "0"))
num_0_button.grid(column=1, row=7)

decimal_img = PhotoImage(file="images/decimal.png")
decimal_button = Button(image=decimal_img, border=0, highlightthickness=0, bg=THEME_COLOR)
decimal_button.config(command=lambda: output.insert(END, "."))
decimal_button.grid(column=2, row=7)

equal_img = PhotoImage(file="images/equals.png")
equal_button = Button(image=equal_img, border=0, highlightthickness=0, bg=THEME_COLOR)
equal_button.config(command=calculation_result)
equal_button.grid(column=3, row=7)

# -------------------------------------------- LIST OF ALL BUTTONS ------------------------------------------------ #
calculator_buttons = [
	percent_button,
	ce_button,
	clear_button,
	back_button,
	fraction_button,
	squared_button,
	root_button,
	divide_button,
	num_7_button,
	num_8_button,
	num_9_button,
	multiply_button,
	num_4_button,
	num_5_button,
	num_6_button,
	subtract_button,
	num_1_button,
	num_2_button,
	num_3_button,
	add_button,
	plus_minus_button,
	num_0_button,
	decimal_button,
	equal_button
]

window.mainloop()