class Product:
    '''
    Class representing a product in an online shopping cart, storing
    description, price and stock level.
    '''

    def __init__(self, description: str, price: float, stock: int):
        # initialise the three private instance variables
        self._description = description
        self._price = price
        self._stock = stock

    # define three getter methods returning their instance variable values
    def getDescription(self):
        return self._description

    def getPrice(self):
        return self._price

    def getStock(self):
        return self._stock

    # define two setter methods updating their respective instance variable values
    def setDescription(self, text):
        self._description = text

    def setPrice(self, amount):
        self._price = amount

    def updateStock(self, amount):
        '''
        Takes a positive or negative value, checks it against the current
        stock, ensuring it will not go below zero, before adding it to the
        stock value. Returns True if stock was updated, False if not.
        '''
        # validate that amount is an integer
        if not isinstance(amount, int):
            raise TypeError('amount must be an integer')

        # update stock only if it won't go below zero
        if self._stock + amount < 0:
            return False
        else:
            self._stock += amount
            return True


class CartItem:
    """
    A class modelling a product and the quantity required for purchase,
    and calculating the total cost for that quantity.
    """

    def __init__(self, product: Product, quantity: int):
        # initialise the two private attributes
        self._product = product   # referencing the Product class to use its methods
        self._quantity = quantity

    # two getter methods returning their respective values
    def getProduct(self):
        return self._product

    def getQuantity(self):
        return self._quantity

    def getTotalPrice(self):
        # calculate price * quantity using the product's own getPrice method
        return self._product.getPrice() * self._quantity


class ShoppingCart:
    '''
    A class modelling a collection of CartItems, which can be added or
    removed after appropriate checking of the referenced product stock.
    '''

    def __init__(self):
        # instance variable: an empty list that will hold CartItem objects
        self._items = []

    def getItems(self):
        # return the list of CartItem objects currently in the cart
        return self._items

    def addItem(self, product, quantity):
        # check if product has enough stock and then update it accordingly by deducting
        if quantity <= product.getStock():
            product.updateStock(-quantity)
            self._items.append(CartItem(product, quantity))
            return True
        else:
            return False

    def removeItem(self, product):
        # search the list of CartItems to find the matching product
        for item in self._items:
            if item.getProduct() == product:
                # update the stock using this item's own quantity
                product.updateStock(item.getQuantity())
                # remove the matching CartItem from the items list
                self._items.remove(item)
                # return True since the product was found and updated
                return True
        # return False if no matching product was found
        return False

    def getCartTotal(self):
        # return the sum of all the CartItem totals in the cart
        total = 0
        for item in self._items:
            total += item.getTotalPrice()
        return total