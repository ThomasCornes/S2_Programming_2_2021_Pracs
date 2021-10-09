from Prac_08.Silver_service_taxi import silver_service_taxi

def main():
    taxi = silver_service_taxi("Test Fancy Taxi",100,2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())
