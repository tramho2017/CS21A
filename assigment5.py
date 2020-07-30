#This program generate two random cards
#it also tells the name of two card
#then it adds the total point of two card together
from random import randint
DeckofCard = {1: ["king", "spade"], 2: ["Queen", "spade"], 3: ["Jack", "spade"], 4: ["ten", "spade"],
                  5: ["nine", "spade"],6:["eight","spade"],7:["seven","spade"],8:["six","spade"],9:["five","spade"],10:["four","spade"],11:['three',"spade"],\
              12:["two","spade"], 13:["ace","spade"], 14:["king",'heart'],15:["Queen","heart"],16:["jack","heart"],17:['ten',"heart"],18:['nine','heart'],\
              19:["eight", "heart"],20:["seven","heart"],21:["six","heart"],22:['five','heart'],23:["four","heart"],24:['three','heart'],25:['two','heart']\
    ,26:["ace","heart"],27:['king','diamond'],28:['queen','diamond'],29:['jack','diamond'],30:["ten",'diamond'],31:['nine','diamond'],32:['eight','diamond'],\
              33:["seven",'diamond'],34:['six','diamond'],35:['five','diamond'],36:['four','diamond'],37:['three','diamond'],38:['two','diamond'],\
              39:['ace','diamond'],40:["king","clubs"],41:['queen','clubs'],42:['jack','club'],43:['ten','club'],44:['nine',"clubs"],45:['eight','club'],\
              46:["seven",'clubs'],47:['six','club'],48:['five','club'],49:["four",'club'],50:["three",'club'],51:['two','club'],52:['ace','club']}
class Card: #create card class
  print('do you want to play')

  def __init__(self):
       self.rank=0
       self.suit=0
       draw=randint(1, 52)

       self.suit=DeckofCard[draw][1]
       self.rank=DeckofCard[draw][0]
       nrank=0


  def getRank(self): #this method return the rank of the card(1 through 13)
      return self.rank
  def getSuit(self):#this method return the suit of the card(diamond, club, heart, spade)
      return self.suit

  def getbjvalue(self): #getbjvalue call the function getpoint(card)
      # print(card1.rank)
      # print(getpoint(card1))
      # print(card2.rank)
      # print(getpoint(card2))
      print("your total point is", getpoint(card1)+getpoint(card2))

      return  getpoint(card1)+getpoint(card2)


  def __str__(self): # this funtion give the name of the card
      return self.rank +" of " +self.suit
     # print(self.rank +" of " +self.suit)

def getpoint(card): #convert string number into interger
    if card.getRank() == 'ace': nrank = 1
    if card.getRank() =='two': nrank = 2
    if card.getRank()== 'three': nrank = 3
    if card.getRank() == 'four': nrank = 4
    if card.getRank() == 'five': nrank = 5
    if card.getRank ()== 'six': nrank = 6
    if card.getRank ()== 'seven': nrank = 7
    if card.getRank ()== 'eight': nrank = 8
    if card.getRank() == 'nine': nrank = 9
    if card.getRank() == 'ten': nrank = 10
    if card.getRank ()== 'jack': nrank = 10
    if card.getRank ()== 'queen': nrank = 10
    if card.getRank ()== 'king': nrank = 10
    return (nrank)
print('do you want to play? Press yes for Yes Press any key for No')
choice=input()
if choice=="yes":

    card1=Card()
    card2=Card()
#print("card2 suit",card2.suit)
#print('card2 rank',card2.rank)

#print(card1.getRank())

#print(card1)
    card1.getSuit()
    print("card 1 is ", card1)
    card2.getRank()
#print(card2)
    card2.getSuit()
    print("card 2 is ", card2)
    card1.getbjvalue() #call the funtion bjvalue

