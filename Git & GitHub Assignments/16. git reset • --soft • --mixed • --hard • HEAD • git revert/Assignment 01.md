## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Answers:**
- <img width="318" height="144" alt="Capture1" src="https://github.com/user-attachments/assets/c3e024f9-e9ba-41bc-bf82-9f922f02d398" />

- <img width="635" height="243" alt="image" src="https://github.com/user-attachments/assets/438e6618-6f04-44a9-9007-df62e12bf81f" />
<img width="639" height="321" alt="image" src="https://github.com/user-attachments/assets/f75d963d-f3c7-481d-86bc-7a9809c321ad" />

- [Repository link](https://github.com/dhruvpatel09cg/Git-command-practice/tree/main/Day16)

---
