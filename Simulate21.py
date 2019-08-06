class Simulate21:
    def __init__(self):
        cards = {1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:16}
        tmp = []
        for k,v in cards.items():
            tmp.append([k]*v)
        cards_list = [card for i in tmp for card in i]
        self.cards = cards_list
        
    def dealer_result(self):
        current = random.choice(self.cards)
        self.cards.remove(current)
        current_sum = current
        while current_sum<17:
            current = random.choice(self.cards)
            self.cards.remove(current)
            current_sum+=current
        return current_sum
        
    def dealer_result_observed(self,observed):
        current = observed
        self.cards.remove(current)
        current_sum = current
        while current_sum<17:
            current = random.choice(self.cards)
            self.cards.remove(current)
            current_sum+=current
        return current_sum
    
    def player_cards(self):
        card1 = random.choice(self.cards)
        self.cards.remove(card1)
        card2 = random.choice(self.cards)
        self.cards.remove(card2)
        total = card1 + card2
        if card1 == 1 or card2 == 1:
            total = total+10
        return card1,card2,total
        
def simulation(iterations,observed = 0):
    legal_results = []
    lost_count = 0
    for i in range(iterations):
        sim=Simulate21()
        if observed !=0:        
            simulation_result = sim.dealer_result_observed(observed)
        else:
            simulation_result = sim.dealer_result()
        if simulation_result<=21:
            legal_results.append(simulation_result)
        else:
            lost_count+=1
    return np.mean(legal_results),lost_count, lost_count/iterations, (1-lost_count/iterations)*np.mean(legal_results)

def nohit_sim(iterations):
    player_wins = 0
    for i in range(iterations):
        sim = Simulate21()
        player_result = sim.player_cards()[2]
        deal_result = sim.dealer_result()
        if deal_result>21:
            player_wins+=1
        elif player_result>deal_result :
            player_wins+=1
    return player_wins, iterations,  player_wins/iterations
