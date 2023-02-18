#!/usr/bin/env python3

from os import system, name

def clear():
    #for windows
    if name == 'nt':
        _ = system('cls')
    #for mac and linux
    else:
        _ = system('clear')

def change_format(num, before_decimal, after_decimal):
    str_num = str(num).split('.')
    b_num = len(str_num[0])
    a_num = len(str_num[1])
    new_b = []
    new_a = []

    new_a.append(str_num[1])

    while (b_num < before_decimal):
        new_b.append('0')
        b_num += 1
    while (a_num < after_decimal):
        new_a.append('0')
        a_num += 1

    new_b.append(str_num[0])

    a_null = ''
    new_b_str = a_null.join(new_b)
    new_a_str = a_null.join(new_a)
    new_b_a_str = []
    new_b_a_str.append(new_b_str)
    new_b_a_str.append(new_a_str)
    a_null = '.'
    new_str_num = a_null.join(new_b_a_str)

    return new_str_num


principal = float(input("Please enter the amount of loan = "))
interest_rate = float(input("Please enter the applicable interest rate p.a = "))
tenure = float(input("Please enter the tenure in year = "))

clear()

calc_month = 0
calc_year = 0

p = principal
r = (interest_rate / 12) / 100
n = tenure * 12

r1 = (1 + r) ** n
p1 = p * r

r2 = r1 / (r1 - 1)

emi = round(p1 * r2, 2)

print()
print("All Data are indicative not the exact amount due to different taxes.")
print()
msg1 = "Your EMI will be " + str(emi)
print()
print(msg1)
print()

# length for Interest
i_l = format(round(p * r, 2),'.2f')
i_s = i_l.split('.')
i_length = len(i_s[0])

# length for emi
p_str = format(emi,'.2f').split('.')
p_length = len(p_str[0])

# length for balance principal
b_str = format(round(p - (emi - p1),2),'.2f').split('.')
b_length = len(b_str[0])

line_len = 0
while (calc_year < tenure):
    calc_month += 1
    interest = round(p * r, 2)
    p_repay = round(emi - interest, 2)
    p = round(p - p_repay, 2)
    
    # Avoid negative numbers
    if p < 0:
        p = 0.0

    str_int = change_format(interest,i_length,2)
    str_p_rpay = change_format(p_repay,p_length,2)
    str_balance = change_format(p,b_length,2)

    text1 = "| "
    text2 = "Month: " + f"{calc_month:02d}" + " |" + " Year: " + f"{calc_year:02d}" + " || "
    text3 = "Interest: " + str_int + " |" + " Principal payment: "
    text4 = str_p_rpay + " |" + " Balance Principal: " + str_balance + " |"
    msg2 = text1 + text2 + text3 + text4

    line_len = len(msg2)
    a = 0
    while (a < line_len):
        print('-',end='')
        a += 1
    print()
    print(msg2)
    if (calc_month >= 12):
        calc_year += 1
        calc_month = 0
a = 0
while(a < line_len):
    print('-',end='')
    a += 1

a = input()