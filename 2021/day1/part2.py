
with open('input.txt', 'r') as f:
    input = f.readlines()

WINDOW_SIZE = 3

# VERSION 1
# Using partial sums
increases = 0
partial_sums = []

for i, n in enumerate(input):
    if i == 0:
        partial_sums.append(int(n))
    else:
        partial_sums.append(int(n) + partial_sums[i-1])

right = WINDOW_SIZE
last_sum = partial_sums[right-1]
while(right < len(partial_sums)):
    left = right - WINDOW_SIZE
    if(partial_sums[right] - partial_sums[left] > last_sum):
        increases+=1
    last_sum = partial_sums[right] - partial_sums[left]
    right +=1


print(increases)


# VERSION 2
# Using normal sliding window
right = 0
left = 0
increases = 0
current_sum = 0
last_sum = float('-inf')

while(right < len(input)):
    while(right - left < WINDOW_SIZE):
        current_sum+=int(input[right])
        right+=1
    if(current_sum > last_sum):
        increases+=1
    last_sum = current_sum
    current_sum-=int(input[left])
    left+=1

print(increases-1)