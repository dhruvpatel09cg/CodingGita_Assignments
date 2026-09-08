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

**Submit:**
- Screenshot of `git status` when the file was untracked
- Screenshot after using `git restore --staged`
- Repository link

---
