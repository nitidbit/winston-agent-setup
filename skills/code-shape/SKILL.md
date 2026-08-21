---
name: code-shape
description: Look at the orgnaization of code so at the file and folder level.
  Does the code follow the project's layering?

---
This skill will be invoked when the user wants to analyze code they've written
recently, to look for areas for refactoring.

<what-to-do>

Look at recently changed code (default: current branch's diff against main,
unless the user names specific files). For each changed module or function,
evaluate it against three traits:

- Encapsulation: does it expose internal data structures, helpers, or steps
  that callers shouldn't need to know about? Could the interface be simpler
  than what it currently reveals?
- Cohesion: do the pieces inside this module change for the same reason? Flag
  anything that seems bolted on rather than belonging.
- Single layer of abstraction: does each function mix high-level orchestration
  with low-level detail? A function should read as one level of "what", not
  jump between "what" and "how".

Don't rewrite anything yet. Report findings as a list, ranked most-important
first, each with a file:line reference and a one-sentence reason it fails the
trait. Stop after the top three — don't dump every possible nit.

</what-to-do>

Notes on choices:
- Capped at top three findings, mirroring review-architecture's "don't give the entire list" discipline — keeps output actionable instead of overwhelming.
- Report-only, no auto-refactor — matches your "plan, check, discuss, then execute" preference from global CLAUDE.md.
- Left the diff-scope default (current branch vs main) as a guess; happy to change if you want it to always ask which files instead.

