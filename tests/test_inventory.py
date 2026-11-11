import pytest
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    """Kumpulan kasus uji fungsional fitur Inventory SauceDemo."""

    def test_add_backpack_to_cart(self, driver):
        """
        TC-04: Verifikasi penambahan produk Backpack ke keranjang.

        Expected:
        Badge keranjang belanja menampilkan angka 1.
        """

        # 1. Arrange: Membuat objek Page Object
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        # 2. Act: Login menggunakan standard_user
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Menunggu hingga halaman inventory berhasil dibuka
        expected_inventory_url = (
            "https://www.saucedemo.com/inventory.html"
        )
        login_page.wait.until(
            EC.url_to_be(expected_inventory_url)
        )

        # 3. Act: Menambahkan Backpack ke keranjang
        inventory_page.add_backpack_to_cart()

        # 4. Assert: Memeriksa jumlah produk pada cart badge
        expected_count = "1"
        actual_count = inventory_page.get_cart_badge_count()

        assert actual_count == expected_count, (
            f"Jumlah produk tidak sesuai. "
            f"Diharapkan: '{expected_count}', "
            f"Diterima: '{actual_count}'"
        )

    def test_logout_from_inventory(self, driver):
        """
        TC-05: Verifikasi proses logout dari halaman Inventory.

        Expected:
        Pengguna kembali ke halaman login SauceDemo
        dan tombol Login kembali ditampilkan.
        """

        # 1. Arrange: Membuat objek Page Object
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        # 2. Act: Login menggunakan standard_user
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Menunggu hingga halaman inventory berhasil dibuka
        expected_inventory_url = (
            "https://www.saucedemo.com/inventory.html"
        )
        login_page.wait.until(
            EC.url_to_be(expected_inventory_url)
        )

        # 3. Act: Melakukan logout
        inventory_page.logout()

        # 4. Assert 1: Memeriksa URL setelah logout
        expected_login_url = "https://www.saucedemo.com/"

        login_page.wait.until(
            EC.url_to_be(expected_login_url)
        )

        actual_url = login_page.get_current_url()

        assert actual_url == expected_login_url, (
            f"URL setelah logout tidak sesuai. "
            f"Diharapkan: '{expected_login_url}', "
            f"Diterima: '{actual_url}'"
        )

        # 5. Assert 2: Memastikan tombol Login kembali tampil
        assert login_page.find_element(
            LoginPage.LOGIN_BUTTON
        ).is_displayed() is True, (
            "Tombol Login tidak tampil setelah proses logout!"
        )
