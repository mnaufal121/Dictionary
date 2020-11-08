Dict = [{'barang': 'komputer', 'jumlah': 50, 'harga': ''},
        {'barang': 'mouse', 'jumlah': 20, 'harga': ''},
        {'barang': '', 'jumlah': 30, 'harga': '1200'}]

for x in range(len(Dict)):
    for k, v in Dict[x].items():
        # print(Dict[x][k])
        if Dict[x][k] == '':
            n = input('masukkan value' + k + ':')
            n1 = {k : n}
            Dict[x].update(n1)

for s in Dict:
    print(s)

# item = [{'barang': 'komputer', 'jumlah': 50, 'harga': ''},
#         {'barang': 'mouse', 'jumlah': '', 'harga': '200'},
#         {'barang': '', 'jumlah': 30, 'harga': ''}]

# for x in range(len(item)):
#     for k in item[x]:
#         if v == None:
#             n = input('masukkan value key' + k + ': ')
#             item[x][k] = n

# for s in item:
#     print(s)