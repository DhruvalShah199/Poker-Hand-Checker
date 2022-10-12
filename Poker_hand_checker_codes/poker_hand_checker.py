#!/home/pi/software/bin/python3

import cgi, cgitb
import subprocess

cgitb.enable( )

form = cgi.FieldStorage()

faces = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "th", "jh", "qh", "kh", "ah"
"2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "tc", "jc", "qc", "kc", "ac"
"2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "ts", "js", "qs", "ks", "as"
"2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "td", "jd", "qd", "kd", "ad"]
rank = {"t":10, "j":11, "q":12, "k":13, "a":1}
deck = {}

cardNum = 0
for cardNum in range(len(faces)) :
	deck[cardNum] = faces[cardNum]
	cardNum += 1

def findCategory(cards) :
    if isStraightFlush(cards) :
        return "SF"
    elif isFourOfAKind(cards) :
        return "4K"
    elif isFullHouse(cards) :
        return "FH"
    elif isFlush(cards) :
        return "FL"
    elif isStraight(cards) :
        return "ST"
    elif isThreeOfAKind(cards) :
        return "3K"
    elif isTwoPair(cards) :
        return "2P"
    elif isOnePair(cards) :
        return "1P"
    elif isHighCard(cards) :
        return "HC"
    else:
    	return ", Error!! No possible outcome"

def isHighCard(cards) :
    if not (isOnePair(cards) or isTwoPair(cards) or isThreeOfAKind(cards) or isStraight(cards) or isFlush(cards) or isFullHouse(cards) or isFourOfAKind(cards) or isStraightFlush(cards)) :
        return True
    else :
        return False	

def isOnePair(cards) :
    value = []
    for card in cards :
        if card[0] in value :
            return True
        value.append(card[0])
    return False

def isTwoPair(cards) :
    var = {}
    num = 0
    for card in cards :
        if num >= 2 :
            break
        if card[0] in var :
            if var[card[0]] + 1 == 2:
                num += 1
            var[card[0]] += 1
        else :
            var[card[0]] = 1
    if num == 2 :
        return True
    else :
        return False    

def isThreeOfAKind(cards) :
    var = {}
    for card in cards :
        if card[0] in var :
            var[card[0]] += 1
        else:
            var[card[0]] = 1

    for key, value in var.items() :
        if value >= 3:
            return True
    return False

def isStraight(cards) :
    value = []
    for card in cards :
        if card[0].isnumeric() :
            value.append(int(card[0]))
        else:
            value.append(int(rank[card[0]]))
    range1 = min(value)
    range2 = max(value) + 1
    total = sum(value)
    expectedSum = 0
    
    for i in range(range1, range2) :
        expectedSum += i
    if(expectedSum == total) :
        return True
    else :
        return False

def isFlush(cards) :
    suit = cards[0][1]
    for card in cards :
        if card[1] != suit :
            return False
    return True

def isFullHouse(cards) :
    twoPair = False
    threePair = False
    value = []
    for card in cards :
        value.append(card[0])
    for rank in value :
        if value.count(rank) == 3 :
            threePair = True
        if value.count(rank) == 2 :
            twoPair = True
    if(twoPair == True) and (threePair == True) :
        return True
    else :
        return False

def isFourOfAKind(cards) :
    value = []
    for card in cards :
        value.append(card[0])
    for rank in value :
        if value.count(rank) == 4 :
            return True
    return False

def isStraightFlush(cards) :
    if isStraight(cards) and isFlush(cards) :
        return True
    else :
        return False

print("Content-type: text/html\n\n")
print("<h1>Poker Hand Checker\n</h1>")

if len(form)!= 5 :
    print("<p style='color:red;'>Please go back and select exactly 5 cards</p>")
    exit()

selectedCards = []
print("<p><b>Cards selected:</b></p>")
for field in form :
    print("<div class='card' style='display:inline-block;margib:15px;'><img src='http://192.168.2.175:8080/~pi/cards/{}.png\' height=\'53\' width=\'37\'/></div>".format(field))
    selectedCards.append(field)

if(findCategory(selectedCards) == "HC") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a HIGH CARD</h2>")
elif(findCategory(selectedCards) == "1P") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a ONE PAIR</h2>")
elif(findCategory(selectedCards) == "2P") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a TWO PAIR</h2>")
elif(findCategory(selectedCards) == "3K") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a THREE OF A KIND</h2>")
elif(findCategory(selectedCards) == "ST") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a STRAIGHT</h2>")
elif(findCategory(selectedCards) == "FL") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a FLUSH</h2>")
elif(findCategory(selectedCards) == "FH") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a FULL HOUSE</h2>")
elif(findCategory(selectedCards) == "4K") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a FOUR OF A KIND</h2>")
elif(findCategory(selectedCards) == "SF") :
	print("<h2 style='color:blue;'>Your Poker Hand represents a STRAIGHT FLUSH</h2>")
else :
	print("<h2 style='color:blue;'>Your Poker Hand represents an ERROR</h2>")

def piInfo():
   print(subprocess.check_output("date", shell=True, text=True))
   print(subprocess.check_output("ps ax | grep httpd | tail -10", shell=True, text=True))
   print(subprocess.check_output("uname -a", shell=True, text=True))
   print(subprocess.check_output("cat /sys/class/net/eth0/address", shell=True, text=True))
   print(subprocess.check_output("sudo cat /proc/cpuinfo | tail -5", shell=True, text=True))
   print(subprocess.check_output("ifconfig | grep netmask", shell=True, text=True))

# end def

piInfo( )