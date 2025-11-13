````markdown
# OldSchoolDailyProgPrac

Daily 60–90 minute **no-AI** coding practice in **C++20 (MSVC)** and **Python 3.12** on **Windows + VS Code + CMake**.  
**Odd days = C++**, **Even days = Python**. Aim to start **9:00 AM**.

---

## Quick Start

1. Install:

   - Visual Studio **Build Tools 2022** (C++ build tools + Windows 10 SDK)
   - **CMake ≥ 3.24**
   - **Python 3.12**
   - VS Code extensions: **C/C++**, **Python**, **CMake Tools**

2. Create/activate venv and install deps:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r python\requirements.txt
```
````

3. Open the repo folder in **VS Code** → select the **.venv** interpreter.

4. **C++ days** (CMake route):

   - Command Palette → **CMake: Select Configure Preset** → `msvc-debug`
   - **CMake: Build**
   - **CMake: Set Debug/Launch Target** → pick today’s target (e.g., `days_day01_cpp`)
   - Run/Debug with ▶ or **F5**

5. **Python days**:

   - **Run Task** → **Python: run active file (venv)**, or F5 with the Python debug config.

6. Create a new day any time:

```powershell
python .\scripts\new_day.py
```

This creates `days/dayNN/` with `cpp/main.cpp`, `python/main.py`, a day `README.md`, and `NOTES.md`.

---

## Repo Layout

```
.vscode/          VS Code settings/tasks/launch
scripts/          new_day.py (creates days/dayNN from templates)
common/
  cpp/{include,src}        shared C++ code (linked into each day target)
  python/src/algos/        shared Python helpers (on PYTHONPATH via settings)
  templates/               day templates (cpp/python/README)
python/
  requirements.txt         pytest, numpy, black
  pytest.ini               test discovery config ("days/" tree)
days/
  dayNN/{cpp,python,README.md,NOTES.md}
progress/
  problems.csv             simple practice log
