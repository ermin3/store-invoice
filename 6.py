import csv
import os


def uvod():
    with open('py.csv', newline='')as pr:
        read = csv.reader(pr, delimiter=',', quotechar='"')
        print('prodavnica prodaje ' + ' '.join(red[1] for red in read))


def ispis(suma, iznos, pdv):
    print('{:10} {:10} {:10} {:10}'.format('Proizvod:', 'Kolicina:', 'Cijena:', 'Suma:'))
    print('{:10} {:10} {:10} {:10}'.format('--------', '--------', '--------', '--------'))
    for i in racun.values():
        print('{:9} {:9} {:9.2f} {:9}'.format(i[0], i[1], i[2], i[1] * i[2]))

    print('{:10} {:10} {:10} {:9.2f}'.format(' ', '', 'iznos', iznos))
    print('{:10} {:10} {:10} {:9.2f}'.format('', '', 'PDV', pdv))
    print('{:10} {:10} {:10} {:9}'.format('', '', 'UKUPNO', suma))
    print('{:14} Dodjite nam opet!'.format(''))
    print('-------------')
    racun.clear()


suma = 0
pdv = 0
iznos = 0
racun = {}


def prodaja(suma, iznos, pdv):
    br_racuna = 0
    # varijable koje se ne postavljaju na nulu
    ponavljati_ispis = True
    while ponavljati_ispis:
        er = '5'  # varijable koje moraju biti 0
        print('unos racuna \n---------')
        uvod()
        while er != '0':
            i = 0
            proizvod = str(input('unesi proizvod, za kraj pritisni 0'))
            with open('py.csv', newline='')as pr:
                read = csv.reader(pr, delimiter=',', quotechar='"')
                for line in read:
                    if proizvod == line[1]:
                        i -= 1
                        while proizvod == line[1]:
                            if proizvod not in racun:
                                cijena = float(line[2])
                                kolicina = int(input('unesite kolicinu'))
                                racun.update({proizvod: [proizvod, kolicina, cijena]})
                                suma += cijena * kolicina
                                break
                            elif proizvod in racun:
                                cijena = float(line[2])
                                kolicina += int(input('unesite kolicinu'))
                                racun.update({proizvod: [proizvod, kolicina, cijena]})
                                suma += cijena * kolicina
                                break
                if i == 0:
                    print('nemamo taj proizvod')

            if proizvod == '0':
                er = '0'

        pdv = suma * 0.17
        iznos = suma - pdv

        print('----------')
        br_racuna += 1
        print('broj racuna', br_racuna, '\n----------')
        ispis(suma, iznos, pdv)
        suma = 0
        pdv = 0
        iznos = 0
        ponovo = input('da li zelite ispis novog racuna da/ne').lower()
        if ponovo == 'da':
            os.system('cls')

        else:
            ponavljati_ispis = False
            break


def inventura():

    te = '0'
    b=4
    while te == '0' or te == 'da':
        lista = []
        with open('py.csv', 'r+', newline='')as pr:
            read = csv.reader(pr, delimiter=',', quotechar='"')
            te = '0'
            uvod()
            n_proizvod = str(input('unesi novi proizvod')).lower()
            for i,line in enumerate(read):
                b = len(line)+i-2
                if n_proizvod == line[1]:
                    print('taj proizvod vec postoji')
                    te = str(input('da li zelite unjeti novi proizvod da/ne')).lower()

            if te == '0':
                n_cijena = str(input('unesi cijenu proizvoda'))
                b+=1
                lista.append(str(b))
                lista.append(n_proizvod)
                lista.append(n_cijena)
                pr.write('\n' + ','.join(lista))
                te = str(input('da li zelite unjeti novi proizvod da/ne')).lower()


r_i = '5'
while r_i != '0':
    r_i = str(input('da li zelite racun ili inventuru, za kraj pritisnite 0 r/i/0'))

    if r_i == 'i':
        inventura()
    elif r_i == 'r':
        prodaja(suma, iznos, pdv)
    else:
        print('hvala sto ste uredili podatke')
