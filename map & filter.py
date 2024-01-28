menu = ['espresso',  'cappuccino', 'mocha', 'macchiato', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# map_cofffee = map(find_coffee, menu)

# print(map_cofffee)

# for x in map_cofffee:
#     print(x)
    
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)
    