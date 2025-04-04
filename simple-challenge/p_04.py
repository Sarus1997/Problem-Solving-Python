# 💬 โจทย์ที่ 4: นับสระในประโยค
# คำสั่ง: เขียนโปรแกรมรับประโยคจากผู้ใช้ แล้วนับว่ามีสระภาษาอังกฤษ (a e i o u) กี่ตัว

# ตัวอย่างผลลัพธ์:
# ป้อนประโยค: This is an example  
# มีสระทั้งหมด 6 ตัว

text = input("ป้อนประโยค: ")
vowels = "aeiouAEIOU"  # สระภาษาอังกฤษ
count = 0
for char in text:
    if char in vowels:
        count += 1
print("มีสระทั้งหมด", count, "ตัว")
