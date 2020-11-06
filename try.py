# Dict = [{'barang': 'komputer', 'jumlah': 50, 'harga': '2000'},
#         {'barang': 'mouse', 'jumlah': 20, 'harga': '200'},
#         {'barang': 'keyboard', 'jumlah': 30, 'harga': '1200'}, ]

# newD =  {'barang':'komputer', 'jumlah': 50, 'kualitas' : 'baru'}
# Dict2 = Dict.copy()


# print ("Dict = ", Dict)
# view = newD.fromkeys(newD)
# print (view)
# print (newD.keys())
# print (newD.values())
# print (newD.items())

# Dict.clear()
# print ("Dict2 = ", Dict2)

Dict = {'barang': 'komputer'}
chg = input('barang: ')
nDict = {'barang': chg}
Dict.update(nDict)
print(Dict)
