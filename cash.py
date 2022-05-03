from typing import Dict, List

denomintations = {
    'quarter': 25,
    'dimes': 10,
    'nickels': 5,
    'pennies': 1
}
# 1 dolar equals 100 pennies coin or 20 nickels coins or 10 dimes coins or 4 quartes coins

class Cash:

    def __init__(self, mount: float):
        self.mount = mount

    @classmethod
    def review(cls, values, change ) -> Dict:
        new_dict = values.copy()
        denomitations_over: List[str] = []
        for k, v in new_dict.items():
            coins_by_denonation = round(change/v, 2)
            
            # if the value of denomitation by change greather than 1 and 
            # this values greather than change then this denomitadion over the change
            if coins_by_denonation > 1 and (v * 2) > change:
                denomitations_over.append(k)
            else:
                if coins_by_denonation >= 1:
                    new_dict[k] = coins_by_denonation
        for denomination in denomitations_over:
            del new_dict[denomination]
        return new_dict

    # in this functions the progaman calculates the change owed to some user
    # 
    def calculate_change(self) -> int:
        mounts: List[float] = []
        
        change = float(self.mount)
        
        # convert the dollars to cents even the fraction dolar
        change = change * 100
        #other_dictionary = {k: float(f'{round(change/v, 2)}') for k, v in denomintations.items()}
        results = self.review(denomintations, change)
        #print(results)
        return int(min(results.values()))



def entrance_is_rigth(entrance: str) -> bool:
    try: 
        number = float(entrance)
        # To user entrance increments 10 times due to sometimes the user types numbers like 0.4
        # 0.4 is a positve number althoug lower than zero
        return (number * 10) > 0
    except ValueError:
        return False


if __name__ == '__main__':
    rigth_entrance: bool = False
    while not rigth_entrance:
        mount = input("Change owed: ")
        if entrance_is_rigth(mount):
            cash = Cash(mount)
            change = cash.calculate_change()
            print(change)
            print()
            rigth_entrance = True