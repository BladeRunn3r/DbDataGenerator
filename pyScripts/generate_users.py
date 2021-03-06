import csv
with open('companies.csv', 'rt', encoding='utf8') as f:
    reader = csv.reader(f)
    csvFileArray = []
    for row in reader:
        csvFileArray.append(row) # gets list of lists from csv

def generate_users(user_type, rows):
    import random
     
    def get_client_name():
        from pyfaker import Fake
        fake = Fake(lang_code='pl')
        random_name = fake.Name.name()
        print(random_name)
        if 'Pan' in random_name or 'Pani' in random_name and not 'Pankracy' in random_name and not 'Pantaleon' in random_name:
            name_wo_title = random_name.split(' ', 1)[1]
            return name_wo_title
        else:
            return random_name

    def get_company_name():

            random_company = csvFileArray[random.randint(0, len(csvFileArray) - 1)] # randoms a company 
            return "'" + random_company[1] + "'" # returns company name


    seller_types = ['company', 'individual', 'tradesman']
    client_types = ['company', 'individual']

    if user_type == 'client':
        file = open('clients.sql', 'w')
    elif user_type == 'seller':
        file = open('sellers.sql', 'w')

    for _ in range(rows):
        single_insert_string = ''

        if user_type == 'client':
            randomed_user_type = random.choice(client_types)
            single_insert_string += 'INSERT INTO client(full_name, client_type, company_name) VALUES('

        elif user_type == 'seller':
            randomed_user_type = random.choice(seller_types)
            if randomed_user_type is not 'company':
                randomed_user_type = 'null'
            single_insert_string += 'INSERT INTO seller(full_name, seller_type, company_name) VALUES('

        single_insert_string += "'" + get_client_name() + "'" + ', ' + \
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