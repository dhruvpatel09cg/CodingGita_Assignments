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

**Answers:**
- <img width="817" height="340" alt="image" src="https://github.com/user-attachments/assets/8fea319b-a639-4fb2-a743-c92f38d20b11" />
- <img width="645" height="362" alt="image" src="https://github.com/user-attachments/assets/99c10698-9990-4473-9baa-1c92cda8cd1b" />
- <img width="1075" height="308" alt="image" src="https://github.com/user-attachments/assets/29c3ea97-2583-4516-9ea1-80d7a0b60581" />

- [Repository link](https://github.com/dhruvpatel09cg/Git-command-practice/tree/main/Day15)

---
