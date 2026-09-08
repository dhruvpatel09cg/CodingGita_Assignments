## Assignment 1 – Practice `git restore` and `git restore --staged`

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
```bash
git restore profile.txt
```
Observe that it does **not** work (because the file is untracked).
4. Stage the file:
```bash
git add profile.txt
```
5. Unstage it using:
```bash
git restore --staged profile.txt
```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
```bash
git add profile.txt
git commit -m "Add profile.txt"
```

**Answers:**
- <img width="1357" height="382" alt="image" src="https://github.com/user-attachments/assets/22f3189f-37ff-459b-9910-c5b3c3ab2993" />

- <img width="766" height="465" alt="image" src="https://github.com/user-attachments/assets/3eba37dc-626c-4054-88ed-64cd8d98d706" />

- [Repository link](https://github.com/dhruvpatel09cg/Git-command-practice/tree/main/Day14)

---
