# Consumer class amd its subclass
class Consumer:
    def __init__(self, name, items, cost):
        self.name = name
        self.items = items
        self.cost = cost


class member(Consumer):
    def __init__(self, memberNumber, nights, totalspent, address, email):
        self.memberNumber = memberNumber
        self.nights = nights
        self.totalSpent = totalspent
        self.address = address
        self.email = email
        setStatus(self)

    def setStatus(self):
        if self.nights > 25:
            self.status = "gold"
        if self.nights > 50:
            self.status = "titanium"
        if self.nights > 75 & self.totalSpent > 10000:
            self.status = "Ambassador"
