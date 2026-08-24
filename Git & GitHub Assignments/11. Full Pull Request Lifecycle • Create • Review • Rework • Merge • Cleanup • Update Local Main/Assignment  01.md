### Assignment 1 – Complete PR Lifecycle with `feature/contact-form` (Mandatory)

**Goal:** Practice the full cycle: branch → file → commit → push → PR → merge → cleanup.

1. Update main:  
   `git checkout main && git pull origin main`
2. Create branch:  
   `git checkout -b feature/contact-form`
3. Create file `contact.html` with a simple heading and a short paragraph about a contact form.
4. Stage, commit and push:  
   ```bash
   git add contact.html
   git commit -m "Add contact form page"
   git push -u origin feature/contact-form
   ```
5. On GitHub: Open a Pull Request (base = `main`, compare = `feature/contact-form`). Write a clear title and description.
6. Merge the Pull Request using **“Create a merge commit”**.
7. Delete the remote branch (GitHub “Delete branch” button or `git push origin --delete feature/contact-form`).
8. Update local main using the two-command method:  
   ```bash
   git checkout main
   git fetch origin main
   git merge origin/main
   ```
9. Delete local branch:  
   `git branch -d feature/contact-form`
   
   **Answers:**
   
11. Take screenshots of:  
    (a) the merged PR
    <img width="1014" height="624" alt="image" src="https://github.com/user-attachments/assets/f4190e15-82d6-4a66-85ae-a814ea7c2f6b" />

    (b) terminal after fetch + merge
    <img width="816" height="473" alt="image" src="https://github.com/user-attachments/assets/148f5e24-c2ca-43e5-adec-becdcc6c9fc7" />

    (c) `git branch` showing the branch is gone
    <img width="481" height="158" alt="image" src="https://github.com/user-attachments/assets/f07edd51-115a-4791-9a88-50f3a533d1c2" />


[Merged PR link](https://github.com/dhruvpatel09cg/Git-command-practice/pull/4)

---
