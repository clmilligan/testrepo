import time
def main():
    blue()
    time.sleep(5)
    blastoff()
    time.sleep(5)
    print(candy_shop())
    time.sleep(5)
    fruit_pricing()

def blue():
    red =3
    purple=red*12
    print (purple)

def blastoff():
    count = int(input("what number do you want to count from? "))
    for i in range (count, 0, -1):
        print (i)
    print ("Blastoff")

def candy_shop():
    candies = ["skittles","haribo","sour patch"]
    candies.append("kit kat")
    candies.insert(1,"nerds")
    candies.sort()
    candies.remove("kit kat")
    #ask user for 3 candies and add them to the list
    candy1=input("#1 favorite candy: ")
    candy2=input("#2 favorite candy: ")
    candy3=input("#2 favorite candy: ")
    user_candies=[candy1,candy2,candy3]
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
    trip=3*fruits["apple"]+2*fruits["banana"]+fruits["coconut"]
    print(trip)
 
if __name__ == "__main__":#runs the whole project
    main()
     