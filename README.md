# Closest Pair of Points - Assignment 3

## Author
Chang Le

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
