Characteristics of Good Code
============================

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

