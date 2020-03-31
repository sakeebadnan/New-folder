

price_list = {
    'internet_connection': {
        'name': 'Internet Connection',
        'price': 200,
        'regularity': 'monthly'
    },
    'phone_line': {
        'name': 'Phone Line',
        'price': 150,
        'regularity': 'monthly'
    },
    'motorola_G99': {
        'name': 'Motorola G99',
        'price': 800,
        'regularity': 'once'
    },
    'iphone_99': {
        'name': 'iPhone 99',
        'price': 6000,
        'regularity': 'once'
    },
    'samsung_galaxy_99': {
        'name': 'Samsung Galaxy 99',
        'price': 1000,
        'regularity': 'once'
    },
    'sony_xperia_99': {
        'name': 'Sony Xperia 99',
        'price': 900,
        'regularity': 'once'
    },
    'huawei_99': {
        'name': 'Huawei 99',
        'price': 900,
        'regularity': 'once'
    },
}


class Purchase():

    internet_connection = False
    phone_lines = 0
    cell_phones = []
    price = 0

    def get_price(self, service_name):
        service = price_list.get(service_name)
        return service['price']

    def get_name(self, service_name):
        service = price_list.get(service_name)
        return service['name']

    def in_ex_internet_conn(self, with_int):
        # TODO: test type of with_int
        if with_int and not self.internet_connection:
            self.price += self.get_price('internet_connection')
            self.internet_connection = True
        else:
            self.price -= self.get_price('internet_connection')
            self.internet_connection = False

        return self.price

    def increment_phn_line(self):
        self.price += self.get_price('phone_line')
        self.phone_lines += 1
        return self.price

    def decrementing_phn_line(self):
        self.price -= self.get_price('phone_line')
        self.phone_lines -= 1
        return self.price

    def select_cell_phn(self, phn_model):
        if phn_model not in self.cell_phones:
            self.cell_phones.append(phn_model)
            self.price += self.get_price(phn_model)
        return self.price

    def unselect_cell_phn(self, phn_model):
        if phn_model in self.cell_phones:
            self.cell_phones.remove(phn_model)
            self.price -= self.get_price(phn_model)
        return self.price

    def purchase(self):
        msg = "Items you are buying:\n"
        if self.internet_connection:
            msg += "{} \t {}\n".format(
                self.get_name('internet_connection'),
                self.get_price('internet_connection')
                )
        if self.phone_lines > 0:
            msg += "{}x{} \t {}\n".format(
                    self.phone_lines,
                    self.get_name('phone_line'),
                    self.get_price('phone_line')*self.phone_lines
                    )
        if len(self.cell_phones) > 0:
            for cell_phone in self.cell_phones:
                msg += "1x{} \t {}\n".format(
                        self.get_name(cell_phone),
                        self.get_price(cell_phone)
                        )
        msg += "Total price \t: {} DKK\n".format(self.price)

        return msg
