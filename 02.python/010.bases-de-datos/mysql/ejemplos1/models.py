class Staff:
    def __init__(self, staff_id, first_name, last_name, address_id, picture, email, store_id, active, username,
                 password, last_update):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id
        # self.picture = picture
        self.email = email
        self.store_id = store_id
        self.active = active
        self.username = username
        self.password = password
        self.last_update = last_update

    def __str__(self):
        return self.first_name + " " + self.last_name

