n = int(input())
t, m = map(int, input().split())

m_sum = 0
for i in range(n):
    x = int(input())
    m_sum += x

t_sum = m_sum // 60
m_sum = m_sum % 60

t += t_sum
m += m_sum

if m >= 60:
    t += 1
    m -= 60
t = t % 24

print(t,m)