data/                      sample inputs (optional)
CMakeLists.txt             builds one target per day's C++ main
CMakePresets.json          MSBuild presets: msvc-debug / msvc-release
PATTERNS.md                (optional) quick recall notes per pattern
```

---

## Daily Playbook (60–90 min, no AI)

**Plan (5–10 min)**

- In today’s `README.md` add:

  - **Patterns**: e.g., `Sliding Window, Hash Map`
  - **Why this pattern fits**: one line
  - **Links**: problems for today (see schedule)

**Code (40–60 min)**

- C++ days: `days/dayNN/cpp/main.cpp`
- Python days: `days/dayNN/python/main.py`

**Test & Refactor (10–15 min)**

- Add a couple of edge-case inputs.
- Tighten complexity; rename for clarity.

**Wrap (5–10 min)**

- `NOTES.md`: what worked, what failed, what you’d change.
- Log to `progress/problems.csv`:

  ```
  date,day,pattern,lc_id,title,lang,time_min,result,retries
  ```

- Commit & push:

  ```powershell
  git add .
  git commit -m "W01D01: Two Pointers (C++) – 977, 26"
  git push
  ```

---

## Weekly Operating Rhythm

- **Mon–Thu**: 1–2 problems in the current pattern(s).
- **Fri**: rewrite one of the week’s solutions in the **other language**.
- **Sat (optional)**: second problem, cleanup, or notes.
- **Sun**: spaced repetition — re-do a problem from ~7 or ~21 days ago **from scratch**.

---

## Pattern Tagging (required)

At the top of each day **README.md**:

```
**Patterns**: <choose>
**Why this pattern fits (1 line)**: <reason>
```

Core buckets: Two Pointers, Sliding Window, Prefix Sum, Binary Search, Hash Map/Set, Stack/Monotonic, Intervals/Greedy, Linked List (fast/slow, dummy), Trees (DFS/BFS/BST/LCA), Graphs (DFS/BFS/Topo/DSU/Shortest Path), Heap/Two Heaps, DP (1D/2D/Subsequence/String), Backtracking.

---

## Good-to-Know Links

- VS Code C/C++: [https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- VS Code Python: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- CMake Tools: [https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
- CMake Presets: [https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html)
- CMake FetchContent (for GoogleTest if you enable tests later): [https://cmake.org/cmake/help/latest/module/FetchContent.html](https://cmake.org/cmake/help/latest/module/FetchContent.html)
- Python venv: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
- pytest: [https://docs.pytest.org/en/latest/getting-started.html](https://docs.pytest.org/en/latest/getting-started.html)
- Black: [https://black.readthedocs.io/en/stable/](https://black.readthedocs.io/en/stable/)
- Add existing project to GitHub: [https://docs.github.com/en/repositories/creating-and-managing-repositories/adding-an-existing-project-to-github-using-the-command-line](https://docs.github.com/en/repositories/creating-and-managing-repositories/adding-an-existing-project-to-github-using-the-command-line)
- NeetCode 150: [https://neetcode.io/roadmap](https://neetcode.io/roadmap)
- Blind 75 (reference): [https://leetcode.com/list/xi4ci4ig/](https://leetcode.com/list/xi4ci4ig/)

---

## Troubleshooting

- **`cl` not found**
  Start VS Code from **Developer Command Prompt for VS 2022**, or ensure the C++ build tools workload is installed.

- **`<bits/stdc++.h>` missing on MSVC**
  MSVC doesn’t ship it. Use explicit headers (already fixed in template):

  ```cpp
  #include <algorithm>
  #include <iostream>
  #include <numeric>
  #include <string>
  #include <vector>
  ```

- **LeetCode I/O locally**
  Simulate inputs via stdin; craft a tiny harness in `main` for quick checks.

---

## 6-Week Schedule (odd=C++, even=Python)

### Week 1 — Arrays & Strings (Two Pointers, Sliding Window, Prefix, Binary Search, Hashing)

**Day 1 — C++ — Two Pointers I**

- 977. Squares of a Sorted Array — [https://leetcode.com/problems/squares-of-a-sorted-array/](https://leetcode.com/problems/squares-of-a-sorted-array/)
- 26. Remove Duplicates from Sorted Array — [https://leetcode.com/problems/remove-duplicates-from-sorted-array/](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Day 2 — Python — Sliding Window I**

- 3. Longest Substring Without Repeating Characters — [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- 209. Minimum Size Subarray Sum — [https://leetcode.com/problems/minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Day 3 — C++ — Two Pointers II**

- 283. Move Zeroes — [https://leetcode.com/problems/move-zeroes/](https://leetcode.com/problems/move-zeroes/)
- 11. Container With Most Water — [https://leetcode.com/problems/container-with-most-water/](https://leetcode.com/problems/container-with-most-water/)

**Day 4 — Python — Prefix Sum / Hashing**

- 560. Subarray Sum Equals K — [https://leetcode.com/problems/subarray-sum-equals-k/](https://leetcode.com/problems/subarray-sum-equals-k/)
- 724. Find Pivot Index — [https://leetcode.com/problems/find-pivot-index/](https://leetcode.com/problems/find-pivot-index/)

**Day 5 — C++ — Binary Search I**

- 704. Binary Search — [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)
- 33. Search in Rotated Sorted Array — [https://leetcode.com/problems/search-in-rotated-sorted-array/](https://leetcode.com/problems/search-in-rotated-sorted-array/)

**Day 6 — Python — Kadane / Stock I**

- 53. Maximum Subarray — [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)
- 121. Best Time to Buy and Sell Stock — [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

**Day 7 — C++ — Matrix Traversal**

- 48. Rotate Image — [https://leetcode.com/problems/rotate-image/](https://leetcode.com/problems/rotate-image/)
- 54. Spiral Matrix — [https://leetcode.com/problems/spiral-matrix/](https://leetcode.com/problems/spiral-matrix/)

---

### Week 2 — Linked Lists, Stacks/Queues, Hashing

**Day 8 — Python — Linked List Reversal**

- 206. Reverse Linked List — [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)
- 92. Reverse Linked List II — [https://leetcode.com/problems/reverse-linked-list-ii/](https://leetcode.com/problems/reverse-linked-list-ii/)

**Day 9 — C++ — Fast/Slow Pointers**

- 141. Linked List Cycle — [https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)
- 142. Linked List Cycle II — [https://leetcode.com/problems/linked-list-cycle-ii/](https://leetcode.com/problems/linked-list-cycle-ii/)

**Day 10 — Python — List Merge**

- 21. Merge Two Sorted Lists — [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)
- 23. Merge k Sorted Lists — [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)

**Day 11 — C++ — Dummy Node Patterns**

- 19. Remove Nth Node From End — [https://leetcode.com/problems/remove-nth-node-from-end-of-list/](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- 83. Remove Duplicates from Sorted List — [https://leetcode.com/problems/remove-duplicates-from-sorted-list/](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

**Day 12 — Python — Stacks I**

- 20. Valid Parentheses — [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)
- 155. Min Stack — [https://leetcode.com/problems/min-stack/](https://leetcode.com/problems/min-stack/)

**Day 13 — C++ — Monotonic Stack**

- 739. Daily Temperatures — [https://leetcode.com/problems/daily-temperatures/](https://leetcode.com/problems/daily-temperatures/)
- 503. Next Greater Element II — [https://leetcode.com/problems/next-greater-element-ii/](https://leetcode.com/problems/next-greater-element-ii/)

**Day 14 — Python — Queue/Deques**

- 232. Implement Queue using Stacks — [https://leetcode.com/problems/implement-queue-using-stacks/](https://leetcode.com/problems/implement-queue-using-stacks/)
- 622. Design Circular Queue — [https://leetcode.com/problems/design-circular-queue/](https://leetcode.com/problems/design-circular-queue/)

---

### Week 3 — Trees (DFS/BFS) + Graphs Intro

**Day 15 — C++ — Tree Traversal**

- 94. Binary Tree Inorder Traversal — [https://leetcode.com/problems/binary-tree-inorder-traversal/](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- 102. Binary Tree Level Order Traversal — [https://leetcode.com/problems/binary-tree-level-order-traversal/](https://leetcode.com/problems/binary-tree-level-order-traversal/)

**Day 16 — Python — Tree Depth/Diameter**

- 104. Maximum Depth of Binary Tree — [https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- 543. Diameter of Binary Tree — [https://leetcode.com/problems/diameter-of-binary-tree/](https://leetcode.com/problems/diameter-of-binary-tree/)

**Day 17 — C++ — BST Patterns**

- 98. Validate Binary Search Tree — [https://leetcode.com/problems/validate-binary-search-tree/](https://leetcode.com/problems/validate-binary-search-tree/)
- 230. Kth Smallest Element in a BST — [https://leetcode.com/problems/kth-smallest-element-in-a-bst/](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

**Day 18 — Python — LCA & Paths**

- 236. Lowest Common Ancestor of a Binary Tree — [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- 257. Binary Tree Paths — [https://leetcode.com/problems/binary-tree-paths/](https://leetcode.com/problems/binary-tree-paths/)

**Day 19 — C++ — Graphs I (Grids)**

- 200. Number of Islands — [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)
- 994. Rotting Oranges — [https://leetcode.com/problems/rotting-oranges/](https://leetcode.com/problems/rotting-oranges/)

**Day 20 — Python — Graphs II (Clone & Coloring)**

- 133. Clone Graph — [https://leetcode.com/problems/clone-graph/](https://leetcode.com/problems/clone-graph/)
- 785. Is Graph Bipartite? — [https://leetcode.com/problems/is-graph-bipartite/](https://leetcode.com/problems/is-graph-bipartite/)

**Day 21 — C++ — Topo / DSU Intro**

- 207. Course Schedule — [https://leetcode.com/problems/course-schedule/](https://leetcode.com/problems/course-schedule/)
- 684. Redundant Connection — [https://leetcode.com/problems/redundant-connection/](https://leetcode.com/problems/redundant-connection/)

---

### Week 4 — Heaps, Greedy, Intervals, Binary Search (advanced)

**Day 22 — Python — Heaps Basics**

- 215. Kth Largest Element in an Array — [https://leetcode.com/problems/kth-largest-element-in-an-array/](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- 347. Top K Frequent Elements — [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

**Day 23 — C++ — Merge K Lists / Two-Heaps**

- 23. Merge k Sorted Lists — [https://leetcode.com/problems/merge-k-sorted-lists/](https://leetcode.com/problems/merge-k-sorted-lists/)
- 295. Find Median from Data Stream — [https://leetcode.com/problems/find-median-from-data-stream/](https://leetcode.com/problems/find-median-from-data-stream/)

**Day 24 — Python — Intervals I**

- 56. Merge Intervals — [https://leetcode.com/problems/merge-intervals/](https://leetcode.com/problems/merge-intervals/)
- 435. Non-overlapping Intervals — [https://leetcode.com/problems/non-overlapping-intervals/](https://leetcode.com/problems/non-overlapping-intervals/)

**Day 25 — C++ — Intervals II**

- 452. Minimum Number of Arrows to Burst Balloons — [https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
- 57. Insert Interval — [https://leetcode.com/problems/insert-interval/](https://leetcode.com/problems/insert-interval/)

**Day 26 — Python — Binary Search on Answer**

- 410. Split Array Largest Sum — [https://leetcode.com/problems/split-array-largest-sum/](https://leetcode.com/problems/split-array-largest-sum/)
- 875. Koko Eating Bananas — [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/)

**Day 27 — C++ — Hashing Review**

- 49. Group Anagrams — [https://leetcode.com/problems/group-anagrams/](https://leetcode.com/problems/group-anagrams/)
- 128. Longest Consecutive Sequence — [https://leetcode.com/problems/longest-consecutive-sequence/](https://leetcode.com/problems/longest-consecutive-sequence/)

**Day 28 — Python — Matrix / Implementation**

- 48. Rotate Image — [https://leetcode.com/problems/rotate-image/](https://leetcode.com/problems/rotate-image/)
- 73. Set Matrix Zeroes — [https://leetcode.com/problems/set-matrix-zeroes/](https://leetcode.com/problems/set-matrix-zeroes/)

---

### Week 5 — Dynamic Programming

**Day 29 — C++ — 1D DP I**

- 70. Climbing Stairs — [https://leetcode.com/problems/climbing-stairs/](https://leetcode.com/problems/climbing-stairs/)
- 198. House Robber — [https://leetcode.com/problems/house-robber/](https://leetcode.com/problems/house-robber/)

**Day 30 — Python — 1D DP II**

- 213. House Robber II — [https://leetcode.com/problems/house-robber-ii/](https://leetcode.com/problems/house-robber-ii/)
- 322. Coin Change — [https://leetcode.com/problems/coin-change/](https://leetcode.com/problems/coin-change/)

**Day 31 — C++ — Subsequence DP I**

- 300. Longest Increasing Subsequence — [https://leetcode.com/problems/longest-increasing-subsequence/](https://leetcode.com/problems/longest-increasing-subsequence/)

**Day 32 — Python — Subsequence DP II**

- 1143. Longest Common Subsequence — [https://leetcode.com/problems/longest-common-subsequence/](https://leetcode.com/problems/longest-common-subsequence/)

**Day 33 — C++ — String DP**

- 5. Longest Palindromic Substring — [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)
- 72. Edit Distance — [https://leetcode.com/problems/edit-distance/](https://leetcode.com/problems/edit-distance/)

**Day 34 — Python — 2D Grid DP**

- 62. Unique Paths — [https://leetcode.com/problems/unique-paths/](https://leetcode.com/problems/unique-paths/)
- 64. Minimum Path Sum — [https://leetcode.com/problems/minimum-path-sum/](https://leetcode.com/problems/minimum-path-sum/)

**Day 35 — C++ — Partition/Subsets**

- 416. Partition Equal Subset Sum — [https://leetcode.com/problems/partition-equal-subset-sum/](https://leetcode.com/problems/partition-equal-subset-sum/)
- 494. Target Sum — [https://leetcode.com/problems/target-sum/](https://leetcode.com/problems/target-sum/)

---

### Week 6 — Backtracking + Shortest Paths + Review

**Day 36 — Python — Backtracking I**

- 78. Subsets — [https://leetcode.com/problems/subsets/](https://leetcode.com/problems/subsets/)
- 46. Permutations — [https://leetcode.com/problems/permutations/](https://leetcode.com/problems/permutations/)

**Day 37 — C++ — Backtracking II**

- 39. Combination Sum — [https://leetcode.com/problems/combination-sum/](https://leetcode.com/problems/combination-sum/)
- 40. Combination Sum II — [https://leetcode.com/problems/combination-sum-ii/](https://leetcode.com/problems/combination-sum-ii/)

**Day 38 — Python — Classic Backtracking**

- 51. N-Queens — [https://leetcode.com/problems/n-queens/](https://leetcode.com/problems/n-queens/)
- 79. Word Search — [https://leetcode.com/problems/word-search/](https://leetcode.com/problems/word-search/)

**Day 39 — C++ — Shortest Path I**

- 743. Network Delay Time — [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)
- 1631. Path With Minimum Effort — [https://leetcode.com/problems/path-with-minimum-effort/](https://leetcode.com/problems/path-with-minimum-effort/)

**Day 40 — Python — Shortest Path II**

- 1129. Shortest Path with Alternating Colors — [https://leetcode.com/problems/shortest-path-with-alternating-colors/](https://leetcode.com/problems/shortest-path-with-alternating-colors/)
- 1091. Shortest Path in Binary Matrix — [https://leetcode.com/problems/shortest-path-in-binary-matrix/](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

**Day 41 — C++ — Greedy/Intervals Review**

- 55. Jump Game — [https://leetcode.com/problems/jump-game/](https://leetcode.com/problems/jump-game/)
- 45. Jump Game II — [https://leetcode.com/problems/jump-game-ii/](https://leetcode.com/problems/jump-game-ii/)

**Day 42 — Python — Mock Interview (2 mediums)**

- Pick two from NeetCode 150 — [https://neetcode.io/roadmap](https://neetcode.io/roadmap)
- Blind 75 reference — [https://leetcode.com/list/xi4ci4ig/](https://leetcode.com/list/xi4ci4ig/)

## License

MIT (no holder set).
