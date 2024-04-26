from ngaunhien import so_nguyen, so_ngau_nhien

danh_sach_ngau_nhien = so_ngau_nhien()
so_nguyen_to_chia_het_7 = [x for x in danh_sach_ngau_nhien if so_nguyen(x) and x % 7 == 0]
tong_so_le = sum([x for x in danh_sach_ngau_nhien if x % 2 != 0])

print(f"Dãy số ngẫu nhiên: {danh_sach_ngau_nhien}")
print(f"Các số nguyên tố chia hết cho 7: {so_nguyen_to_chia_het_7}")
print(f"Tổng các số lẻ: {tong_so_le}")