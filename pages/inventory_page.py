class Inventory:
    def __init__(self,page):
        self.page=page
        self.title=page.locator(".title")
        self.inventory_items=page.locator(".inventory_item")
        self.cart_icon=page.locator(".shopping_cart_link")
        self.menu_btn=page.locator("#react-burger-menu-btn")
        self.cart_count = page.locator(".shopping_cart_badge")
    def get_title(self):
        return self.title.inner_text()
    def get_item_count(self):
        return self.inventory_items.count()
    def add_item_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-bike-light").click()
    def go_to_cart(self):
        self.cart_icon.click()
    def get_cart_count(self):
        return self.cart_count.inner_text()