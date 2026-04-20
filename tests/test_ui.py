# from playwright.sync_api import Page
# import pytest

# def test_open_saucedemo(page: Page):
#     # Go to saucedemo
#     page.goto("https://www.saucedemo.com")

#     page.fill("#user-name","standard_user")
#     page.fill("#password","secret_sauce")
#     page.click("#login-button")

#     assert page.locator(".title").inner_text()=="Products"
#     assert "inventory" in page.url
    
#     # Check title
    
# def test_login_failed(page:Page):
#     page.goto("https://www.saucedemo.com")

#     page.fill("#user-name","WrongUser")
#     page.fill("#password","Wrongpassword")

#     page.click("#login-button")

#     error=page.locator("[data-test='error']")
#     assert error.is_visible()
 
# def test_login_locked_out(page:Page):
#     page.goto("https://www.saucedemo.com")

#     page.fill("#user-name","locked_out_user")
#     page.fill("#password","secret_sauce")

#     page.click("#login-button")

#     error=page.locator("[data-test='error']")
#     assert error.is_visible()
#     assert "locked out" in error.inner_text().lower()

## Using POM
from playwright.async_api import Page
from pages.login_page import Login
from pages.inventory_page import Inventory
def test_success_login(page:Page):
    login=Login(page)
    login.goto()
    login.login("standard_user","secret_sauce")
    assert "inventory" in page.url
    assert login.get_page_title()=="Products"

def test_login_failed(page:Page):
    login=Login(page)
    login.goto()
    login.login("Wrongusername",'WrongPassword')
    assert "Epic sadface" in login.get_error_messege()
def test_locked_out_user(page:Page):
    login=Login(page)
    login.goto()
    login.login("locked_out_user","secret_sauce")
    assert "locked out" in login.get_error_messege()

def test_inventory_page(logged_in_user):
    

    inventory=Inventory(logged_in_user)
    assert inventory.get_title()=="Products"
    assert inventory.get_item_count()==6
    inventory.add_item_to_cart()
    assert inventory.get_cart_count()=="1"
    
    inventory.go_to_cart()
    assert "cart" in logged_in_user.url
    
    
    

