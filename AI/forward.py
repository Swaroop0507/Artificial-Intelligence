database = ["Crocks", "Eating flies","Shrimps","Sings"]
knownbase = ["Frog","Cannary","Green","Yellow"]

def display():
    print("\n X is")
    print("\n1. Crocks \n2. Eating flies \n3. Shrimps \n4. Sings")
    print("\n Select any one ",end='')

def main():
    print("\n *-------Forward Chaining-------*")
    display()
    x= int(input())
    
    if x ==1 or x==2:
        print("Chances of Frog",end='')
    elif x==3 or x==4:
        print("Chances of Canarry",end='')
    else:
        print("Invalid",end='')

    if x>=1 and x<=4:
        print("\n X is ",end='')
        print(database[x-1],end='')
        print("\n Select the Color \n1. Green \n2. Yellow ",end='')

        k= int(input())

        if k==1 and (x==1 or x==2):
            print("Yes it is ",end='')
            print(knownbase[0], end='')
            print(" and color is ",end='')
            print(knownbase[2],end='')
        elif k==2 and (x==3 or x==4):
            print("Yes it is ",end='')
            print(knownbase[1], end='')
            print(" and color is ",end='')
            print(knownbase[3], end='')
        else:
            print("Invalid Knownbase")

if __name__ =="__main__" :
    main()


