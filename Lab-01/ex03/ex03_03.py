def to_tuple(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số ngăn cách bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
my_tuple = to_tuple(numbers)
print("Sau khi chuyển list -> tuple:", my_tuple)
