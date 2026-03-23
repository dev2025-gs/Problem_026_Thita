# 🌳 Same Tree

🔗 Problem Link: https://thita.ai/problems/same-tree

## 🧠 Problem Description

Given the roots of two binary trees `p` and `q`, write a function to determine if they are the same.

Two binary trees are considered the same if:
- They are **structurally identical**, and
- The nodes have the **same values**. :contentReference[oaicite:0]{index=0}

---

## 📥 Examples

### Example 1

Input: p = [1,2,3], q = [1,2,3]
Output: true

### Example 2

Input: p = [1,2], q = [1,null,2]
Output: false

### Example 3

Input: p = [1,2,1], q = [1,1,2]
Output: false


---

## ⚙️ Constraints

- Number of nodes in each tree: `[0, 100]`
- `-10^4 <= Node.val <= 10^4` :contentReference[oaicite:1]{index=1}

---

## 💡 Approach

We use a **recursive Depth-First Search (DFS)** approach:

### ✅ Base Cases
- If both nodes are `null` → return `true`
- If one is `null` and the other is not → return `false`
- If values differ → return `false`

### 🔁 Recursive Step
- Check:
  - Left subtree of both trees
  - Right subtree of both trees

If all checks pass → trees are identical.


