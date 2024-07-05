def bemid(a, b, c):
    T = a + b + c
    return T

Sc = int(input("รับค่าคะแนนเก็บ: "))
Jit = int(input("รับค่าคะแนนจิตพิสัย: "))
Mid = int(input("รับค่าคะแนนกลางภาค: "))
print("คะแนนเก็บก่อนกลางภาค %.2f " % bemid(Sc, Jit, Mid))