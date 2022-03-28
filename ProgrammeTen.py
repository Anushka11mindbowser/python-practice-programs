#Approach One : Using class
class Football:
    def __init__(self, wins, losses, draws):
        self.wins = wins
        self.losses = losses;
        self.draws = draws;

    def calculate_score(self):
        w = self.wins * 3
        d = self.draws * 1
        score = w + d
        return score

real_madrid =  Football(10,1,5)
print(real_madrid.calculate_score())

#Approach Two: Using normal function
def football_score():
    win = int(input("Enter the number of wins: \n"))
    losses = int(input("Enter the number of losses: \n"))
    draws = int(input("Enter the number of draws: \n"))
    return (win * 3) + (draws *1)
print(football_score())
