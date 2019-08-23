x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10

big_list = x_list + y_list

print("The X List has %d objects" % len(x_list))
print("The Y List has %d objects" % len(y_list))
print("and finally... the big list has %d objects" %len(big_list))

if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("It worked!!!")




