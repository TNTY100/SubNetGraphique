from model.network import network_from_str, ipv4_to_int

import unittest


class NetworkUtilsTest(unittest.TestCase):
    def test_ipv4_to_int_normal_all_255(self):
        self.assertEqual(0xff_ff_ff_ff, ipv4_to_int("255.255.255.255"))

    def test_ipv4_to_int_normal_all_0(self):
        self.assertEqual(0, ipv4_to_int("0.0.0.0"))

    def test_ipv4_to_int_normal_split_groupe_1(self):
        self.assertEqual(0x0f_00_00_00, ipv4_to_int("15.0.0.0"))

    def test_ipv4_to_int_normal_split_groupe_2(self):
        self.assertEqual(0x0f_0f_00_00, ipv4_to_int("15.15.0.0"))

    def test_ipv4_to_int_normal_split_groupe_3(self):
        self.assertEqual(0x0f_0f_0f_00, ipv4_to_int("15.15.15.0"))

    def test_ipv4_to_int_normal_split_groupe_4(self):
        self.assertEqual(0x0f_0f_0f_0f, ipv4_to_int("15.15.15.15"))


if __name__ == '__main__':
    unittest.main()
