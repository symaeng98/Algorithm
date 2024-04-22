n = int(input())
s = input()

cnt_list = []
red_to_right = s.rstrip("R")
cnt_list.append(red_to_right.count("R"))

red_to_left = s.lstrip("R")
cnt_list.append(red_to_left.count("R"))

blue_to_right = s.rstrip("B")
cnt_list.append(blue_to_right.count("B"))

blue_to_left = s.lstrip("B")
cnt_list.append(blue_to_left.count("B"))

print(min(cnt_list))