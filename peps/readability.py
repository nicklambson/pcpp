# not readable, not good

def f(i):
    l = i + (0.08 * i)
    return l


# much more readable, much better
# Calculates the gross price of products in Wonderland.

def calculate_gross_price(net_price):
    gross_price = net_price + (0.08 * net_price)
    return gross_price