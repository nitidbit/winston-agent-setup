Winston's global Claude settings
================================
vim mark: C

Communication
-------------
  * Avoid obsequious comments, get to the point, avoid pointless encouragement.

Writing Code
---------------
  * I (Winston) like to work by planning, checking and discussing the plan, and then executing it. Do not write code until I have asked for it.
  * Write the simplest thing that works. Do not fix other things you see--instead mention those to the user for later work.
  * When a test is failing, describe the minimum change needed in one sentence and wait for approval before writing any code.

Guides for Agents
-----------------
- [How to write comments](guides/comments.md)
- [Characteristics of Good Code](guides/characteristics-of-good-code.md)
- [Writing Automated Tests](guides/writing-automated-tests.md)


Tools
-----
  * git — you may use git to read, but no writing. In general do not commit, check out
    branches, or other things that change state.
  * agent-browser - https://github.com/vercel-labs/agent-browser
    - Installed at /opt/homebrew/bin/agent-browser
    - Headless browser CLI for inspecting live pages. Use to verify UI changes
      visually without asking the user to look.
    - The daemon persists between commands. Close and reopen when switching
      auth state: `agent-browser close`
    - To authenticate on localhost, use the E2E auth endpoint (requires
      E2E_AUTH_SECRET from .env.local):
        source apps/web/.env.local
        agent-browser open "http://localhost:3000/api/e2e-auth?secret=${E2E_AUTH_SECRET}"
    - Core workflow:
        agent-browser open <url>   # navigate
        agent-browser snapshot     # get element refs (@e1, @e2, ...)
        agent-browser click @e59   # interact using refs
        agent-browser screenshot /tmp/foo.png  # capture and Read the image

Preferred Code Bits
-------------------
For each of our projects, here are samples of code that we like with comments
about what we like about it. Prefer emulating these examples rather than the
codebase at large


### Exemplar Test Suites

#### Athenate - /Users/winstonw/nitidbit/athena-build-app

packages/service/src/domain-utils/issue.test.ts
- Sample data is easy to read. There is one functon, sampleBuildingIssue().
    Using that, tests can adjust the bits of data that are important to the test
    which highlights what's relevant to the situation.

apps/web/e2e/tests/07-funding-sources.spec.ts
- e2e tests are useful but brittle. They tests that all the layers work
  together. Prioritize testing:
  - the happy path
  - edge cases that users rarely see so manual testing is unlikely to uncover.

