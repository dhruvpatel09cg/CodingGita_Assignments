### Assignment 2 
**Modify/Delete Conflict**

**Goal:** Create and resolve a Modify/Delete conflict (one branch deletes a file, another branch modifies it).

1. On remote `main`, create a file `notes.txt` with some content and commit it on GitHub.  
   Then update local main:
   ```bash
   git fetch origin main
   git merge origin/main
   ```
2. Create branch `feature/notes-delete`:
   - Delete `notes.txt`
   - Commit and push
   - Open a Pull Request (do **not** merge yet)
3. Create branch `feature/notes-edit` (from main):
   - Edit `notes.txt` and add one extra sentence
   - Commit and push
   - Open a second Pull Request
4. Merge the **delete** PR first.
5. Try to merge the **edit** PR → you will get a complex conflict (may not be resolvable in the web editor).
6. Resolve it **locally**:
   ```bash
   git checkout main
   git pull origin main
   git switch feature/notes-edit
   git merge main
   ```
7. Decide to **keep the file** and write a clear final content.  
   Then:
   ```bash
   git add .
   git commit -m "Resolve modify/delete conflict"
   git push origin feature/notes-edit
   ```
8. Merge the PR on GitHub, delete remote & local feature branches, and run `git pull origin main`.

**Answers:**
- [1st PR](https://github.com/dhruvpatel09cg/Git-command-practice/pull/15)
- [2nd PR](https://github.com/dhruvpatel09cg/Git-command-practice/pull/16)
- <img width="1255" height="611" alt="image" src="https://github.com/user-attachments/assets/5b7560fe-3a33-4194-ad3a-9de1daf12fb6" />

- <img width="940" height="788" alt="image" src="https://github.com/user-attachments/assets/4970c8ed-08fa-44a1-95f9-55890ed0c57e" />

-<img width="1893" height="735" alt="image" src="https://github.com/user-attachments/assets/17e79f02-da1e-40a3-aea8-091127fc380d" />

- [Repository link](https://github.com/dhruvpatel09cg/Git-command-practice/tree/main/Day13)

---
