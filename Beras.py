
import cv2
import numpy as np

img = cv2.imread('beras3.jpg', 0)
blur = cv2.GaussianBlur(img, (11, 11), 0)
edges = cv2.Canny(blur, 40, 90)


dilated = cv2.dilate(edges, (1, 1), iterations=2)
# ini artinya kernelnya 1 x 1
# atau matriks 1x 1

# punya parameter
# cv2.dilate(img, kernel/matriknya, iterasinya )


# Kalian pasti sudah tidak asing lagi dengan peta bukan?
# Umumnya pada skala peta bertuliskan 1:1000000 cm, artinya jika
# skala pada peta 1 cm maka pada kenyataannya berjarak 1.000.000 cm.
# Perhitungan tersebut dalam matematika disebut dengan dilatasi.

(cnt, _) = cv2.findContours(dilated.copy(),
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# kita ambil copy nya agar image asli tidak kehapus
# cv2.RETR_EXTERNAL digunakan untuk
# menyeleksi bagian tepi luar koin
# cv2.CHAIN_APPROX_SIMPLE digunakan untuk
# memastikan tepi luar koin ttp utuh
# findcontour berfungsi untuk menghitung garis(contour) pada object

# print('Terdapat {} koin dalam gambar'.format(len(cnt)))
font = cv2.FONT_HERSHEY_PLAIN
teks = 'Terdapat {} Butir Beras'.format(len(cnt))
cv2.putText(dilated, teks, (50, 20), font, 1, (255, 0, 0), 2, cv2.LINE_AA)


cv2.imshow('Beras', dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
