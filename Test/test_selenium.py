import unittest
from selenium import webdriver


class TestPrueba(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("chromedriver")

    def tearDown(self):
        self.browser.close()

    def test_texto_barra_busqueda_despues_de_buscar(self):
        self.browser.get("https://www.google.com")
        #name="q"
        barra_busqueda = self.browser.find_element_by_name("q")
        barra_busqueda.send_keys("django docs")
        #name="btnK
        boton_buscar = self.browser.find_element_by_name("btnK")
        #sleep(5)
        self.browser.implicitly_wait(5)
        boton_buscar.click()   

        barra_busqueda = self.browser.find_element_by_name("q")
        texto = barra_busqueda.get_property("value")
        self.assertEqual(texto, "django docs")

if __name__ == "__main__":
    unittest.main()
