#ชนิดข้อมูล Dictionary
person = ["Raktiya", 18, 157, 63, "ratiyatecho@gmail.com"]
print(person)
person[1] = 18
print("อายุ %d " % person[1])
print("ส่วนสูง %d น้ำหนัก %d" % (person[2], person[3]))
print("อีเมล %s" % person[4])
print(person[0:3])
print(person[2:4])
print(person[2:])
print(person[:4])
print(person[-4:-1])