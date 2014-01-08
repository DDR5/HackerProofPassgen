import random, hashlib, time, string, sys
print("____________________________________________________________")
print(" Welcome to KingofPython's hacker proof password generator!")
print("____________________________________________________________")
print("************************************************************")
time.sleep(3)
print("\n Please keep in mind. If the symbol count + the capital count exceeds the \n password length you may not receive the symbols/capitals you wanted \n")


class Passwordgeneration:
        def __init__(self):
                ran = random.SystemRandom()
                rannum = random.randrange(1, 12345672234578)
                ans1 = raw_input("Do you want capital letters? [Y/N] \n").lower()
                doneUpper = 0
                if ans1 == "y":
                        ans2 = input ("How many capital letters would you like to include? [MAX 8] \n")
                        randomUppercase = ''.join(random.choice(string.ascii_uppercase) for i in range(8))
                        if int(ans2) in range(1,8):
                                doneUpper = randomUppercase[:int(ans2)]
                        
                        else:
                                print("Invalid number entry")
                sym = 0
                symbols = raw_input("Would you like to include symbols in your password [Y/N] \n").lower()
                if symbols == "y":
                        ans3 = input ("How many symbols would you like to include? [MAX 3] \n")
                        listedsyms = ['$', '^', '*', '&' '#', '@']
                        ransym1 = (random.choice(listedsyms))
                        ransym2 = (random.choice(listedsyms))
                        ransym3 = (random.choice(listedsyms))
                        if ans3 == 1:
                                sym = ransym1      
                        if ans3 == 2:
                                sym = ransym1 + ransym2
                        if ans3 == 3:
                                sym = ransym1 + ransym3 + ransym2
                length = raw_input("How long do you want the password to be [MIN 3][Max 52] \n").lower()
                sport = raw_input("Whats your favorite sport? \n").lower()
                objected = raw_input("Whats your favorite object? \n").lower()
                word = raw_input("Whats your favorite word? \n").lower()
                listed = [sport, objected, word]
                ranitem = (random.choice(listed))
                bday = raw_input("What is your birthday mm/dd/year? \n")
                m = hashlib.md5()
                m.update(bday)
                hexgenp = m.hexdigest()
                hexgen = hexgenp[-4:]
                randitem = ranitem[:-2]
                r = random.SystemRandom()
                ranhex = raw_input("Input a random string of chracters. \n")
                m1 = hashlib.md5()
                m1.update(ranhex)
                hexgenp1 = m.hexdigest()
                hexgen1 = hexgenp[:6]
                rannum = random.randrange(1, 12345672234578)
                unfinpassword = str(sym) + str(hexgen) + str(doneUpper) + str(rannum) + str(randitem) + str(hexgen1)
                yourpass = unfinpassword[:int(length)]
                print("Your hacker proof password is: " + yourpass)
                write = raw_input("Would you like to write your password to a .txt file? [Y/N] \n").lower()
                if write == 'y':
                        f = open("passwords.txt","w")
                        f.write("Password: " + yourpass)
                        f.close()
                        print("File is created, thanks for using the hacker proof pass gen by KingofPython")
                else:
                        print("Thanks for using the hacker proof pass gen by KingofPython")
                        sys.exit()

                

                        
                                   
                        
Passwordgeneration()
