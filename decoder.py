#Python 3 program to find hidden message in a line of text

string = "Something from your hand reached the questionČ Until she saw how couldL Psalm mountain wild by judith bronteI Only to put on the cabinC Puzzled emma swallowed hard to another wordK Cora and then crawled inside  Brown has been doing all my promiseĤ Sighed in thought he nodded emmaE However and yet but until emmaR Every step toward her in emmaE"

m = ""

def uppersInArray(x):
    
    a = []
    
    for y in x:
        if(y.islower() == False):
                a += y
        else: pass
    return a
    
print(uppersInArray(uppersInArray(string.split())))

#Ultimately the message means nothing. It came from a friend's spam email.

#ar = uppersInArray(string.split())
#print(uppersInArray(ar))

#>>> CULPIOCPKCBHSEREE"
