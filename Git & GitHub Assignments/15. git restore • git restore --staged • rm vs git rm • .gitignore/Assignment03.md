## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- <img width="897" height="455" alt="image" src="https://github.com/user-attachments/assets/436e56ab-0d4d-466d-8856-b6a916161b47" />

- <img width="1431" height="600" alt="image" src="https://github.com/user-attachments/assets/7511c85a-de5a-4dd0-8a29-43f9efd1bbce" />

- <img width="1120" height="503" alt="image" src="https://github.com/user-attachments/assets/437c0e52-805c-4d2a-9ee6-26eb4c78c418" />

- [Repository link](https://github.com/dhruvpatel09cg/Git-command-practice/tree/main/Day15)

---
