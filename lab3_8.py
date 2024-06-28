total = 0
n = int(input("จำนวนตัวเลขที่ต้องการกรอก: "))

for i in range(n):
    x = int(input("กรอกค่า x: "))
    total = total + x
    
print(f"ผลรวมคือ {total}")