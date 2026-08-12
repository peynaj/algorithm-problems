Morris Traversal
---

No Left?
- visit
- go right

Has Left?
- find predecessor (rightmost of left)

    - No Thread?
        - create thread: predecessor.right = current
        - go left

    - Has Thread?
        - clear thread: predecessor.right = None
        - visit
        - go right