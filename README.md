# recursive-challenge-solution
# Recursive Technical Assessment – Python Solution

This repository contains a Python code submission for the **technical assessment round** of **Recursive Inc. (Japan)** for the Software Developer role.

The assessment focused on evaluating **recursive thinking**, clean input handling, and the ability to write functional-style code without using loops.

---

## 🧠 Problem Overview

For each test case:
1. Read an integer `x` — the number of integers expected
2. Read the next line containing `x` integers
3. From the list, select all **non-positive integers** (≤ 0)
4. **Recursively compute the sum of their 4th powers**

If the number of integers doesn’t match `x`, or if input is invalid, output `-1`.

---

## 🔁 Recursive Focus

This code demonstrates:
- Recursive parsing of all test cases (no `for` or `while` loops used)
- Recursive summation logic for computing power values
- Robust error handling using recursion itself

---

## 📥 Sample Input

2
3
-1 0 2
4
1 -2 -3 4

shell
Copy
Edit

## 📤 Sample Output

1
97
---

## 🛠️ How to Run

You can run the script by piping input from a file or typing manually.

```bash
python main.py < sample_input.txt

