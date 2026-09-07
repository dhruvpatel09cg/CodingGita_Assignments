### Assignment 1 
**Conflict during `git pull`**

**Goal:** Face and resolve a conflict that appears when you run `git pull origin main`.

1. On GitHub (remote `main`), create a file `welcome.txt` with the content:  
   `Welcome to Git class`
2. Commit it directly on GitHub.
3. On your **local main**, create the same file `welcome.txt` with different content:  
   `Welcome to Day 13`
4. Run:
   ```bash
   git add welcome.txt
   git commit -m "Add welcome.txt locally"
   git pull origin main
   ```
5. A conflict will appear. Resolve it by keeping **both** lines (or any final version you prefer).
6. Remove all conflict markers, then:
   ```bash
   git add welcome.txt
   git commit -m "Resolve pull conflict in welcome.txt"
   git push origin main
   ```

**Submit:**
- Screenshot of the conflict markers
- <img width="1053" height="792" alt="image" src="https://github.com/user-attachments/assets/cf140ea5-a5b0-464b-8fdc-fb7c324c92a7" />
- Screenshot of the final resolved file on GitHub
- <img width="1420" height="717" alt="image" src="https://github.com/user-attachments/assets/fe5c4a8a-dd1c-4306-85ba-0d3ec451d873" />

- [Repository link](https://github.com/dhruvpatel09cg/Git-command-practice/blob/main/welcome.txt)


---
