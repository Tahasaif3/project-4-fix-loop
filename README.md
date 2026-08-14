# Project 4 - A Fix Loop With a Real Checker

Idea: one agent (the implementer) drafts a fix in its own branch, a second,
separate agent (the reviewer) grades that fix without knowing in advance
what "correct" is supposed to look like. Only a `PASS` opens a pull
request. A reviewer that approves everything isn't a reviewer.

## The bug
`cart_total.py` gives quantity discounts, but the tier checks use `>`
instead of `>=`. So buying exactly 5 or exactly 10 units misses the
discount tier it should land in - an off-by-one at the boundary.

`test_cart_total.py` pins down what the tiers should actually do.

## What happened here
1. Bug shipped on `main` (see the first commit).
2. **Implementer** branch `fix/discount-boundaries`: changed both `>` to
   `>=`. Tests pass.
3. **Reviewer**: a fresh agent, with no memory of what I intended, was
   handed only the diff and the test suite and asked to run the tests and
   judge the fix on its own. It said `PASS` - opened a real PR.
4. To prove the reviewer isn't a rubber stamp, a second branch,
   `fix/discount-boundaries-bad`, fixed only one of the two conditions on
   purpose. Same reviewer process. It said `FAIL`, and said why - no PR
   opened for that branch.

## Done when
- A real fix gets `PASS` and a real PR.
- A deliberately incomplete fix gets `FAIL` with reasons, and no PR.
