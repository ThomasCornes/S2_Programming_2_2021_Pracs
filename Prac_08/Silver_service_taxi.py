from Prac_08.Taxi import Taxi

class silver_service_taxi(Taxi):
    flagfall= 4.5

    def __init__(self, name, fuel, fanciness):
        super().init(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness


    def __str__(self):
        return "{} flagfall  of ${:.2f}".format(super().__str__(),self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()
