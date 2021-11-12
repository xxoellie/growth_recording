x,y,w,h = map(int,input().split())
min_list = []
min_list.append(x)
min_list.append(y)
min_list.append(w)
min_list.append(h)
min_list.append(w-x)
min_list.append(h-y)
print(min(min_list))