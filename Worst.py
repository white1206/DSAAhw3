import math
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def euclidean_dist(p, q):
    return math.hypot(p.x - q.x, p.y - q.y)

def brute_force(points):
    min_d = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = euclidean_dist(points[i], points[j])
            if d < min_d:
                min_d = d
    return min_d

def cross_pair(points_by_y, mid_x, d):
    strip = [p for p in points_by_y if abs(p.x - mid_x) < d]
    
    min_d = d
    m = len(strip)
    
    for i in range(m):
        # 检查后续最多 7 个点
        for j in range(i+1, min(i+8, m)):
            # y 方向剪枝
            if strip[j].y - strip[i].y >= min_d:
                break
            
            dist = euclidean_dist(strip[i], strip[j])
            if dist < min_d:
                min_d = dist
    
    return min_d

def closest_pair_rec(points_by_x, points_by_y):
    n = len(points_by_x)
    if n <= 3:
        return brute_force(points_by_x), points_by_x, points_by_y
    
    mid = n // 2
    mid_x = points_by_x[mid].x
    left_by_x = points_by_x[:mid]
    right_by_x = points_by_x[mid:]
    
    left_by_y = []
    right_by_y = []
    for p in points_by_y:
        if p.x <= mid_x:
            left_by_y.append(p)
        else:
            right_by_y.append(p)
    
   
    d_left, left_by_x, left_by_y = closest_pair_rec(left_by_x, left_by_y)
    d_right, right_by_x, right_by_y = closest_pair_rec(right_by_x, right_by_y)
    d = min(d_left, d_right)
    
    d_cross = cross_pair(points_by_y, mid_x, d)
    
    return min(d, d_cross),points_by_x, points_by_y

def closest_pair(points):
    if len(points) < 2:
        return float('inf')
    points_by_x = sorted(points, key=lambda p: p.x)
    points_by_y = sorted(points, key=lambda p: p.y)
    
    min_dist, _, _ = closest_pair_rec(points_by_x, points_by_y)
    return min_dist

if __name__ == "__main__":
    with open("points1.in", "r") as f:
        lines = f.readlines()
    
        n = int(lines[0].strip())
      
        points = []
        for i in range(1, n + 1):
            x, y = map(float, lines[i].strip().split())
            points.append(Point(x, y))
    
    start_time = time.perf_counter()
    result = closest_pair(points)
    end_time = time.perf_counter()
    
    print(f"Closest Distance: {result:.6f}")
    print(f"Time: {(end_time - start_time)*1000:.4f} ms")
