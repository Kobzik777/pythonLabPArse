from pyparsing import Word, nums, Literal

EXPRESION = input("Enter expression\n")
pm_sign = Literal("+") | Literal("-") | Literal("*")
int_num = Word(nums)
float_num=int_num + pm_sign + int_num
s = float_num.parseString(EXPRESION).asList()
if s[1] == "+" :
    print(int(s[0]) + int(s[2]))
elif s[1] == "-":
    print((int(s[0]) - int(s[2])))
else:
    print(int(s[0]) * int(s[2]))
