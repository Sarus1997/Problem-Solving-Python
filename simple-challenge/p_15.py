# 🎲 โจทย์ที่ 15: ทอยลูกเต๋า
# คำสั่ง: เขียนโปรแกรมสุ่มเลขจาก 1 ถึง 6 เหมือนการทอยลูกเต๋า แล้วแสดงผล

# ตัวอย่างผลลัพธ์:
# ผลการทอยลูกเต๋าคือ: 4

import random
def roll_dice():
    return random.randint(1, 6)
def main():
    result = roll_dice()
    print(f"ผลการทอยลูกเต๋าคือ: {result}")
if __name__ == "__main__":
    main()
