## input = [1,12,-5,-6,50,3], k=4 ==> find the max average of k consecutive numbers

def find_the_max(input_list, k):
    start = 0
    sum_ = 0
    avg = []

    for i in range(len(input_list)):
        sum_ += input_list[i]

        if i >= k-1:
            avg.append(sum_/k)
            sum_ -= input_list[start]
            start += 1

    return max(avg)

print(find_the_max([1,12,-5,-6,50,3], 4)) # 12.75