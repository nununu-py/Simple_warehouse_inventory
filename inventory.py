import json
import os


class Inventory:

    def __init__(self):
        self.stock = {
            "stock": []
        }

    def view_stock(self):
        try:
            with open("stock_data.json", mode="r") as file:
                view_data = json.load(file)
                print(view_data)
        except FileNotFoundError:
            print("No Exist Data")

    def add_new_stock(self):
        try:
            with open("stock_data.json", mode="r") as file:
                json.load(file)
        except FileNotFoundError:
            product_code = input("Insert a unique product key : ").lower()
            product_name = input("Insert a product name : ").title()
            product_desc = input("Insert a product description : ").title()
            product_stock = input("Insert a product stock : ")
            product_price = input("Insert a product price : ")
            product_data = {
                "product_code": product_code,
                "product_name": product_name,
                "product_desc": product_desc,
                "product_stock": product_stock,
                "product_price": product_price
            }

            self.stock["stock"].append(product_data)

            with open("stock_data.json", "w") as file:
                json.dump(self.stock, file, indent=4)
        else:

            product_code = input("Insert a unique product key : ").lower()
            product_name = input("Insert a product name : ").title()
            product_desc = input("Insert a product description : ").title()
            product_stock = input("Insert a product stock : ")
            product_price = input("Insert a product price : ")
            product_data = {
                "product_code": product_code,
                "product_name": product_name,
                "product_desc": product_desc,
                "product_stock": product_stock,
                "product_price": product_price
            }

            with open("stock_data.json", "r+") as file:
                json_data = json.load(file)
                json_data["stock"].append(product_data)
                file.seek(0)
                json.dump(json_data, file, indent=4)

    def search_stock(self, product_code_input):
        search_data = {}
        with open("stock_data.json", "r") as file:
            json_data = json.load(file)

            for data in json_data["stock"]:
                for product_code in data:
                    if data[product_code] == product_code_input:
                        search_data = data
                        break

        return search_data

    def delete_stock(self, product_code_input):
        data_selected = self.search_stock(product_code_input)

        with open("stock_data.json", mode="r+") as file:
            json_file = json.load(file)
            for index_file in range(0, len(json_file["stock"])):
                if data_selected == json_file["stock"][index_file]:
                    del json_file["stock"][index_file]
                    print("Data Is Remove")
                    break
        os.remove("stock_data.json")

        with open("stock_data.json", mode="w") as new_file:
            json.dump(json_file, new_file, indent=4)

    def update_stock(self, product_code_input):
        data_selected = self.search_stock(product_code_input)

        with open("stock_data.json", "r+") as file:
            json_file = json.load(file)

            for index_file in range(0, len(json_file["stock"])):
                if data_selected == json_file["stock"][index_file]:
                    new_product_code = input("Insert a unique product key : ").lower()
                    new_product_name = input("Insert a product name : ").title()
                    new_product_desc = input("Insert a product description : ").title()
                    new_product_stock = input("Insert a product stock : ")
                    new_product_price = input("Insert a product price : ")
                    product_data = {
                        "product_code": new_product_code,
                        "product_name": new_product_name,
                        "product_desc": new_product_desc,
                        "product_stock": new_product_stock,
                        "product_price": new_product_price
                    }
                    data_selected = product_data
                    print(data_selected)
                    json_file["stock"][index_file] = data_selected
                    print("Data Is Update")
                    break
                else:
                    print("Invalid Product Code Input")

        os.remove("stock_data.json")

        with open("stock_data.json", mode="w") as new_file:
            json.dump(json_file, new_file, indent=4)


class User(Inventory):
    def __init__(self):
        super().__init__()

    def view_stock(self):
        super().view_stock()

    def search_stock(self, product_code_input):
        print(super().search_stock(product_code_input))


# Inventory Administrator
# my_stock = Inventory()
# my_stock.view_stock()
# my_stock.add_new_stock()
# my_stock.view_stock()
# print(my_stock.search_stock(input("insert a product code : ")))
# my_stock.update_stock(input("insert a product code : "))
# my_stock.delete_stock((input("insert a product code : ")))

# USER
# user = User()
# user.view_stock()
# user.search_stock(input("insert a product code : "))
