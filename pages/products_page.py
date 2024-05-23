# from selenium.webdriver.common.by import By
# from base_page import BasePage

# class ProductsPage(BasePage):
#     # Locators for elements on the products page
#     PRODUCT_CARD = (By.CLASS_NAME, "product-image-wrapper")
#     ADD_TO_CART_BUTTON = (By.XPATH, ".//a[contains(@class, 'add-to-cart')]")
#     MODAL = (By.ID, "cartModal")
#     VIEW_CART_LINK = (By.XPATH, "//a[contains(@href, '/view_cart')]")
#     CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")

#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver.get("https://www.automationexercise.com/products")

#     def add_product_to_cart(self, product_index):
#         """Click the 'Add to Cart' button for a specific product"""
#         product_cards = self.driver.find_elements(*self.PRODUCT_CARD)
#         if product_index < len(product_cards):
#             add_to_cart_button = product_cards[product_index].find_element(*self.ADD_TO_CART_BUTTON)
#             add_to_cart_button.click()
#             self.wait.until(EC.visibility_of_element_located(self.MODAL))
#         else:
#             raise IndexError(f"Product with index {product_index} not found")

#     def continue_shopping(self):
#         """Close the modal and continue shopping"""
#         continue_shopping_button = self.find_element(*self.CONTINUE_SHOPPING_BUTTON)
#         continue_shopping_button.click()
#         self.wait.until(EC.invisibility_of_element_located(self.MODAL))

#     def view_cart(self):
#         """Click on the 'View Cart' link in the modal"""
#         view_cart_link = self.find_element(*self.VIEW_CART_LINK)
#         view_cart_link.click()
