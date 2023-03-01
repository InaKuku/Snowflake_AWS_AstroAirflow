class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            if customer not in self.customers:
                self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for cus in self.customers:
            if cus.id == customer_id:
                for a_rented_dvd in cus.rented_dvds:
                    if a_rented_dvd.id == dvd_id:
                        return f"{cus.name} has already rented {a_rented_dvd.name}"
                for dv in self.dvds:
                    if dv.id == dvd_id:
                        if dv.is_rented:
                            return "DVD is already rented"
                        else:
                            if cus.age >= dv.age_restriction:
                                dv.is_rented = True
                                cus.rented_dvds.append(dv)
                                return f"{cus.name} has successfully rented {dv.name}"
                            else:
                                return f"{cus.name} should be at least {dv.age_restriction} to rent this movie"


    def return_dvd(self, customer_id, dvd_id):
        for cus in self.customers:
            if cus.id == customer_id:
                for a_rented_dvd in cus.rented_dvds:
                    if a_rented_dvd.id == dvd_id:
                        a_rented_dvd.is_rented = False
                        cus.rented_dvds.remove(a_rented_dvd)
                        return f"{cus.name} has successfully returned {a_rented_dvd.name}"
                else:
                    return f"{cus.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for a_cust in self.customers:
            if not self.customers.index(a_cust) == len(self.customers) - 1:
                result += f"{a_cust}\n"
            else:
                if len(self.dvds) > 0:
                    result += f"{a_cust}\n"
                else:
                    result += f"{a_cust}"
        for a_dvd in self.dvds:
            if not self.dvds.index(a_dvd) == len(self.dvds) - 1:
                result += f"{a_dvd}\n"
            else:
                result += f"{a_dvd}"
        return result







