# 📆 โจทย์ที่ 6: แปลงอายุเป็นวัน
# คำสั่ง: รับอายุเป็นจำนวนปีจากผู้ใช้ แล้วคำนวณว่าเท่ากับกี่วัน (สมมติว่าปีหนึ่งมี 365 วัน)

# ตัวอย่างผลลัพธ์:
# ป้อนอายุของคุณ: 20  
# คุณมีอายุประมาณ 7300 วัน

age = int(input("ป้อนอายุของคุณ: "))
years = 365  # กำหนดค่าก่อนใช้งาน
days = age * (years + (age // 4))  # บางปีมี 366 วัน
print("คุณมีอายุประมาณ", days, "วัน")
