class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                return pr

    def remove(self, product_name):
        for pr in self.products:
            if pr.name == product_name:
                self.products.remove(pr)

    def __repr__(self):
        result = [f"{p.name}: {p.quantity}" for p in self.products]
        return '\n'.join(result)
        # result = ""
        # for prd in self.products:
        #     if not prd == self.products[-1]:
        #         result += f"{prd.name}: {prd.quantity}\n"
        #     else:
        #         result += f"{prd.name}: {prd.quantity}"
        # return result