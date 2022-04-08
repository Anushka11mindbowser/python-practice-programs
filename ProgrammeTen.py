#Approach One : Using class
class Football:
    def __init__(self, wins, losses, draws):
        self.wins = wins
        self.losses = losses;
        self.draws = draws;

    def calculate_score(self):
        #Every win accounts for 3 points, draws for 1 point and loss for zero
        w = self.wins * 3
        d = self.draws * 1
        score = w + d
        return score

real_madrid =  Football(10,1,5)
print(real_madrid.calculate_score())

#Approach Two: Using normal function
def football_score():
    try:
        win = int(input("Enter the number of wins: \n"))
        losses = int(input("Enter the number of losses: \n"))
        draws = int(input("Enter the number of draws: \n"))
        return (win * 3) + (draws *1)
    except:
        print("Entered wrong values")
print(football_score())
