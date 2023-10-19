# TODO Найдите количество книг, которое можно разместить на дискете
disk_Mb = 1.44
pages = 100
lines = 50
symbols = 25
one_symbol_B = 4
disk_B = disk_Mb * 1024 * 1024
book_B = pages * lines * symbols * one_symbol_B
count_book_in_one_disk = int(disk_B // book_B)
print("Количество книг, помещающихся на дискету:", count_book_in_one_disk)
