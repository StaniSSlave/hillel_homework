# """
# 1. Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить на екран максимум
# із трьох, мінімум із трьох або середньоарифметичне трьох чисел.
# """
# num1 = int(input("Enter first random integer, please: "))
# num2 = int(input("Enter second random integer, please: "))
# num3 = int(input("Enter third random integer, please: "))
#
# task = int(input("Select what you want to do with this numbers:\n"
#                  "\t1. Show the biggest number\n"
#                  "\t2. Show the smallest number\n"
#                  "\t3. Show the average of three of (3)three nums\n"))
####################
# Without exception
####################
# if task == 1:
#     if num1 < num3 and num2 < num3:
#         print(f"Number {num3} is the biggest")
#     elif num2 < num1 and num3 < num1:
#         print(f"Number {num1} is the biggest")
#     elif num3 < num2 and num1 < num2:
#         print(f"Number {num2} is the biggest")
# elif task == 2:
#     if num1 > num3 and num2 > num3:
#         print(f"Number {num3} is the smallest")
#     elif num2 > num1 and num3 > num1:
#         print(f"Number {num1} is the smallest")
#     elif num3 > num2 and num1 > num2:
#         print(f"Number {num2} is the smallest")
# elif task == 3:
#     avr = (num1+num2+num3)/3
#     print(f"Average of three is - {avr}")
# else:
# #     print("Error: Invalid task number, try to restart program, please!")
# ####################
#
# ####################
# # With an exception
# ####################
# try:
#     if task == 1:
#         if num1 < num3 and num2 < num3:
#             print(f"Number {num3} is the biggest")
#         elif num2 < num1 and num3 < num1:
#             print(f"Number {num1} is the biggest")
#         elif num3 < num2 and num1 < num2:
#             print(f"Number {num2} is the biggest")
#     elif task == 2:
#         if num1 > num3 and num2 > num3:
#             print(f"Number {num3} is the smallest")
#         elif num2 > num1 and num3 > num1:
#             print(f"Number {num1} is the smallest")
#         elif num3 > num2 and num1 > num2:
#             print(f"Number {num2} is the smallest")
#     elif task == 3:
#         avr = (num1+num2+num3)/3
#         print(f"Average of three is - {avr}")
#     else:
#         raise Exception("Invalid task number, try to restart program, please!")
# except Exception as e:
#     print(f"Error: {e}")
# ####################


# """
# 2. Користувач вводить з клавіатури кількість метрів.
# Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.
# """
# try:
#     lng = float(input("Enter distance in meters, please: "))
#
#     task = int(input("Select units to transform:\n"
#                      "\t1. Transform to Miles\n"
#                      "\t2. Transform to Inches\n"
#                      "\t3. Transform to Yards\n"))
#     match task:
#         case 1:
#             mil = lng * 0.00062137
#             print(f"Your {lng} meters is {mil} miles")
#         case 2:
#             inch = lng * 39.370
#             print(f"Your {lng} meters is {inch} inches")
#         case 3:
#             yard = lng * 1.0936
#             print(f"Your {lng} meters is {yard} yards")
#         case _:
#             print("Invalid task number, try to restart program, please!")
#
# except ValueError as e:
#     print(f"Error: Invalid input type. Enter numbers only!")