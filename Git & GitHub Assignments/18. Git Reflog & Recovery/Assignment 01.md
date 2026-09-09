## 📋 Part 1: Recovery After `git reset --hard` (5 Points)

### Task
1. Create a new repository called `reflog-practice-part1`
2. Create 3 commits:
   - **C0:** `README.md` with project title
   - **C1:** `index.html` with `<h1>Welcome</h1>`
   - **C2:** `style.css` with basic styling
3. Accidentally delete C1 and C2 using `git reset --hard <C0-commit-hash>`
4. Use `git reflog` to find the lost C2 commit
5. Recover C2 (and C1) using detached HEAD + branch + merge
6. Verify all commits are restored

### Answers

✅ <img width="621" height="154" alt="image" src="https://github.com/user-attachments/assets/e432b8f2-1a34-47b4-ab09-6b9c974a20dd" />


✅ <img width="599" height="212" alt="image" src="https://github.com/user-attachments/assets/0c0f7e6a-02c2-4010-a23e-a2756c3ec285" />

✅ <img width="1083" height="275" alt="image" src="https://github.com/user-attachments/assets/31239efa-9be4-4072-a567-986752ed57e6" />

✅ <img width="662" height="158" alt="image" src="https://github.com/user-attachments/assets/d9f34ef4-56b8-4da4-a871-518cdf3b5c46" />

✅ [Push final repository to GitHub](https://github.com/dhruvpatel09cg/reflog-practice-part1)
