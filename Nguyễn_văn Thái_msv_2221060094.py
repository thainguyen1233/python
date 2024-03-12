'''Họ và tên : Nguyễn Văn Thái
   MSV:2221060094
   Nhóm: 01
   làm bài tập VD: sáng ngày 11/03/2024'''


'''vd 1 : viết chương trình cho phép nhập vào một số gồm n  phần tử tính và in ra tổng các số trong n trong 
các dãy số:'''
b = []
s = 0
n = int(input("nhập số phần tử của dãy số: "))
for i in range(1, n+1):
    a = int(input("nhập phần tử thứ " + str(i) + ": "))
    b.append(a)
for i in b: 
    s += i                                            
print("tổng của dãy số là: " + str(s))


'''vd2:viết chương trình nhập vào dãy số nguyên gôm m pần tử tính và in ra lũy thừa 2 của dãy số đó:'''
# Khởi tạo một danh sách rỗng để lưu trữ các phần tử
a = []
n = int(input("Nhập số phần tử của dãy số: "))
for i in range(1, n+1,1):
    c = int(input("Nhập phần tử thứ " + str(i) + ": "))
    a.append(c)
for i in a:
    print(str(i**2),"lũy thừ 2 của dãy số đó là :")

'''vd 3:chương trình cho phép nhập vào một câu đếm chữ hoa , chữ thường 
giả sử đầu vào là : khoa Công Nghệ Thông Tin :
ouput: chữ hoa: 5
       chu thường :15'''

n = input("Nhập câu của bạn: ")
d = {"UPPER CASE": 0, "LOWER CASE": 0}
for c in n:
    if c.isupper():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
print("Chữ hoa:", d["UPPER CASE"])
print("Chữ thường:", d["LOWER CASE"])
'''vd4:code nhập vào 1 câu , đếm chữ cái và chữ cái trong câu đó 
giả sử :"hello world!123
só chữ cái là 10 
số chữ thường là 5:"'''

s = input("Nhập câu của bạn: ")
a = 0
b = 0

for c in s:
    if c.isalpha():
        a += 1
    elif c.isdigit():
        b += 1


print("Số  chữ cái:", a)
print("Số chữ số là:", b)
'''vd:viết chương trình nhập số n từ bàn phím . kiểm tra số n là số nguyên tố hay không nguyên tố, thì thông báo ra màn hình '''
n=int(input("nhập một số:"))
dem =0
for i in range(1,n+1):
    if n % i==0:
        dem +=1
        if dem==2:
            print(n, "là số nguyên tố")
        else:
            print(n,"không phải là số nguyên tố:")