def Triangle(base, height):
    area = 1/2*base*height
    print("พื้นที่สามเหลี่ยม %d" % area)
    return area

b = int(input("รับค่าฐาน "))
h = int(input("รับค่าสูง "))
print("พื้นที่สามเหลี่ยม %d" % Triangle(b,h))
Triangle(b,h)
Triangle(5,10)