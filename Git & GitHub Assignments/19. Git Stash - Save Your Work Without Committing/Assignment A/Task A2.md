### Task A2 — Switch Branch with Half-Done Work (10 mins)

1. Create branch:
   ```bash
   git switch -c feature/login
   ```
2. In this branch:
   - Create `login.html` → commit it.
   - Create `login.css` → stage it (`git add login.css`).
   - Create `login.js` → leave it untracked.

3. You must switch to `main` urgently.  
   Stash your work (include untracked files) with a message:
   ```bash
   git stash -u -m "WIP: login page"
   ```

4. Switch to `main`, make a small change, commit, push:
   ```bash
   git switch main
   # edit README.md
   git add README.md
   git commit -m "Small update"
   git push
   ```

5. Go back and restore your work:
   ```bash
   git switch feature/login
   git stash pop
   ```

6. Answer:
   - Q4: Why did you need `git stash` before switching to `main`? (2–3 lines)
   - Q5:<img width="650" height="169" alt="image" src="https://github.com/user-attachments/assets/4399cf8b-2720-46b1-ae15-f75ff8b6940e" />


***
