def Tahun_kabisat(tahun):
    if tahun % 400 == 0:
        return True
    elif tahun % 4 == 0 and tahun % 100 != 0:
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))
if Tahun_kabisat(tahun):
    print(tahun, "adalah tahun kabisat.")
else:
    print(tahun, "bukan tahun kabisat.")
