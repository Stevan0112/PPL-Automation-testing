from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object untuk halaman Inventory SauceDemo."""

    # =========================================================
    # LOCATORS (RELATIVE XPATH)
    # =========================================================

    # Tombol Add to Cart untuk produk Sauce Labs Backpack
    ADD_BACKPACK_BUTTON = (
        By.XPATH,
        "//button[contains(@data-test, 'add-to-cart-sauce-labs-backpack')]"
    )

    # Ikon keranjang belanja dan badge jumlah produk
    CART_BADGE = (
        By.XPATH,
        "//a[contains(@class, 'shopping_cart_link')]//span[contains(@class, 'shopping_cart_badge')]"
    )

    # Tombol Burger Menu
    BURGER_MENU_BUTTON = (
        By.XPATH,
        "//button[@id='react-burger-menu-btn']"
    )

    # Opsi Logout pada sidebar
    LOGOUT_LINK = (
        By.XPATH,
        "//a[@id='logout_sidebar_link']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # =========================================================
    # METHODS
    # =========================================================

    def add_backpack_to_cart(self):
        """Menambahkan produk Sauce Labs Backpack ke keranjang."""
        self.click(self.ADD_BACKPACK_BUTTON)

    def get_cart_badge_count(self) -> str:
        """Mengambil jumlah produk yang ditampilkan pada badge keranjang."""
        return self.get_text(self.CART_BADGE)

    def logout(self):
        """Membuka burger menu dan melakukan logout."""
        self.click(self.BURGER_MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
