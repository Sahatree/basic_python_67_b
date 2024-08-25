# กำหนดช่วงของหมายเลข
start = 21
end = 40

# สร้างลิสต์สำหรับจำนวนคู่และจำนวนคี่
even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]

print("จำนวนคู่:", even_numbers)
print("จำนวนคี่:", odd_numbers)