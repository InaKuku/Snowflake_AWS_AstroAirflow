class Customer:
    customer_id = 0

    def __init__(self, name: str, address: str, email: str):
        Customer.customer_id += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.customer_id
        
    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


