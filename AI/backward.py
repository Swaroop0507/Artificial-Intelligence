database = ["Crocks", "Eating flies","Shrimps","Sings"]
knownbase = ["Frog","Canarry"]
color = ["Green","Yellow"]

def display():
    print("\n1. Frog \n2. Canarry ",end='')
    print("\n Select any one ",end='')

def main():
    print("\n *----Backward Chaining-----*")
    display()
    x=int(input())
    print("\n ",end='')

    if x==1:
        print("Chances of eating flies ",end='')
    elif x==2:
        print("Chances of shrimping ",end='')
    else:
        print("Invalid choice")

    if x>=1 or x<=2:
        print(knownbase[x-1], end='')
        print("\n Select the color \n1. Green \n2. Yellow ",end='')
        print("\n ",end='')

        k = int(input())

        if k==1 and x==1:
            print("Yes it is in ",end='')
            print(color[0], end='')
            print(" color and will ",end='')
            print(database[0], end='')
        elif k==2 and x==2:
            print("Yes it is in ",end='')
            print(color[1], end='')
            print("color and will ",end='')
            print(database[1], end='')
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
