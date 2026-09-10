Writing Automated Tests
-----------------------

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


