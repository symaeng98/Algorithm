n, m = map(int, input().split())
brands = []
for _ in range(m):
    package, single = map(int, input().split())
    brands.append((package, single))

cheapest_package_brand = sorted(brands, key=lambda x: x[0])[0]
cheapest_single_brand = sorted(brands, key=lambda x: x[1])[0]

package_num = n // 6
single_num = n % 6

price = 0
if cheapest_package_brand[0] > cheapest_single_brand[1] * 6:
    price += package_num*6*cheapest_single_brand[1]
else:
    price += package_num*cheapest_package_brand[0]

if cheapest_single_brand[1]*single_num > cheapest_package_brand[0]:
    price += cheapest_package_brand[0]
else:
    price += cheapest_single_brand[1]*single_num

print(price)