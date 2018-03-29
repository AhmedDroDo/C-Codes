st1=["2","4","9"]
st2=["7","5","3"]
st3=["6","1","8"]
st4=["2","7","6"]
st5=["9","5","1"]
st6=["4","3","8"]
st7=["2","5","8"]
st8=["4","5","6"]

print("\nName : Ahmed Taha Basyoni")
print("ID : 20170023")
print("Game : 3")

while (True):
    s1=[]
    s2=[]
    ls=["1","2","3","4","5","6","7","8","9"]
    print ("ـ"*80)
    print (" "*30+"Number Scrabble Game"+" "*30)
    print ("ـ"*80)
    n1=str(input("\nPlayer (1) Enter Your Name: "))
    n2=str(input("Player (2) Enter Your Name: "))
    while (True):
        while (True):
            print ("\n"+"ـ"*80)
            print (ls)
            p1=str(input("\n"+n1+" Swap Number: "))

            if (p1=="1") and ("1" in ls):
                s1.append(p1)
                ls.remove("1")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="2") and ("2" in ls):
                s1.append(p1)
                ls.remove("2")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="3") and ("3" in ls):
                s1.append(p1)
                ls.remove("3")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="4") and ("4" in ls):
                s1.append(p1)
                ls.remove("4")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="5") and ("5" in ls):
                s1.append(p1)
                ls.remove("5")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="6") and ("6" in ls):
                s1.append(p1)
                ls.remove("6")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="7") and ("7" in ls):
                s1.append(p1)
                ls.remove("7")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="8") and ("8" in ls):
                s1.append(p1)
                ls.remove("8")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p1=="9") and ("9" in ls):
                s1.append(p1)
                ls.remove("9")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            print ("\nOops! You Must Swap Number Between 1 to 9 and Not Choosen Before ")

        if (set(st1).issubset(set(s1))) or (set(st2).issubset(set(s1))) or (set(st3).issubset(set(s1))) or (set(st4).issubset(set(s1))) or (set(st5).issubset(set(s1))) or (set(st6).issubset(set(s1))) or (set(st7).issubset(set(s1))) or (set(st8).issubset(set(s1))):
            print ("ـ"*80)
            print ("Congratulations! player (1) Wins")
            break

        elif (ls==[]):
            print ("\nDraw!")
            break

        while (True):
            print("ـ"*80)
            print(ls)
            p2=str(input("\n"+n2+" Swap Number: "))

            if (p2=="1") and ("1" in ls):
                s2.append(p2)
                ls.remove("1")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="2") and ("2" in ls):
                s2.append(p2)
                ls.remove("2")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="3") and ("3" in ls):
                s2.append(p2)
                ls.remove("3")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="4") and ("4" in ls):
                s2.append(p2)
                ls.remove("4")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="5") and ("5" in ls):
                s2.append(p2)
                ls.remove("5")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="6") and ("6" in ls):
                s2.append(p2)
                ls.remove("6")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="7") and ("7" in ls):
                s2.append(p2)
                ls.remove("7")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="8") and ("8" in ls):
                s2.append(p2)
                ls.remove("8")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            elif (p2=="9") and ("9" in ls):
                s2.append(p2)
                ls.remove("9")
                print (n1+"=",s1,"|",n2+"=",s2)
                break

            print ("\nOops! You Must Swap Number Between 1 to 9")

        if (set(st1).issubset(set(s2))) or (set(st2).issubset(set(s2))) or (set(st3).issubset(set(s2))) or (set(st4).issubset(set(s2))) or (set(st5).issubset(set(s2))) or (set(st6).issubset(set(s2))) or (set(st7).issubset(set(s2))) or (set(st8).issubset(set(s2))):
            print ("\nCongratulations! player (2) Wins")
            break


