def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_list = input("Nhập danh sách các số ngăn cách bởi dấu phẩy: ")
tuple_data = tuple(map(int, input_list.split(",")))
first, last = truy_cap_phan_tu(tuple_data)
print("Phần tử đầu:", first)
print("Phần tử cuối cùng:", last)
