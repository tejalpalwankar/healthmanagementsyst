# heath management system
def getdate():
    import datetime
    return datetime.datetime.now()


a = input("Do you want to write the data or retrieve the data. \n Enter w for write \n Enter r for retrieve ")
if a=='w' :
    write = int(input("whose data you want to write \n1.Harry \n2.Rohan \n3.Hamad"))
    if write==1:
        harry = input("do you want to update your meal or excercise \n enter m for meal \n enter e for excercise ")
        if harry=='m':
            hm = input("enter your meal \n")
            f = open("harrym.txt","a")
            f.write(f"[{str(getdate())}]")
            f.write(f"{hm}\n")
            print("you have successfully entered your meal")
            f.close()
        elif harry=='e':
            he = input("enter your exercise \n")
            f = open("harrye.txt", "a")
            f.write(f"[{str(getdate())}]")
            f.write(f"{he}\n")
            print("you have successfully entered your exercise")
            f.close()
        else:
            print("invalid input")
    elif write==2:
        rohan = input("do you want to update your meal or excercise \n enter m for meal \n enter e for excercise ")
        if rohan=='m':
            rm = input("enter your meal \n")
            f = open("rohanm.txt","a")
            f.write(f"[{str(getdate())}]")
            f.write(f"{rm}\n")
            print("you have successfully entered your meal")
            f.close()
        elif rohan=='e':
            re = input("enter your exercise \n")
            f = open("rohane.txt", "a")
            f.write(f"[{str(getdate())}]")
            f.write(f"{re}\n")
            print("you have successfully entered your exercise")
            f.close()
        else:
            print("invalid input")
    elif write==3:
        hamad = input("do you want to update your meal or excercise \n enter m for meal \n enter e for excercise ")
        if hamad=='m':
            ham = input("enter your meal \n")
            f = open("hamadm.txt","a")
            f.write(f"[{str(getdate())}]")
            f.write(f"{ham}\n")
            print("you have successfully entered your meal")
            f.close()
        elif hamad=='e':
            hae = input("enter your exercise \n")
            f = open("hamade.txt", "a")
            f.write(f"[{str(getdate())}]")
            f.write(f"{hae}\n")
            print("you have successfully entered your exercise")
            f.close()
        else:
            print("invalid input")

elif a=='r' :
    read = int(input("whose data you want to retrieve \n1.Harry \n2.Rohan \n3.Hamad \n"))
    if read==1:
        harry = input("do you want to retrieve your meal or excercise \n enter m for meal \n enter e for excercise \n")
        if harry=='m':
            f = open("harrym.txt")
            print(f.read())
            f.close()
        elif harry=='e':
            f = open("harrye.txt")
            print(f.read())
            f.close()
        else:
            print("invalid input")
    if read==2:
        rohan = input("do you want to retrieve your meal or excercise \n enter m for meal \n enter e for excercise \n")
        if rohan=='m':
            f = open("rohanm.txt")
            print(f.read())
            f.close()
        elif rohan=='e':
            f = open("rohane.txt")
            print(f.read())
            f.close()
        else:
            print("invalid input")
    if read==3:
        hamad = input("do you want to retrieve your meal or excercise \n enter m for meal \n enter e for excercise \n")
        if hamad=='m':
            f = open("hamadm.txt")
            print(f.read())
            f.close()
        elif hamad=='e':
            f = open("hamade.txt")
            print(f.read())
            f.close()
        else:
            print("invalid input")
else:
    print("invalid input")





