Winston's global Claude settings
================================
vim mark: C

Communication
-------------
  * Avoid obsequious comments, get to the point, avoid pointless encouragement.

Developing Code
---------------
  * I (Winston) like to work by planning, checking and discussing the plan, and
    then executing it. Do not write code until I have asked for it.
  * Write the simplest thing that works. Do not fix other things you
    see--instead mention those to the user for later work.
  * When a test is failing, describe the minimum change needed in one sentence
    and wait for approval before writing any code.

Testing
-------
  * Write code in a test-driven manner (TDD) which means:
    - outline tests,
    - write one test and see that it fails,
    -  implement the minimum code to make that one test pass -- nothing more
       Principle: Do not implement behavior that no test yet covers. If a button
       test only checks visibility, implement only the render condition -- not
       the click handler, not the drawer, not the form.
       This holds even when I've already described the full behavior in
       plain English before any tests exist -- knowing the eventual spec is
       not license to implement it early. A stub (e.g. `return false`) that
       satisfies the one test in front of you is correct; the real logic
       waits for the test that forces it.
    - Move on to next test passes.
  * For e2e/integration tests, since the tests are slow, try and test the "happy
    path" with multiple expectations per test. This also means fewer tests so
    it's easier for humans to understand.
  * Try to make tests with a sample input that is complete. Often called
    `Sample___`. Later tests will modify the good sample data to illustrate
    error inputs.


Tools
-----
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
