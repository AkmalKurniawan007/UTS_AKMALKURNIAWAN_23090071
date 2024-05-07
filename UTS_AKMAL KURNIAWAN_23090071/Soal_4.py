def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def berikan_rekomendasi(bmi):
    if bmi < 18.5:
        return " Berat badan kurang. Makan yang berprotein!!! ."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal. Sip Bro pertahankan!!!! ."
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan. Jangan kebanyakan Makan dong dan Olahraga juga JANGAN MALAS....!!!!!."
    elif bmi >= 30 :
        return "obesitas. Disarankan untuk berkonsultasi dengan dokter untuk mendapatkan nasihat medis."
    else:
        return "Anda Sepertinya Bukan Orang"

        

berat_badan = float(input("Masukkan berat badan (Kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (meter): "))

bmi = hitung_bmi(berat_badan, tinggi_badan)
rekomendasi = berikan_rekomendasi(bmi)

print("BMI Anda:", bmi)
print("Rekomendasi Kesehatan:", rekomendasi)
