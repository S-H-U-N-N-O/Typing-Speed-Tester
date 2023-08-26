from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error 

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)
while True:
    ck = input("Do you want to test your typing speed? Y/N : ")
    if ck == "Y":
        test = ["Hello My name is Howard and I am from Dark Web's darkest part where no one can access", 
            "Oh dawg thats mine which I have been finding from thirty nine years and now I finally found it",
            "Do you know any good gaming laptop in ninety to ninety five thousand bangladeshi taka because I need one very urgent"]

        test1 = r.choice(test)
        print("                                                                 *****Typing Test*****")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print('Speed: ', speed_time(time_1, time_2, testinput), "w/sec")
        print("Error :", mistake(test1, testinput))
    elif ck == "N":
        print("Thank You")
        break
    else:
        print("Wrong Input :(")