class Simulate21:
    def dealer_result(self):
        cards = {1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:16}
        tmp = []
        for k,v in cards.items():
            tmp.append([k]*v)
        cards_list = [card for i in tmp for card in i]
        current = random.choice(cards_list)
        cards_list.remove(current)
        current_sum = current
        while current_sum<=21:
            current = random.choice(cards_list)
            current_sum+=current
            cards_list.remove(current)
            if current_sum>=17:
                break
        return current_sum
    
    def dealer_result_observed(self,observed):
        cards = {1:4,2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:16}
        tmp = []
        for k,v in cards.items():
            tmp.append([k]*v)
        cards_list = [card for i in tmp for card in i]
        current = observed
        cards_list.remove(current)
        current_sum = current
        while current_sum<=21:
            current = random.choice(cards_list)
            current_sum+=current
            cards_list.remove(current)
            if current_sum>=17:
                break
        return current_sum
        
    
    def simulation(self,iterations,observed = 0):
        legal_results = []
        lost_count = 0
        for i in range(iterations):
            if observed !=0:        
                simulation_result = self.dealer_result_observed(observed)
            else:
                simulation_result = self.dealer_result()
            if simulation_result<=21:
                legal_results.append(simulation_result)
            else:
                lost_count+=1
        return np.mean(legal_results),lost_count, lost_count/iterations, (1-lost_count/iterations)*np.mean(legal_results)
