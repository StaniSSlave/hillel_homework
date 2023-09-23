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

