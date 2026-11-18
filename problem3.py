stock = {"paracetamol": 20, "vitamin C": 5, "bandage": 12}
def sell(stock, item, amount):
    if item not in stock:
        return "not sold here"
    elif item in stock and stock[item]<amount:
        return "not enough"
    else:
        stock[item]-=amount
        return "sold"
def restock(stock, item, amount):
    current = stock.get(item, 0)
    stock[item] = current + amount
orders = [["paracetamol", 3], ["bandage", 15], ["aspirin", 2], ["vitamin C", 5]]
for order in orders:
    

