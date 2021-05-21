import unittest
from empresa import Empleado


class TestEmpleado(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def setUp(self):
        print("setup")
        self.emp1 = Empleado("axel", "perez", 5000)
        self.emp2 = Empleado("sandra", "rodriguez", 6000)

    def tearDown(self):
        print("teardown")

    def test_nombre_completo(self):
        print("test nombre")


        self.assertEqual(self.emp1.nombre_completo(), "axel perez")
        self.assertEqual(self.emp2.nombre_completo(), "sandra rodriguez")

    def test_aumentar_sueldo(self):
        print("test sueldo")
        self.emp1.aumentar_sueldo(500)
        self.emp2.aumentar_sueldo(500)
        self.assertEqual(self.emp1.sueldo, 5500)
        self.assertEqual(self.emp2.sueldo, 6500)

if __name__ == "__main__":
    unittest.main()
