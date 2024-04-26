# bài 3 sinh ngẫu nhiên một dãy số  <=100
#liệt kê và hiển thị các số nguyên tố chia hết cho 7
#tính tổng các số lẻ trong đấy

import random
def so_nguyen(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def so_ngau_nhien():
    return [random.randint(1, 100) for _ in range(10)]