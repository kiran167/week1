from datetime import datetime
def greeting(name):
    present_time=datetime.now()
    time = present_time.strftime("%H")
    current_time=int(time)
    if(current_time<11 and current_time>5):
        print(" Hi "+name+" Good Morning..!!\n")
    if(current_time<18 and current_time>11):
        print(" Hi "+name+" Good Afternoon..!!\n")
    if(current_time<22 and current_time>19):
        print(" Hi "+name+" Good Evening..!!\n")
    else:
        print("OH..! Its High Time\n")
    choice()
def choice():
    t=True
    while(t==True):
        print("What do you want me to do:-" \
              +"\n1.Calulation" \
            +"\n2.CROP info ..."\
            +"\n3.Exit")
        user_input=int(input())
        if(user_input==1):   
            calculation()
        elif(user_input==2):
            crops()
        elif(user_input==3):
            t=False
        else:
            print("Enter a valid option")
def calculation():
    try:
        e = eval(input("Enter The Expression : "))
    except ZeroDivisionError:
        print("divided by zero cannot be validated")
    except:
        print("Not a valid expression")
    else:
        print(f"Here is your answer Buddy {e}")


def crops():
    print("Hii.. I am here to suggest the crops based on your region")
    print("Please enter the region u belong to:\n1.coastaandhra\n2.rayalaseema")
    n=int(input("Only integer 1 or 2\n"))
    try:
        if(n==1):
            region={"summer":"Paddy\nVegetables like:-\nBrinjal,Chillies\nFruits like Melons etc..","monsoon":"GroundNut\nCotton","winter":"Millets\nPulses","rates":{"summer":"Paddy:1,826\nBrinjal:2,000\nChillies:8,500 - 9,000\nWatermelons:2,100\n","monsoon":"GroundNut:4,500\nCotton:4,500\n","winter":"Ragi:2,300\nCheakPea:4,500\nDry Green Pea:2,900"}}
        elif(n==2):
            region={"summer":"Vegetables like :-\nTomato\nChillies\nOnions etc..\n Try to prefer horticulture","monsoon":"Maize\nRedGram\nGroundNut\nPaddy\nCotton","winter":"Turmeric\nfruits like Mango and orange are also preferrable","rates":{"summer":"Tomato:1,300\nChillies:8,000\nOnions:3,400","monsoon":"Maize:1,650-1,850\nRedGram:4,412\nGroundNut:4,500\nPaddy:1,850\nCotton:11,000","winter":"Turmeric:6,800\n Mango:9,000\norange:6000\n"}}
    except:
        print("invalid region")
    present_time=datetime.now()
    current_time=present_time.month
    print("Do you want to check for the present season or any other season\n")
    text=input("Enter Yes to change season or else no\n")
    if(text=="Yes"):
        t=True
        while(t==True):
            season=input("Please enter summer or winter or monsoon\n")
            if(season=="summer" or season=="monsoon" or season=="winter"):
                t=False
    else:
        if(current_time>=3 and current_time<=5):
            season="summer"
        if(current_time>=6 and current_time<=10):
            season="monsoon"
        if(current_time>=11 or current_time<=2):
            season="winter"
    print("You can go with \n"+region.get(season))
    print("Do you want the current rates of crops per quintal:")
    s=input("Enter Yes/No\n")
    if(s=="Yes"):
        print("Price of crops per quintal:\n"+region["rates"][season])
    else:
        pass
def start():
    name=input(" Hi Nice To Meet You\n May I Know your Name : ")
    print("\n")
    greeting(name)
start()