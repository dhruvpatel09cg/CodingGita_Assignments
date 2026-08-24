### Assignment 2 – `feature/about-page` with Review & Rework (Mandatory)

**Goal:** Practice receiving a review comment, reworking the **same** branch, and updating the PR.

1. Create branch:  
   `git checkout -b feature/about-page`
2. Create `about.html` with only a basic heading (intentionally incomplete).
3. Commit and push:  
   ```bash
   git add .
   git commit -m "Add about page skeleton"
   git push -u origin feature/about-page
   ```
4. Open a Pull Request on GitHub.
5. **Simulate review:** Add a comment on the PR yourself (or ask a classmate/mentor) requesting:  
   *“Please add a short paragraph about the purpose of the about page and a simple team section placeholder.”*
6. Rework on the **same branch**:  
   ```bash
   git checkout feature/about-page
   # edit about.html as requested
   git add .
   git commit -m "Address review: add description and team section"
   git push origin feature/about-page
   ```
7. Confirm the PR on GitHub now shows the new commit.
8. Merge the PR, delete remote branch, update local main (`git fetch` + `git merge` or `git pull`), delete local branch.
   **Answers:**
   
10. Screenshot:  
   (a) PR conversation showing the review comment + your new commit
      <img width="948" height="777" alt="image" src="https://github.com/user-attachments/assets/62770c09-55c6-4e30-9f09-a7355d706f3c" />

   (b) merged PR
      <img width="1012" height="736" alt="image" src="https://github.com/user-attachments/assets/d6be9367-6a3c-41d7-9e39-8ff69bdff50a" />

      
 [PR link showing review comment + rework commit](https://github.com/dhruvpatel09cg/Git-command-practice/pull/5)


---
