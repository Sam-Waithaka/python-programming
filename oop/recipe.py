class Recipe():
    def __init__(self, dish, item, time) -> None:
        self.dish = dish
        self.item = item
        self.time = time


    def content(self):
        print('the' + self.dish + 'has' + str(self.item)+ \
              ' and takes', + str(self.time) + 'minutes to prepare')
        
pizza = Recipe('Pizza', ['cheese', 'bread', 'tomato'], 45)
pasta = Recipe('Pasta', ['penne', 'sauce'], 55) 

print(pizza.item)
print(pasta.item)

print(pizza.content())