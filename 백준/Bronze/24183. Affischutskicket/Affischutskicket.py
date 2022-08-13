c4, a3, a4 = map(int, input().split())

envelop = 229 * 324 * c4 * 2
poster = 297 * 420 * a3 * 2
sheet = 210 * 297 * a4

print("{:.6f}".format((envelop + poster + sheet) * 0.000001))