## Question 1:

Explain the following in your own words:

1. What is the difference between a **Branch** and a **Tag** in Git?
-->Answer:

        A branch is used for development of new features and can move forward as new commits are added.
        A tag is used to mark a specific commit and work as permanent mark for it.
        Branches can change, but tags generally remain fixed on the same commit.
    
2. What is the difference between a **Lightweight Tag** and an **Annotated Tag**?
-->Answer:

       A lightweight tag is used for personal reference only, it's tag name can be anything you understand,
       also it can't contain any message or extra information about commit.
       A annotated tag is used in professional practice, it can store tag message and extra information about
       it, it's tag name is recommended to be like semantic versioning. It shows name of tagger.
   
4. Why should we prefer Annotated tags in professional/collaborative projects?
-->Answer:

        Annotated tags allow you to attach a tag message or extra information about that tag which can make it
        easy to understand for other teammates or the code reviewer to understand about purpose of that particular
       tag. That's why the annotated tags are recommended in professional practice.
   
6. What is Semantic Versioning? Explain with examples of `v1.0.0`, `v1.1.0`, and `v1.1.1`.
-->Answer:

       Semantic Versioning (or SemVer) is a system for giving numbers to software versions. It helps developers
       tell users how much a new update changes the code.
       A version number has three parts: MAJOR.MINOR.PATCH (like 1.4.2). Each part goes up by a number when you make changes:
       MAJOR: Changes when you break old rules or fix things so old code stops working.
       MINOR: Changes when you add new features, but old code still works fine.
       PATCH: Changes when you fix small bugs, and everything stays safe and working.
       Example: v2.1.3 --> It tells that after the release of web or app there have been two major updates
       in design or function of it followed by one minor change and three bug fixes.
---
