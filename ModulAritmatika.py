import Aritmatika
def main():
    a=int(input('Masukan nilai a : '))
    b=int(input('Masukan nilai b : '))
    
    print('a\t: %d' %a)
    print('b\t: %d' %b)

    print('a+b\t: %d' % Aritmatika.tambah(a,b))
    print('a-b\t: %d' % Aritmatika.kurang (a,b))
    print('a*b\t: %d' % Aritmatika.kali (a,b))
    print('a/b\t: %d' % Aritmatika.bagi(a,b))
main()