from database_operations import *
import sys
while(True):
    print("***************contact book***************")
    print("1)new conact")
    print("2)view contact")
    print("3)delete contact")
    print("4) exit")
    print("Enter choice to continue : ")
    ch=int(input())
    if ch==4:
        sys.exit(0)
    elif ch==1:
        print("Enter name :")
        name=input()
        print("Enter number :")
        num=input()
        print("Enter address")
        add=input()
        write_to_base(name,num,add)
        print("Save success")
    elif ch==2:
        print("Enter name to view ")
        name=input()
        res=fetch_by_name(name)
        if res==[]:
            print("No reecords by that name")
        else:
            print(f"The number of {name} is {res[0][1]}")
        #  res=[('nana','22434','gergeger')]
        # res[0]=('nana','2323','dfwrgr')
        #  res[0][1]='2323'
    else:
        print("Enter number to delete : ")
        num=input()
        del_from_base(num)
        print("Deletion success")