import sys
sys.path.append("c:\code")
import functions2 as f
def calculate_total (exp):
    total=0
    for item in exp:
        total += item
    return total

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

tom_total = calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)

print(tom_total)
print(joe_total)


# sum of two numbers
def sum(a,b):
    total = a + b
    return total
n =sum(5,6)
print(n)

print("SOmething")
area = f.calculate_square_area(10)
area = f.calculate_triangle_area(5,2)
print(area)