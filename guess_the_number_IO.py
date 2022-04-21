import random
class project:
 print("welcome to the guess the number game!!!")
 name=input("enter your name..")
 print(f"{ name } you  will be allowed to guess the number until you guesses it right...")
 print("------hope u will enjoy the game-----")
 print("******LET'S GO******")

 comp_guess = random.randint(1, 100)

 c1=0
 def game(self,number):
    self.c1=self.c1+1
    
    if (number > self.comp_guess):
         print("enter lower number..")
         return True
    elif (number < self.comp_guess):
        print("enter higher number..")
        return True
    else:
        print("you guessed it right  #####")
        print(f"you made it in {self.c1 } attempts")
        
        with open("highscore.txt", "r") as f:
             data = int(f.read())
        if (data>self.c1):
                with open("highscore.txt", "w") as f:
                 f.write(str(self.c1))
                with open("highscorelog.txt", "a") as f:
                      print("::::made a new highscore::::")
                      f.write(f"highscore made by {self.name } in {str(self.c1)} attempts\n")
        else:
          pass

        return False
c=project()        
check = True
while (check):

    number = int(input("enter a number.. "))
    check=c.game(number)