# class Futsal:
#     def __init__(self,team_name,entry_fee):
#         self.team_name=team_name
#         self.entry_fee=entry_fee
#         self.football=[]
#     def addteam(self,team_name):
#         self.football.append(team_name)
#     def total_collection(self):
#         return self.entry_fee*len(self.football)
    
        

# mytournament=Futsal("Divya Gyan",500)    
# mytournament.addteam("DAV")
# mytournament.addteam("bright")
# mytournament.addteam("noman")
# mytournament.addteam("vision")

class DietCalc:
    def __init__(self,user_name,target_calories):
        self.user_name=user_name
        self.target_calories=target_calories
   
    def check_meal(self,meal_calories):
        if meal_calories>self.target_calories:
            print("Too heavy")
        else:
            print("Good choice")

users=DietCalc("Samundra",2000)
users.check_meal(4000)
