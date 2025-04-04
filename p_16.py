# 🎲 โจทย์ที่ 16: ทอยลูกเต๋า 2 ลูก
# คำสั่ง: เขียนโปรแกรมสุ่มเลขจาก 1 ถึง 6 เหมือนการทอยลูกเต๋า 2 ลูก แล้วแสดงผล และหาผลรวมของลูกเต๋าทั้งสองลูก

# ตัวอย่างผลลัพธ์:
# ผลการทอยลูกเต๋าคือ: 4, 5

import random
def roll_dice():
    return [random.randint(1, 6), random.randint(1, 6)]
def main():
    result = roll_dice()
    print(f"ผลลัพธ์การทอยลูกเต๋าคือ: {result[0]}, {result[1]}")
    print(f"ผลรวมของลูกเต๋าคือ: {sum(result)}")
if __name__ == "__main__":
    main()

