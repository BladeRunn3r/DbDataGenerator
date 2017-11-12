def generate_users(user_type, rows):
    import random
    from pyfaker import Fake

    de_faker = Fake(lang_code='de')
    pl_faker = Fake(lang_code='pl')

    def get_user_name():
        if randomed_country is 'Poland':
            random_name = pl_faker.Name.name()
            if 'Pan' in random_name or 'Pani' in random_name:
                name_wo_title = random_name.split(' ', 1)[1]
                return name_wo_title
            else:
                return random_name

        elif randomed_country is 'Germany':
            random_name = de_faker.Name.name()
            if 'Prof. Dr.' in random_name:
                return random_name[10:]
            elif 'Fr.' in random_name or 'Hr.' in random_name or 'Dr.' in random_name:
                return random_name[4:]
            else:
                return random_name
    
    def get_user_city():
        if randomed_country is 'Poland':
            random_city = pl_faker.Address.city()
        elif randomed_country is 'Germany':
            random_city = de_faker.Address.city()
        return random_city

    def get_user_street():
        if randomed_country is 'Poland':
            random_address = pl_faker.Address.street_address()
        elif randomed_country is 'Germany':
            random_address = de_faker.Address.street_address()
        if "'" in random_address:
            return get_user_street()
        else:        
            return random_address

    def get_company_name():
        import csv
        with open('companies.csv', 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            csvFileArray = []
            for row in reader:
                csvFileArray.append(row) # gets list of lists from csv
            random_company = csvFileArray[random.randint(0, len(csvFileArray))] # randoms a company 
            return "'" + random_company[1] + "'" # returns company name


    seller_types = ['company', 'individual', 'tradesman']
    client_types = ['company', 'individual']

    if user_type == 'client':
        file = open('clients.sql', 'w')
    elif user_type == 'seller':
        file = open('sellers.sql', 'w')

    for _ in range(rows):

        countries = ['Poland', 'Germany']    
        randomed_country = random.choice(countries)

        single_insert_string = ''

        if user_type == 'client':
            randomed_user_type = random.choice(client_types)
            single_insert_string += 'INSERT INTO client' + \
                '(full_name, country, city, street, client_type, company_name) VALUES('

        elif user_type == 'seller':
            randomed_user_type = random.choice(seller_types)
            if randomed_user_type is not 'company':
                randomed_user_type = 'null'
            single_insert_string += 'INSERT INTO seller' + \
                '(full_name, country, city, street, seller_type, company_name) VALUES('

        single_insert_string += "'" + get_user_name() + "'" + ', ' + \
            "'" + randomed_country + "'" + ', ' + \
            "'" + get_user_city() + "'" + ', ' + \
            "'" + get_user_street() + "'" + ', ' + \
            "'" + randomed_user_type + "'" + ', '

        if randomed_user_type is 'company':
            single_insert_string += get_company_name()
        else:
            single_insert_string += 'null'
        single_insert_string += ');\n'
        print(single_insert_string)
        file.write(single_insert_string)
    file.close()

generate_users('client', 50)
generate_users('seller', 50)