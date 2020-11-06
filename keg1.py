epl = [{'klub': 'liverpool', 'posisi': 1, 'pelatih': 'klopp', 'gol': 17},
       {'klub': 'chelsea', 'posisi': 7, 'pelatih': 'lampard', 'gol': 16},
       {'klub': 'leeds', 'posisi': 12, 'pelatih': 'bielsa', 'gol': 13},
       {'klub': 'manutd', 'posisi': 15, 'pelatih': 'ole', 'gol': 9},
       {'klub': 'burnley', 'posisi': 20, 'pelatih': 'dyche', 'gol': 3}]

# no1
for team in epl:
    team.pop('klub')
    team.pop('pelatih')
    print(team)

# no2
for x in range(len(epl)):
    if epl[x] == epl[1]:
        epl[x].clear()
    print(epl[x])

# no3
for team in epl:
    print("Nama Tim :", team.get('klub'))
    print("Posisi Klasemen :", team.get('posisi'))
    print("Nama Pelatih :", team.get('pelatih'))
    print("Jumlah Gol :", team.get('gol'))

# no4,5,6
newteam = {'klub': 'leicester', 'posisi': 2, 'pelatih': 'rodgers', 'gol': 17}
epl.append(newteam)
for team in epl:
    chg = input('Ubah value key 4: ')
    # team['gol'] = chg
    ngol = {'gol': chg}
    team.update(ngol)

for team in epl:
    print("1. Nama Tim :", team.get('klub'))
    print("2. Posisi Klasemen :", team.get('posisi'))
    print("3. Nama Pelatih :", team.get('pelatih'))
    print("4. Jumlah Gol :", team.get('gol'))

# no7,8
for x in range(len(epl)):
    if epl[x] == epl[0]:
        chg = input('ubah value key 2: ')
        npos = {'posisi': chg}
        epl[x].update(npos)
        # epl[x]['posisi'] = chg
    elif epl[x] == epl[1]:
        chg = input('ubah value key 4: ')
        ngol = {'gol': chg}
        epl[x].update(ngol)
        # epl[x]['gol'] = chg
    elif epl[x] == epl[3]:
        chg = input('ubah value key 3: ')
        ncoc = {'pelatih': chg}
        epl[x].update(ncoc)
        # epl[x]['pelatih'] = chg

for team in epl:
    print("1. Nama Tim :", team.get('klub'))
    print("2. Posisi Klasemen :", team.get('posisi'))
    print("3. Nama Pelatih :", team.get('pelatih'))
    print("4. Jumlah Gol :", team.get('gol'))

# no9,10
valkey2 = 0
valkey4 = 0
clubs = []
coachs = []

for team in epl:
    valkey2 += team.get('posisi')
    valkey4 += team.get('gol')
    valkey1 = team.get('klub')
    clubs.append(valkey1)
    valkey3 = team.get('pelatih')
    coachs.append(valkey3)

print('Total Nilai Posisi :', valkey2)
print('Total Gol :', valkey4)
print(clubs)
print(coachs)