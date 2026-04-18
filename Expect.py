import time
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def brute_force(points):
    min_dist = float('inf')
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.hypot(points[i].x - points[j].x, points[i].y - points[j].y)
            if dist < min_dist:
                min_dist = dist
    return min_dist

def cross_pair(points_sorted_by_x, mid_x, d):
    # 收集条带内的点
    strip = [p for p in points_sorted_by_x if abs(p.x - mid_x) < d]
    if len(strip) < 2:
        return d
    
    cell_size = d / math.sqrt(2)
    if cell_size == 0:
        return d
    
    # 构建网格：每个点放入对应的网格单元
    grid = {}
    for p in strip:
        cell_x = int(math.floor(p.x / cell_size))
        cell_y = int(math.floor(p.y / cell_size))
        cell_id = (cell_x, cell_y)
        
        if cell_id not in grid:
            grid[cell_id] = []
        grid[cell_id].append(p)
    
    min_d = d
    
    # 遍历所有网格单元
    for cell_id, points_in_cell in grid.items():
        cx, cy = cell_id
        
        # 只检查当前网格和它右边的邻居（包括同一列和右边列）
        # 这样可以避免重复检查 (A,B) 和 (B,A)
        for dx in range(0, 2):      # dx = 0 或 1
            for dy in range(-1, 2):  # dy = -1, 0, 1
                neighbor_id = (cx + dx, cy + dy)
                if neighbor_id not in grid:
                    continue
                
                neighbor_points = grid[neighbor_id]
                
                # 根据情况决定检查方向
                if dx == 0 and dy == 0:
                    # 同一单元格：检查所有点对（只检查一次，用索引避免重复）
                    m = len(points_in_cell)
                    for i in range(m):
                        for j in range(i + 1, m):
                            dist = math.hypot(
                                points_in_cell[i].x - points_in_cell[j].x,
                                points_in_cell[i].y - points_in_cell[j].y
                            )
                            if dist < min_d:
                                min_d = dist
                else:
                    # 不同单元格：检查所有点对
                    for p_left in points_in_cell:
                        for p_right in neighbor_points:
                            dist = math.hypot(p_left.x - p_right.x, p_left.y - p_right.y)
                            if dist < min_d:
                                min_d = dist
    
    return min_d

def closest_pair_rec(points_sorted_by_x):
    n = len(points_sorted_by_x)
    if n <= 3:
        return brute_force(points_sorted_by_x)
    
    mid = n // 2
    mid_point = points_sorted_by_x[mid]
    mid_x = mid_point.x
    
    left = points_sorted_by_x[:mid]
    right = points_sorted_by_x[mid:]
    
    d_left = closest_pair_rec(left)
    d_right = closest_pair_rec(right)
    
    d = min(d_left, d_right)
    
    d_cross = cross_pair(points_sorted_by_x, mid_x, d)
    
    return min(d, d_cross)

def closest_pair(points):
    points_sorted = sorted(points, key=lambda p: p.x)
    return closest_pair_rec(points_sorted)

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
    
    print(f"[Expected O(n log n)] Closest Distance: {result:.6f}")
    print(f"Time: {(end_time - start_time)*1000:.4f} ms")
