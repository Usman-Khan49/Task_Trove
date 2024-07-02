
class Users:
    def __init__(self,username,xp,rank,level):
        self.username = username
        self.xp = xp
        self.rank = rank
        self.level = level
    
    def Rank_up(self):
        if self.xp == 1000 and self.rank == "Novice":
            self.xp = 0
            self.rank = "Amateur"
        if self.xp == 2000 and self.rank == "Amateur":
            self.xp = 0
            self.rank = "Expert"
    
    def xp_inc(self,xp):
        self.xp = xp + 100

    
    
        