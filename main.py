
class character:
    def __init__(self, name, phrase1, phrase2):
        self.name = name
        self.phrase1 = phrase1
        self.phrase2 = phrase2
        self.level = 0 
    
    
    
    def speak(self, phraseNum):
        if phraseNum == 1:
            print(self.phrase1)
        elif phraseNum == 2:
            print(self.phrase2)
    
    def setLevel(self,newLevel): 
        self.level = newLevel
        print(newLevel)
        
        
# Task1

character_1 = character("Jett", "Dash", "Ace")
character_2 = character("Reyna", "Dark", "Hola")


        
# Task 2 

character_1.speak(1)
character_2.setLevel(3)
character_1.speak(2)

        
        
        
            