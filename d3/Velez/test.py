import pprint as pp
_in = open('input')
input_lines = _in.read()
big_string = input_lines
test_string= 'uuumul(   )'
all_mul_brackets= []
cleaned_brackets= []
mul_vals = []
# print(big_string)

def find_mul(s='', ind_start=0):
    return s.find("mul(", ind_start)

def find_close(s='', ind_start=0):
    return s.find(')', ind_start)
 
def add_mul_brackets(s = '', ind_start=0, ind_end=0):
    all_mul_brackets.append(s[ind_start:ind_end+1])
    
mul_count = big_string.count("mul(")

x = 0
for i in range(mul_count):
    add_mul_brackets(big_string, 
        find_mul(
            big_string, x
        ), 
        find_close(
            big_string, (find_mul(big_string, x)+1)
    ))
    x = find_mul(big_string, x)+1

for i in range(len(all_mul_brackets)):
    cleaned_brackets.append(
        all_mul_brackets[i].strip('mul()')
        )

for i in range(len(cleaned_brackets)):
    mul_vals.append(
        cleaned_brackets[i].split(',')
    )

print(mul_vals)

muls_sum = 0
temp = []
for i in range(len(mul_vals)):
    if len(mul_vals[i]) > 2:
        temp.append(mul_vals[i])
    if mul_vals[i][0].isnumeric() and mul_vals[i][1].isnumeric() and len(mul_vals[i]) == 2:
        print(mul_vals[i])
        muls_sum += (int(mul_vals[i][0]) * int(mul_vals[i][1]))
    else:
        print(mul_vals[i], "Not numeric")
print(muls_sum)

pp.pp(temp)
