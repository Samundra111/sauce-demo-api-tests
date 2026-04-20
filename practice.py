# products=['laptop','mouse','keyboard']

# print(products[1])


# userdata={
#     'username':"samundra",
#     'password':"12345678",
#     'attempts':4
# }

# print(userdata['username'])
# userdata['attempts']=4
# print(userdata)

# products=['laptop','mouse','keyboard']

# for product in products:
#     print(f" testing product: {product}")

# error_messeges=['Invalid Password','User not found',"Server Error"]

# for error_msg in error_messeges:
#     if error_msg=="Server Error":
#         print("Critical Failure")
#     else:
#         print("Minor error found")


# test_results=[
#     {'test_name':"Login","Status":"fail"},
#     {'test_name':"register","Status":"pass"},
#     {'test_name':"checkout","Status":"pass"}
# ]

# def count_failures(test_resuslt):
#     count=0
#     for items in test_results:
#         if items['Status']=="fail":
#             count=count+1
#         return count
    
# total=count_failures(test_results)
# print(total)

       

class SauceCart:
    def __init__(self):
        self.items=[]
    def add_items(self,item_name):
        self.items.append(item_name)
    def get_items_len(self):
        return len(self.items)

sc=SauceCart()
sc.add_items("iphone")
sc.add_items("Samsung")
sc.add_items("Oppo")
length=sc.get_items_len()
print(length)

    
class BaseTest:
    def __init__(self):
        self.tester_name="Samundra"
    def log_action(self,action):
        print(f"{self.tester_name}is {action}")

class LoginTest(BaseTest):
    def __init__(self,browser_name):
        super().__init__()
        self.browser_name=browser_name
    def test_valid_login(self):
        self.log_action("Entering credentials")
        print("Login successful")

lt=LoginTest("Chrome")
lt.test_valid_login()

