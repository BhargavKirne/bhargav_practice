l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_comp = [i for i in l if i % 2 == 0]
print(list_comp)


list_comp_com = [f"{i} is even" if i % 2 == 0 else f"{i} is odd" for i in l]
print(list_comp_com)

in_ = int(input("enter your input range: "))
list_comp_com2 = [f"{i} is even" if i % 2 == 0 else f"{i} is odd" for i in range(in_)]
print(list_comp_com2)

tpl_com = (f"{i} is even" if i % 2 == 0 else f"{i} is odd" for i in range(10))
tp_co = tuple(tpl_com)
print(tp_co)

a = 20

rr = "YES" if a < 10 else "NO"
print(rr)

dd_cp = {i: i * i for i in range(10)}
print(dd_cp)

dic_cop = {i: i * i for i in range(10) if i % 2 == 1}
print(dic_cop)
