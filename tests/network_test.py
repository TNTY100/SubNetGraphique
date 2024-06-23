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


if __name__ == '__main__':
    unittest.main()
