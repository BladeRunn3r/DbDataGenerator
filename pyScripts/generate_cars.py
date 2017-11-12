def generate_cars(rows):
    import random

    def get_car():
        import csv
        with open('cars.csv', 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            csvFileArray = []
            for row in reader:
                csvFileArray.append(row) # gets list of lists from csv
            random_car = csvFileArray[random.randint(0, len(csvFileArray))]
            # randoms a car (single list containing brand and model)
            return random_car

    regions = ['dolnośląskie', 'kujawsko-pomorskie', 'lubelskie',
        'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie', 'opolskie',
        'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie',
        'warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie',
        'Baden-Württemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen',
        'Hamburg', 'Hesse', 'Lower Saxony', 'Mecklenburg-Vorpommern',
        'North Rhine-Westphalia', 'Rhineland-Palatinate', 'Saarland',
        'Saxony', 'Saxony-Anhalt', 'Schleswig-Holstein', 'Thuringia']

    file = open('cars.sql', 'w')
    for _ in range(rows):
        fetched_car = get_car()
        single_insert_string = 'INSERT INTO car' + \
        '(car_brand, car_model, car_region, production_year, mileage, ' + \
        'price, engine_capacity, engine_power, gearbox_type, car_drive, ' + \
        'car_body_color, car_body_type, car_cover, fuel_type, number_of_doors) VALUES('
        single_insert_string += "'" + fetched_car[0] + "'" + ', ' + \
            "'" + fetched_car[1] + "'" + ', ' + \
            "'" + random.choice(regions) + "'" + ', ' + \
            str(random.randint(1979, 2016)) + ', ' + \
            str(random.randrange(0, 400000, 500)) + ', ' + \
            str(random.randrange(0, 200000, 250)) + ', ' + \
            get_car_features() + ');\n'
        # max year set to 2016 to prevent situation when car is sold before it's actually produced
        print(single_insert_string)
        file.write(single_insert_string)
    file.close()

def get_car_features():
    import random

    gearboxes = ['automatic', 'manual']
    drive_types = ['4x4', 'front', 'rear']
    body_colors = ['white', 'brown', 'black',
        'red', 'graphite', 'navy blue', 'blue', 'orange',
        'silver', 'grey', 'green', 'yellow', 'gold']
    body_types = ['SUV', 'coupe', 'dual cowl', 'fastback',
        'hatchback', 'cabriolet', 'combo', 'liftback',
        'limousine', 'microvan', 'minivan', 'pick-up',
        'roadster', 'sedan', 'targa', 'van']
    cover_types = ['metallic', 'pearl', 'mat', 'acrylic', 'nonmetallic']
    fuel_types = ['petrol', 'diesel', 'electric', 'ethanol',
        'hybrid', 'hydrogen', 'petrol + LPG', 'petrol + CNG']
    nof_doors = ['2/3', '4/5']

    features_string = str(round(random.uniform(1.0, 5.0), 1)) + ', ' + \
        str(random.randint(45, 500)) + ', ' + \
        "'" + random.choice(gearboxes) + "'" + ', ' + \
        "'" + random.choice(drive_types) + "'" + ', ' + \
        "'" + random.choice(body_colors) + "'" + ', ' + \
        "'" + random.choice(body_types) + "'" + ', ' + \
        "'" + random.choice(cover_types) + "'" + ', ' + \
        "'" + random.choice(fuel_types) + "'" + ', ' + \
        "'" + random.choice(nof_doors) + "'"
    return features_string

generate_cars(50)