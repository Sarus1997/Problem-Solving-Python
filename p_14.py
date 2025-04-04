# 📦 โจทย์ที่ 14: แปลงองศาเซลเซียสเป็นฟาเรนไฮต์
# คำสั่ง: รับอุณหภูมิในหน่วยเซลเซียส แล้วแปลงเป็นฟาเรนไฮต์ (สูตร: °F = °C × 9/5 + 32)

# ตัวอย่างผลลัพธ์:
# ป้อนอุณหภูมิ (°C): 30  
# เท่ากับ 86.0 °F

def celsius_to_fahrenheit(celsius):
 
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
def main():

    celsius = float(input("ป้อนอุณหภูมิ (°C): "))
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"เท่ากับ {fahrenheit} °F")
if __name__ == "__main__":
    main()
80