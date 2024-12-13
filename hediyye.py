import random
cutlukler = []
hediyye_alanlar = ['R', 'N', 'H', 'S']
qebul_edenler = hediyye_alanlar.copy()
random.shuffle(hediyye_alanlar)
random.shuffle(qebul_edenler)

alinmadi = False
with open('hediyye.txt', 'w') as hediyye:
    siyahi = []
    while hediyye_alanlar:
        temp = hediyye_alanlar.pop()
        temp2 = random.choice(qebul_edenler)
        while temp2 == temp:
            if len(hediyye_alanlar) == 0 and temp == temp2:
                print('Alinmadi') 
                alinmadi = True
                break
            temp2 = random.choice(qebul_edenler)
        else:
            qebul_edenler.remove(temp2)
            line = f'{temp}-->{temp2}\n'
            hediyye.write(line)
if alinmadi:
    with open('hediyye.txt', 'w') as hediyye:
        hediyye.write('Alinmadi')
    # print()



