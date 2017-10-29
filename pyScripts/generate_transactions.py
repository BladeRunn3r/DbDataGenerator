def generate_transactions(rows, cars_number, clients_number, sellers_number): 
    #depends on cars number; car can be sold once, so rows <= cars
    if (rows > cars_number):
        print('error, rows number must be <= cars number')
        return

    import random
    already_sold_cars_ids = []
    entry_car_ids = list(range(1, cars_number + 1))

    def get_car_id(): # not to sell same car multiple times
        available_car_ids = list(set(entry_car_ids) - set(already_sold_cars_ids))
        randomed_car_id = random.choice(available_car_ids)
        already_sold_cars_ids.append(randomed_car_id)
        return randomed_car_id

    def get_date():

        def get_month():
            month = random.randint(1, 12)
            if (month < 10):
                month = '0' + str(month)
                return month
            else:
                return str(month)

        def get_day(of_month, of_year):
            longer = ['01', '03', '05', '07', '08', '10', '12']
            shorter = ['04', '06', '09', '11']
            if of_month in longer:
                day = random.randint(1, 31)
            elif of_month in shorter:
                day = random.randint(1, 30)
            else:
                day = random.randint(1, 29) if of_year == '2016' else random.randint(1, 28)
            if (day < 10):
                day = '0' + str(day)
                return day
            else:
                return str(day)

        year = str(random.randint(2016, 2017))
        month = get_month()
        date_string = 'TO_DATE(' + "'" + year + '/' + month + '/' + get_day(month, year) + "'" + ','
        date_string += "'yyyy/mm/dd'" + ')'
        return date_string

    file = open('transactions.sql', 'w')
    for _ in range(rows):
        single_insert_string = 'INSERT INTO car_transaction(car_id, client_id, seller_id, transaction_date) VALUES('
        single_insert_string += \
            str(get_car_id()) + ', ' + \
            str(random.randint(1, clients_number)) + ', ' + \
            str(random.randint(1, sellers_number)) + ', ' + \
            get_date() + ');\n'
        print(single_insert_string)
        file.write(single_insert_string)
    file.close()

generate_transactions(50, 50, 25, 25)
