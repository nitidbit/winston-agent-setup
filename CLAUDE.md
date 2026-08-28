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

Writing Tests
-------
  * Write code in a test-driven manner (TDD) which means:
    - outline tests,
    - write one test and see that it fails,
    - implement the minimum code to make that one test pass -- nothing more Principle: Do not implement behavior that no test yet covers. If a button test only checks visibility, implement only the render condition -- not the click handler, not the drawer, not the form.  This holds even when I've already described the full behavior in plain English before any tests exist -- knowing the eventual spec is not license to implement it early. A stub (e.g. `return false`) that satisfies the one test in front of you is correct; the real logic waits for the test that forces it.
    - Move on to next test passes.
  * For e2e/integration tests, since the tests are slow, try and test the "happy path" with multiple expectations per test. This also means fewer tests so it's easier for humans to understand.
  * Try to make tests with a sample input that is complete. Often called `Sample___`. Later tests will modify the good sample data to illustrate error inputs.
  * Goals of tests:
    * verify code does what it's supposed to, including edge cases
    * document what the code does
    * document the intentions for why we wrote the code
  * To improve documentation, try to test the entire shape of return values from functions so the reader can see what the output will look like.
  * When generating sample numbers in tests, use numbers that are easily
    distingishable such as 111, 222, 333 rather than 001, 002, 003



Characteristics of Good Code
----------------------------
Most important characteristics are at the top.

* Prioritize readability

* Simplest thing that works
  - **Intent**: Every abstraction has a cost. Useful only if it removes more complexity than it adds.
  - **Policy**: Avoid extra layers: Use basic built-in tools (like a standard array or list) instead of building heavy, complex setups. Make it work, then improve: Get the program running first, then clean and refactor the design safely.

* Don't Repeat Yourself (DRY)

* Avoid premature optimization (YAGNI)

* Philosophy of Deep Design
  -   **Intent**: We value high information density behind simple entry points.
  -   **Policy**: Strive to make modules "deep." The interface must be significantly simpler than its hidden internal implementation. 
  -   **Judgment Guidance**: If an interface requires the caller to understand its internal sequence, or if a change forces coordinated modifications across both sides of the interface, the abstraction has failed. Prioritize consolidating that leaked knowledge into a single module.

* Policy on Information Hiding & Leakage
  -   **Intent**: Modules must completely own their structural secrets to minimize change amplification.
  -   **Policy**: Hide implementation decisions. Classes and modules must tightly restrict visibility of internal data structures, helper utilities, and processing steps.
  -   **Judgment Guidance**: Expose only *what* a module does, never *how*. If a system modification requires editing multiple decoupled files, treat it as a symptom of information leakage and refactor the boundaries first.

* Policy on Layer Abstraction (New Layer, New Abstraction)
  -   **Intent**: Every architectural layer must transform the conceptual representation of the problem, rather than merely passing data downward.
  -   **Policy**: Do not create intermediate classes, service wrappers, or controllers that mirror the exact method signatures, parameters, and return types of underlying modules.
  -   **Judgment Guidance**: Identify and eliminate "pass-through methods." If a new module or class does not introduce a completely fresh vocabulary, a simpler data contract, or a higher-level workflow, either merge the adjacent layers or expose the underlying layer directly to callers.

* Policy on Downgrading Complexity
  -   **Intent**: System complexity must be pushed down to the implementer, freeing the user from mental overhead.
  -   **Policy**: The implementer (you, the agent) must absorb the difficulty of edge cases, configuration defaults, and error boundaries so callers remain simple.
  -   **Judgment Guidance**: Never push configuration properties, specialized flags, or manual lifecycle cleanup upward simply because it makes the module implementation easier to write.

* Policy of Defining Errors Out of Existence
  -   **Intent**: Maximize system robustness by minimizing explicit error-handling paths.
  -   **Policy**: Design methods and APIs to implicitly handle unusual or boundary conditions gracefully without throwing exceptions or demanding defensive catch-blocks.
  -   **Judgment Guidance**: Treat exceptions as a design cost. For example, a resource removal request targeting an ID that does not exist should quietly complete as a no-op, rather than raising a disruptive error condition.

* Intentional Documentation
  -   **Intent**: Comments must provide a separate, higher-level conceptual layer than the raw code syntax.
  -   **Policy**: Document the "why" and the high-level abstractions that are completely invisible to a compiler.
  -   **Judgment Guidance**: Draft the high-level structural design in comments *before* writing the implementation. Avoid literal descriptions that mirror the code keywords; focus exclusively on developer intent and non-obvious constraints. If the function is straightforward, no comment is needed.


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

