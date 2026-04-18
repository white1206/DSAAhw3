
# Closest Pair of Points - Assignment 3


## Overview
This project implements two divide-and-conquer algorithms for the closest pair of points problem in the plane:

1. **Algorithm 1: Expected O(n log n) - Hash-Based Grid**  
   Uses a hash table to store grid cells in the merge step.

2. **Algorithm 2: Worst-Case O(n log n) - Divide & Scan**  
   Uses sorting and linear scan in the merge step, guaranteeing deterministic O(n log n) performance.

Both algorithms output:
- The minimum Euclidean distance between any two distinct points
- Execution time (in seconds)

## Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
No external libraries required. Only the Python standard library is used.

## File Structure
```
.
├── closest_pair.py      # Main implementation (both algorithms)
├── test_data/           # Directory for test datasets
│   ├── points1.in
│   └── points2.in
├── README.md            # This file
└── report.pdf           # Assignment report
```

## Usage

### Running the Program

```bash
python closest_pair.py <input_file>
```

### Example

```bash
python closest_pair.py test_data/points1.in
```

### Input Format

The input file should have the following format:
- First line: integer n (2 ≤ n ≤ 100,000), the number of points
- Next n lines: two integers x and y (-10,000,000 ≤ x, y ≤ 10,000,000)

Example:
```
6
0 0
1 1
4 5
10 10
2 2
8 9
```

### Output Format

```
[Expected O(n log n)] Closest Distance: 1.414214 Time: 0.000234 s
[Worst-Case O(n log n)] Closest Distance: 1.414214 Time: 0.000198 s
```

## Implementation Details

### Algorithm 1: Expected O(n log n) - Hash-Based Grid

- Recursively divides points by x-coordinate
- Uses a hash table (Python dict) to store non-empty grid cells
- Grid cell size = current minimum distance δ
- Each cell stores at most 2 points
- Merge step: for each left cell, check O(1) right neighbor cells via hash lookup

### Algorithm 2: Worst-Case O(n log n) - Divide & Scan

- Same recursive divide-and-conquer framework
- Merge step: collects points within δ of median line into a strip
- Strip is already sorted by y-coordinate (passed down recursively)
- Each point checks at most 7 subsequent points (geometric guarantee)
- No hash tables used, guaranteeing deterministic performance

## Complexity

| Algorithm | Time Complexity | 
|-----------|----------------|
| Algorithm 1 (Hash Grid) | Expected O(n log n) |
| Algorithm 2 (Divide & Scan) | Worst-Case O(n log n) | 

## Testing

To run both algorithms on the provided datasets:

```bash
python closest_pair.py points1.in
python closest_pair.py points2.in
```

## Notes

- All input points are assumed to be distinct
- The program handles negative coordinates correctly
- Execution time is measured using Python's `time.perf_counter()` for high precision

