H,W = map(int, input().split())
w_list = list(map(int, input().split()))

max_h = max(w_list)
max_idx = w_list.index(max_h)

start_idx = 0
while w_list[start_idx] == 0:
    if start_idx == W:
        start_idx = W
    start_idx += 1 
end_idx = W-1
while w_list[end_idx] == 0:
    if end_idx == 0:
        end_idx = W
    end_idx -= 1

arr_1 = w_list[start_idx:max_idx]
arr_2 = w_list[max_idx:end_idx+1]
area = 0
stick_area = sum(w_list)

stick = 0
for a in arr_1:
    if stick < a:
        stick = a
    area = area + stick

stick = 0
for a in arr_2[::-1]:
    if stick < a:
        stick = a
    area = area + stick
    
print(area-stick_area)