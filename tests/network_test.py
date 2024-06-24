from model.network import network_from_str

import unittest


class NetworkTest(unittest.TestCase):

    def test_network_constructor_invalid_mask1(self):
        self.assertRaises(Exception, lambda: network_from_str("192.168.1.0", "255.255.64.0"))

    def test_network_constructor_invalid_mask2(self):
        self.assertRaises(Exception, lambda: network_from_str("192.168.1.0", "255.255.160.0"))

    def test_network_constructor(self):
        net = network_from_str("192.168.0.0", "255.255.0.0")
        self.assertEqual(65534, net.get_size())

    def test_network_size_normal24(self):
        net = network_from_str("192.168.1.0", "255.255.255.0")
        self.assertEqual(254, net.get_size())

    def test_network_size_normal16(self):
        net = network_from_str("192.168.0.0", "255.255.0.0")
        self.assertEqual(65534, net.get_size())

    def test_network_ip_int_normal1(self):
        net = network_from_str("192.168.1.0", "255.255.255.0")
        self.assertEqual(0xc0_a8_01_00, net.get_int_ip())

    def test_network_ip_str_normal1(self):
        net = network_from_str("192.168.1.0", "255.255.255.0")
        self.assertEqual("192.168.1.0", net.get_str_ip())

    def test_network_mask_int_normal1(self):
        net = network_from_str("192.168.1.0", "255.255.255.0")
        self.assertEqual(0xff_ff_ff_00, net.get_int_mask())

    def test_network_mask_str_normal1(self):
        net = network_from_str("192.168.1.0", "255.255.255.0")
        self.assertEqual("255.255.255.0", net.get_str_mask())


if __name__ == '__main__':
    unittest.main()
