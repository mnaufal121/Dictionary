std = [{'nama': 'Ahmad', 'jurusan': 'Informatika', 'semester': 2, 'angkatan': ''},
       {'nama': '', 'jurusan': 'Pertanian', 'semester': '', 'angkatan': 2017},
       {'nama': 'Insan', 'jurusan': '', 'semester': 3, 'angkatan': ''},
       {'nama': 'Malik', 'jurusan': '', 'semester': 6, 'angkatan': 2018},
       {'nama': '', 'jurusan': 'Kehutanan', 'semester': '', 'angkatan': 2015}]

# dictionary std masih belum terisi
for s in std:
    print(s)

# proses pengecekan data kosong + input user 
for x in range(len(std)):
    for k, v in std[x].items():
        if std[x][k] == '':
            n = input('masukkan value ' + k + ':')
            n1 = {k : n}
            std[x].update(n1)

# for x in range(len(std)):
#     if std[x] == std[0]:
#         n = input('angkatan: ')
#         year = {'angkatan': n}
#         std[x].update(year)
#     elif std[x] == std[1]:
#         n = input('nama: ')
#         name = {'nama' : n}
#         std[x].update(name)
#         n2 = input('semester: ')
#         smt = {'semester' : n2}
#         std[x].update(smt)
#     elif std[x] == std[2]:
#         n = input('jurusan: ')
#         dpt = {'jurusan' : n}
#         std[x].update(dpt)
#         n2 = input('angkatan: ')
#         year = {'angkatan' : n2}
#         std[x].update(year)
#     elif std[x] == std[3]:
#         n = input('jurusan: ')
#         dpt = {'jurusan': n}
#         std[x].update(dpt)
#     elif std[x] == std[4]:
#         n = input('nama: ')
#         name = {'nama' : n}
#         std[x].update(name)
#         n2 = input('semester: ')
#         smt = {'semester' : n2}
#         std[x].update(smt)

# dictionary std setelah terisi
for s in std:
    print(s)