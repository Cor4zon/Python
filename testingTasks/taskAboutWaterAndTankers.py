def solve (water, capacity):
    capacity = sorted(list(capacity), reverse=True)
    water = sum(list(water))

    number_of_tankers = 0
    sum_water_capacity = 0
    while sum_water_capacity < water:
        sum_water_capacity += capacity[number_of_tankers]
        number_of_tankers += 1
    return number_of_tankers





n = int(input())
capacity = map(int, input().split())
water = map(int, input().split())

out_ = solve(water, capacity)
print (out_)