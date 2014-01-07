import random, hashlib, time
print("--------------------------------------------------------------")
print("----Welcome to KingofPython's hacker proof password gen.! ----")
print("--------------------------------------------------------------")
r = random.SystemRandom()
s = "533c8b20aade2aa9a5b31026f865a7a8"
ranchar = (r.choice(s)) # print random character from the string
rannum = random.randrange(1, 12345672234578)
sport = raw_input("Whats your favorite sport? ")
objected = raw_input("Whats your favorite object? ")
word = raw_input("Whats your favorite word? ")
listed = [sport, objected, word]
ranitem = (random.choice(listed))
bday = raw_input("What is your birthday mm/dd/year? ")
m = hashlib.md5()
m.update(bday)
hexgenp = m.hexdigest()
hexgen = hexgenp[-4:]
randitem = ranitem[:-2]
print("Your hacker proof password is: " + str(randitem) + str(ranchar) + str(hexgen) + str(rannum))

time.sleep(5)


