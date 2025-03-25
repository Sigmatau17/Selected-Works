def calculate(points, n):
    points = comparing(points, n)
    sum_weights = sum_w(points)
    ans = []
    ans.append(str(sum_weights))
    for i in range((len(points) + 1) // 2):
        ans.append(str(points[i].num) + " " + str(points[2*n - i - 1].num))
    return "\n".join(ans)

def comparing(points, n):
    if len(points) != 2*n:
        points.sort(key=lambda x: x.w)
        points = points[:2*n]
    points.sort(key=lambda x: x.x)
    return points

def sum_w(points):
    return sum([point.w for point in points])

class Point:
    def __init__(self, num, x, w):
        self.num = num
        self.x = x
        self.w = w

if __name__ == "__main__":
    t = int(input())
    ans = []
    for _ in range(t):
        input()
        n, m = map(int, input().split())
        points = []
        for _ in range(m):
            point_params = list(map(int, input().split()))
            points.append(Point(point_params[0], point_params[1], point_params[2]))
        ans.append(calculate(points, n))
    print("\n".join(ans))
