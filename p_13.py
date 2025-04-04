# 🔁 โจทย์ที่ 13: ตรวจสอบคำว่า Palindrome
# คำสั่ง: รับคำจากผู้ใช้ แล้วตรวจสอบว่าคำนี้เป็น Palindrome หรือไม่ (อ่านจากซ้ายไปขวาและขวาไปซ้ายเหมือนกัน)

# ตัวอย่างผลลัพธ์:
# ป้อนคำ: radar  
# คำนี้เป็น Palindrome

text = input("ป้อนคำ: ")
is_palindrome = text == text[::-1]

if is_palindrome:
    print("คำนี้เป็น Palindrome")
else:
    print("คำนี้ไม่ใช่ Palindrome")