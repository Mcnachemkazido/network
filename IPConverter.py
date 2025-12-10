from time import process_time


class IPConverter:

    @staticmethod
    def ip_to_int(ip_str):
        parts = ip_str.split(".")
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])


    @staticmethod
    def int_to_ip(ip_int):
        p1 = (ip_int >> 24)
        p2 = (ip_int >> 16) & 255
        p3 = (ip_int >> 8) & 255
        p4 = ip_int & 255
        return f"{p1}.{p2}.{p3}.{p4}"


# x = IPConverter.ip_to_int("127.0.0.1")
# print(bin(x)[2:])
# print(IPConverter.int_to_ip(x))
