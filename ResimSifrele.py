import random
from operator import xor

A = []
B1 = []
B2 = []
A2 = []
A3 = []
A1 = []

_fileFormat = ''


def Sifrele():
    global _fileFormat
    try:
        _dosyaYol = input('Şifrelenecek Dosyanın Yolunu Belirtiniz.\n')
        file = open(_dosyaYol, 'rb')
        data = file.read()
        _fileFormat = _dosyaYol.split('.')
        _fileFormat = _fileFormat[1]

        _A1 = 'Key1.' + _fileFormat
        _A2 = 'Key2.' + _fileFormat
        _A3 = 'Key3.' + _fileFormat

        # B1, B2, A2, A3 creating
        for i in range(len(data)):
            A.append(data[i])
            B1.append(random.randint(0, 255))
            B2.append(random.randint(0, 255))
            A2.append(xor(B1[i], B2[i]))
            A3.append(xor(B2[i], A[i]))

        file = open(_A1, 'wb')
        file.write(bytes(B1))
        file.close()

        file = open(_A2, 'wb')
        file.write(bytes(A2))
        file.close()

        file = open(_A3, 'wb')
        file.write(bytes(A3))
        file.close()

    except FileNotFoundError:
        print('Error : File Not Found')


def SifreCoz():
    global _fileFormat
    try:
        _dosyaYol = input('1. Şifre Anahrının Yolunu Giriniz.\n')

        _fileFormat = _dosyaYol.split('.')
        _fileFormat = _fileFormat[1]

        _A = 'Image.' + _fileFormat

        file = open(_dosyaYol, 'rb')
        data = file.read()
        file.close()

        for i in range(len(data)):
            A1.append(data[i])

        _dosyaYol2 = input("2. Şifre Anahrının Yolunu Giriniz.\n")

        file = open(_dosyaYol2, 'rb')
        data = file.read()
        file.close()
        for i in range(len(data)):
            A2.append(data[i])

        _dosyaYol3 = input("3. Şifre Anahrının Yolunu Giriniz.\n")

        file = open(_dosyaYol3, 'rb')
        data = file.read()
        file.close()

        for i in range(len(data)):
            A3.append(data[i])
        C = []
        for i in range(len(data)):
            C.append(xor(xor(A1[i], A2[i]), A3[i]))

        file = open(_A, 'wb')
        file.write(bytes(C))
        file.close()

    except FileNotFoundError:
        print("Error : File Not Found")


def Main():
    Menu = """
    Yapmak istediginiz islemi seciniz.
    1- Sifrele 2- SifreCoz 3- Çıkış
    """
    while 1:
        _Kontrol = int(input(Menu))
        if _Kontrol == 1:
            Sifrele()
        elif _Kontrol == 2:
            SifreCoz()
        elif _Kontrol == 3:
            exit(0)
        else:
            print("Hatalı tuşa bastınız.")


Main()
