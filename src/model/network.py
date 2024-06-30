IP_LENGTH = 32


class Network:
    def __init__(self, ip: int, mask: int):
        self.validate_network(ip, mask)

        self.ip = ip & mask
        self.mask = mask

    def validate_network(self, ip, mask):
        if (ip > 0xFF_FF_FF_FF or mask > 0xFF_FF_FF_FF
                or ip < 0 or mask < 0):
            raise Exception("Range error")
        if mask & 0b11 > 0:
            raise Exception("Masque ne peut pas dépasser /30 ou 255.255.255.252")
        # Check si le mask est plein (pas de 0 dans les 1)
        mask_check = mask
        count = 1
        # Défiler le nombre jusqu'au premier 1.
        while mask_check & 1 == 0 and count < IP_LENGTH:
            mask_check = mask_check >> 1
            count += 1
        # S'assure qu'il n'y a plus de 0 à travers les 1
        while count < IP_LENGTH:
            mask_check = mask_check >> 1
            if mask_check & 1 == 0:
                raise Exception("Le mask est invalide (suite de 1 suivi de 0).")
            count += 1

    def get_size(self) -> int:
        return 0xff_ff_ff_ff - self.mask - 1

    def get_str_mask(self):
        return int_to_ipv4(self.mask)

    def get_int_mask(self):
        return self.mask

    def get_str_ip(self):
        return int_to_ipv4(self.ip)

    def get_int_ip(self):
        return self.ip

    def __str__(self):
        return f"Netowrk{{ip: {self.get_str_ip()}, mask: {self.get_str_mask()}}}"


def network_from_str(ip: str, mask: str) -> Network:
    return Network(ipv4_to_int(ip), ipv4_to_int(mask))


def ipv4_to_int(ip: str) -> int:
    ip_parts = ip.split(".")
    return (int(ip_parts[3])
            + (int(ip_parts[2]) << 8)
            + (int(ip_parts[1]) << 16)
            + (int(ip_parts[0]) << 24))


def int_to_ipv4(ip: int) -> str:
    return ".".join(str(i) for i in ip.to_bytes(4, "big"))
