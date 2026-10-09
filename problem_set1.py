def main():
    blue()

def blue():
    red =3
    purple=red*12
    print (purple)

def blastoff():
    count = input("what number do you want to count from? ")
    for i in range (count, 0, -1):
        print (i)
    print (blastoff)

def candy_shop():
    candies = ["skittles","haribo","sour patch"]
    candies.append("kit kat")
    candies.insert(1,"nerds")
    candies.sort()
    candies.remove("kit kat")
    #ask user for 3 candies and add them to the list
    user_candies=[]
    all_candies= user_candies+candies
    print (len(all_candies))
    print(*all_candies,sep="\n")
    return ((len(all_candies))*1.25)

def fruit_pricing():
    fruits={
        "apple":.75,"banana":1.25,"orange": .8,"peach":2.25,"coconut":2.8
    }
    fruits["pear"]=1.15
    fruits.get("peach")
    for i in fruits:
        if fruits.get(i)>=1.25:
            print(i)
    trip=3*fruits["apples"]+2*fruits["banana"]+fruits["coconut"]
    print("trip")


            



          

    
    

if __name__ == "__main__":#runs the whole project
    main()
        