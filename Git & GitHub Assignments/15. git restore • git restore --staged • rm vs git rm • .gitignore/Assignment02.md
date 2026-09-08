## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

---
