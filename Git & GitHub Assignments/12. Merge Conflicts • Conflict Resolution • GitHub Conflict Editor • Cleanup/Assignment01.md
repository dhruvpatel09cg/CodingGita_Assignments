### Assignment 1 – Create and Resolve a Merge Conflict on GitHub (Mandatory)

**Goal:** Create a real conflict with two feature branches and resolve it using the GitHub browser editor.

1. Create/clone a repository and on `main` create `tasks.txt`:

```text
My Tasks
1. Study Git
2. Complete assignment
3. Review notes
```

2. Commit and push to `main`.
3. Create branch `feature/tasks-A` → change line 3 to `Practice merge conflicts` → commit → push → open PR (do **not** merge yet).
4. Switch back to `main`, create branch `feature/tasks-B` → change line 3 to `Watch Git tutorial` → commit → push → open second PR.
5. Merge the first PR successfully.
6. Merge the second PR → conflict appears.
7. Resolve the conflict on GitHub:
   - Understand Current vs Incoming
   - Decide final text (keep one, both, or write your own)
   - Remove all conflict markers
   - Mark as resolved → Commit merge → Merge the PR
8. Delete both remote feature branches.
9. Update local main and delete local branches:
   ```bash
   git checkout main
   git pull origin main
   git branch -D feature/tasks-A
   git branch -D feature/tasks-B
   ```

**Answers:**
- [Repository link]:(https://github.com/dhruvpatel09cg/Git-command-practice)
-<img width="929" height="321" alt="Capture1" src="https://github.com/user-attachments/assets/15a58eb5-39e3-49f0-acb2-9611c6a6b2ee" />

-<img width="960" height="510" alt="Capture2" src="https://github.com/user-attachments/assets/b74144e6-847a-4c66-85f4-56165a0a7587" />
 
-<img width="720" height="363" alt="image" src="https://github.com/user-attachments/assets/8cdf5f77-62eb-43a1-925c-6a97d33a90f2" />

---
