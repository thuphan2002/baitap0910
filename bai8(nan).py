import numpy as np
x = np.array([2, np.nan, 5, 9])

#Nếu sử dụng mean và median thông thường thì kết quả trả về là nan 

print("mean = ", np.mean(x))
print("median = ", np.median(x))

print("mean = ", np.nanmean(x))
print("median = ", np.nanmedian(x))

