from faker import Faker
from random import choice, randint, uniform
from server.infrastructure.db import Base, engine, SessionLocal
from server.infrastructure.models_db import VehicleDB

fake = Faker('pt_BR')

brands_models = {
    "Toyota": ["Corolla", "Hilux", "Yaris", "Etios"],
    "Honda": ["City", "Fit", "Civic", "Accord", "HR-V", "CR-V"],
    "Volkswagen": ["Polo", "Gol", "Golf", "Nivus", "T-Cross", "Taos", "Virtus"],
    "Chevrolet": ["Onix", "Tracker", "Equinox", "Onix Plus"],
    "Hyundai": ["HB20", "HB20S", "Creta", "Santa Fé", "Tucson"],
    "BYD": ["Dolphin Mini", "Dolphin", "Song", "Song Pro"],
    "FIAT": ["Mobi", "Argo", "Cronos", "Pulse", "Fastback"]
}

fuel_types = ["Gasoline", "Flex", "Diesel", "Electric"]
transmissions = ["MT", "AT"]
colors = ["Silver", "Black", "White", "Red", "Blue", "Grey"]

def generate_vehicle():
    brand = choice(list(brands_models.keys()))
    model = choice(brands_models[brand])

    if brand == "BYD":
        fuel_type = "Electric"
        transmission = "AT"
        ac = True
    else:
        fuel_type=choice(fuel_types)
        transmission=choice(transmissions)
        ac = choice([True,False])

    return VehicleDB(
        brand = brand,
        model = model,
        fuel_type = fuel_type,
        manufacture_year = randint(2018,2025),
        color = choice(colors),
        mileage = randint(1000, 120000),
        doors = choice([2,4]),
        transmission = transmission,
        ac = ac,
        price = round(uniform(60000,250000), 2)
    )

def populate_db(n=100):
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    for _ in range(n):
        vehicle = generate_vehicle()
        session.add(vehicle)
    
    session.commit()
    session.close()

if __name__ == "__main__":
    populate_db()