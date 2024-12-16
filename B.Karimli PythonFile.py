#my_dict = {
#     "mark" : "Range rover",
#     "year" : 2015,
#    "model" :  "Long"
#}
#
#print(my_dict["mark"])
#print(my_dict["year"])
#print(my_dict["model"])
#
import tkinter

#my_dict ={
#    "Names" : ["Allen", "Jayson", "Shaquille", "Larry", "Kareem"],
#    "Surnames" : ["Iverson", "Tatum", "O'neal", "Bird", "Abdul-Jabbar"],
#    "Heights"  : ["1.83M", "2.03M", "2.16M", "2.06M", "2,18M"]
#}
#
#choice = int(input("Enter Your Choice"))
#
#if choice == "add":
# new_player = input("Enter New Player")
#my_dict["Names"].append(new_player)
#print(my_dict)
#if choice == "remove":
# old_player = input("Enter Old Player")
#my_dict["Names"].remove(old_player)
#print(my_dict)


#my_dict ={
#    "EN" : ["answer", "hammer", "watch", "wireless"],
#    "FR" : ["répondre", "marteau", "montre", "sans fil"]
#}
#choice = input("enter a choice")
#if choice == "add":
#    new_word = input("Enter New Word")
#my_dict["EN"].append(new_word)
#print(my_dict)





#my_list = ["Shahin", "Eltun", "Ayxan"]
#my_tuple = ("Dima", "Behram" , "Nicat")
#my_dict = {
#    "p1" : "Nicat",
#    "p2" : "Shahin",
#    "p3" : "Seymur",
#}
#




#my_choice = input("Enter Your Choice")
#
#my_tuple = ("Watermelon", "Apple", "Apple", "Apple", "Apple")
#count = 0
#for i in range(len(my_tuple)):
#    if my_tuple[i] == my_choice:
#     count+=1
#print(count)


#my_choice = input("Enter Your Choice")
#
#my_tuple = ("Watermelon", "Apple", "Apple", "Apple", "Apple")
#count = 0
#for i in range(len(my_tuple)):
#    if my_choice  in my_tuple[i]:
#     count+=1
#print(count)









#choice_car = input("Enter Choice")
#new_car = input("Enter New Car")
#my_tuple = (159,12,14,1,23,323)
#my_list = []
#
#for i in range(len(my_tuple)):
#    if choice_car == my_tuple[i]:
#        my_list.append(new_car)
#    else:
#        my_list.append(my_tuple[i])
#print(my_list)



# try:
#   print( a )
# except NameError:
#    print("Данной переменной не существует")

# try:
#   A = int(input("Type first number"))
#   B = int(input("Type second number"))
#   print(A / B)
# except ZeroDivisionError:


#     print("You Can't enter 0")
#
# def divine_everything_func(a):
#     try:
#         print(5 / A)
#     except ZeroDivisionError:
#         print("You Can't divine 0")
#
#
# a = int(input("Type first number"))
# divine_everything_func(a)

# try:
#
#  print( int("Dima"))
# except TypeError:
#  print("Пиши нормально")


# try:
#
#  print( int("Dima"))
# except TypeError:
#  print("Пиши нормально")





# try:
#  print( int("123"))
# except ValueError:
#  print("Пиши нормально")
# finally:
#     print("Check ended")
#



# import math
# try:
#     a = int(input("Enter a number"))
#     print(math.sqrt(a))
# except BaseException:
#     print("Not correct")
# finally:
#  print("Always")
#
#  print( math.sqrt(-4))





# import random as rd
# import random as tk
# import tkinter
#
# root = tkinter.Tk()
#
# name = input("Enter your Name")
#
# root.minsize(50, 100)
# root.maxsize(1920, 1080)
# Label = tkinter.Label(root, text= "email")
# Label = tkinter.Entry(root)
# Entry = tkinter.Label(root, text="password")


# import tkinter
# from tkinter import messagebox
#
# root = tkinter.tk()
#
# root.geometry



#
# Name = int(input("Enter Your Name"))
# Surname = int(input("Enter Your surname"))
# Age = int(input("Enter Your Age"))
# list.insert(0, Name)
# list_box = tkinter.Listbox()
#
#
#
#
#
#
# list = tkinter.Listbox(root)




#def bubble_sort(array):    for i in range(len(array)):        # loop to compare array elements        for j in range(0, len(array) - i - 1):            # compare two adjacent elements            # change > to < to sort in descending order            if array[j] > array[j + 1]:                # swapping elements if elements                # are not in the intended order                temp = array[j]                array[j] = array[j + 1]                array[j + 1] = temp# Sample list to be sortedarr_id = ["Elmin","Shahin","AAAAA","rrrr"]arr_number = [656,51,12 ,45 , 72, 10, 2, 18]choice = 0while choice != 5:    print("1. Sort by IDs \n 2.Sort by names \n 3.Show result \n 4.  EXIT")    choice = int(input("Enter choice"))    if choice == 1 :        bubble_sort(arr_id)    elif choice == 2:        bubble_sort(arr_number)    elif choice == 3:        print(f"ARRAY IDs : {arr_id}")        print()




# def dima_func(yo):
#     print("DIMA DIMA")
#     print("Shahin")
#     return "Abu"
#
# dima_func()



#
# import tkinter
#
# root = tkinter.Tk()
# root.geometry("500x500")
#
# name_entry = tkinter.Entry(root)
# name_entry.pack( x= 23, y= 345)
#
# submit_button = tkinter.Button(root, text="Click Me", command=submitFunc)
# submit_button.pack()
# root.mainloop()









