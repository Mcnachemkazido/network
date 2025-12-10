from IPConverter import IPConverter

class IPv4Network:

    def __init__(self, ip_str, mask_str):
        self.ip_str = ip_str
        self.mask_str = mask_str

        self.ip_as_int = IPConverter.ip_to_int(ip_str)
        self.mask_as_int = IPConverter.ip_to_int(mask_str)

        self.network_int = 0
        self.broadcast_int = 0

    def calculate_network(self):
        self.network_int = self.ip_as_int  & self.mask_as_int

    def calculate_broadcast(self):
        network = self.network_int
        new_mask = ~self.mask_as_int & 0xFFFFFFFF
        self.broadcast_int =  network | new_mask

    def get_network_address(self):
        self.calculate_network()
        return IPConverter.int_to_ip(self.network_int)

    def get_broadcast_address(self):
        self.calculate_broadcast()
        return IPConverter.int_to_ip(self.broadcast_int)


    def get_first_host(self):
        return IPConverter.int_to_ip(self.network_int + 1)

    def get_last_host(self):
        return IPConverter.int_to_ip(self.broadcast_int - 1)

    def get_next_network(self):
        return IPConverter.int_to_ip(self.broadcast_int + 1)

x = IPv4Network("204.91.159.172","255.255.255.248")
print(x.get_network_address())
print(x.get_first_host())
print(x.get_broadcast_address())
print(x.get_last_host())
print(x.get_next_network())