## Assignment B —  Theoretical  
**Title:** “Stash Concepts”

**Submit:** File `assignmentB.md` with short answers.

Answer in 2–4 lines each.

1. What is `git stash` in simple words? When do we use it?  
2. You have:
   - `app.js` (tracked, modified)
   - `test.js` (untracked)
   - `.env` (ignored)

   Which files are stashed by:
   - `git stash`
   - `git stash -u`
   - `git stash -a`

3. Explain the difference between:
   - `git stash apply`
   - `git stash pop`
<img width="976" height="691" alt="image" src="https://github.com/user-attachments/assets/e13e16ff-76cd-49d5-a7e5-1a0d99343c8b" />

4. When would you prefer `apply` over `pop`? Give one small example.

5. What do these commands do?
   - `git stash drop`
   - `git stash clear`

6. You see this `git stash list`:
   ```text
   stash@{0}: WIP on feature/login: ...
   stash@{1}: WIP on main: ...
   ```
   - Which is the latest stash?
   - If you run `git stash pop`, which one is removed?

7. Why is it good to use messages like:
   ```bash
   git stash push -m "WIP: login form"
   ```
   instead of just `git stash`? (2–3 lines)
<img width="954" height="762" alt="image" src="https://github.com/user-attachments/assets/d5634b1f-f54d-4ee6-b3b4-d64ba3805a2b" />

8. Scenario:
   - You are on `feature/checkout`.
   - `checkout.html` is committed.
   - `checkout.css` is staged.
   - `checkout.js` is untracked.

   You must switch to `main` urgently.  
   Write the exact command(s) you will use to stash your work safely (include untracked files and a message).
<img width="858" height="341" alt="image" src="https://github.com/user-attachments/assets/49375b7d-d967-417e-98ce-3e76ac208677" />

***
