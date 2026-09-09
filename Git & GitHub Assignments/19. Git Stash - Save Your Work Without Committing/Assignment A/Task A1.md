### Task A1 — Basic Stash (10 mins)

1. On `main`:
   - Edit `README.md`.
   - Create `notes.txt` (don’t add it to Git).

2. Run:
   ```bash
   git stash
   git stash -u
   git stash list
   ```
   - <img width="610" height="124" alt="image" src="https://github.com/user-attachments/assets/568201bd-689f-4e3a-bad7-3e7bba6a718c" />


3. Answer in `assignmentA.md`:
   - Q1: How many stashes do you see? Which is latest (`stash@{0}` or `stash@{1}`)?
   - Q2: Which stash has `notes.txt`? How do you know?
<img width="779" height="209" alt="image" src="https://github.com/user-attachments/assets/37373699-7074-48be-9b40-205ffced3b6c" />

4. Run:
   ```bash
   git stash pop
   git stash list
   ```
   - <img width="728" height="332" alt="image" src="https://github.com/user-attachments/assets/67cff113-122c-4275-807a-a86a7ab1a5f3" />


5. Answer:
   - Q3: What happened to the stash list after `pop`? (2 lines)
<img width="921" height="134" alt="image" src="https://github.com/user-attachments/assets/8d02d30f-c56b-4ca2-9b13-2cd84937fe68" />

***
