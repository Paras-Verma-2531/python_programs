class programmer:
    company = "microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def details(self):
        print(
            f"the name of programmer is {self.name} and his product is {self.product}")
paras = programmer("paras", "github")
harry = programmer("harry", "youtube")
paras.details()
harry.details()
