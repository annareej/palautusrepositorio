class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        
        def get_score_call(points):
            if(points == 0):
                return "Love"
            elif(points == 1):
                return "Fifteen"
            elif(points == 2):
                return "Thirty"
            elif(points == 3):
                return "Forty"
            else:
                return ""

        score = ""
        temp_score = 0

        if self.get_winning_player() == "draw":
            if self.player1_score < 3:
                score = get_score_call(self.player1_score) + "-All"
            else:
                score = "Deuce"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self.player2_score
            if minus_result == 1 or minus_result == -1:
                score = "Advantage " + self.get_winning_player()
            else:
                score = "Win for " + self.get_winning_player()

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score
                
                score = get_score_call(self.player1_score) + "-" + get_score_call(self.player2_score)
        return score
    
    def get_winning_player(self): 
        if(self.player1_score > self.player2_score):
            return self.player1_name
        elif(self.player2_score > self.player1_score):
            return self.player2_name
        else:
            return "draw"