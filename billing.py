class Billing:

    def __init__(self, nights: int):
        self.price_per_night = 100
        self.nights = nights

    def total_amount(self):
        return self.price_per_night * self.nights