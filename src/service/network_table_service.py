from model.network import Network


class NetworkTableService:
    def __init__(self, network: Network = None, network_list: list[Network] = None):
        if network is None and network_list is None:
            raise Exception("Exception : il faut un network ou une liste de network pour procéder")

        if network is not None:
            self.network_list = [network]
        else:
            self.network_list = network_list.copy()

    def _sort_by_ip(self):
        self.network_list.sort(key=lambda x: x.get_int_ip())

    def split(self, element_id: int):
        network = self.network_list.pop(element_id)
        try:
            self.network_list.extend(network.split())
        except Exception as ex:
            self.network_list.append(network)
            raise ex
        finally:
            self._sort_by_ip()

    def __str__(self):
        # Set the table titles and sizes
        id_title = "#"
        id_width = max(len(str(len(self.network_list))), len(id_title))

        ip_title = "IP"
        ip_width = 15

        mask_title = "MASK"
        mask_width = 15

        # TODO : Check if copy is better
        self.network_list.sort(key=lambda x: x.get_size(), reverse=True)
        size_title = "SIZE"
        size_width = max(len(f"{self.network_list[0].get_size():,}"), len(size_title))

        row_format = f"| {{:>{id_width}}} | {{:>{ip_width}}} | {{:>{mask_width}}} | {{:>{size_width}}} |\n"

        # Re-sort of the list
        self._sort_by_ip()

        return (row_format.format(id_title, ip_title, mask_title, size_title)
                + "".join(row_format.format(i, x.get_str_ip(), x.get_str_mask(), f"{x.get_size():,}")
                          for i, x in enumerate(self.network_list)))
