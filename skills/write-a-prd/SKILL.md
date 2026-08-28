---
name: write-a-prd
description: Generate a Product Requirements Doc (PRD) from the client brief and write it as a local markdown file in $ISSUES_DIR. Use this when the user wants to turn a client request into a structured PRD.
---
This skill will be invoked when the user wants to create a PRD. You may skip steps if you don't consider them necessary.

1. Check whether $ISSUES_DIR already contains files. If it does, tell the user to delete them before continuing, so old PRD/issue files don't linger alongside the new work.

2. Ask the user for a long, detailed description of the problem they want to solve and any potential ideas for solutions.

3. Explore the repo to verify their assertions and understand the current state of the codebase.

4. Interview the user relentlessly about every aspect of this plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

5. Sketch out the major modules you will need to build or modify to complete the implementation. Actively look for opportunities to extract deep modules that can be tested in isolation.

A deep module (as opposed to a shallow module) is one which encapsulates a lot of functionality in a simple, testable interface which rarely changes.

Check with the user that these modules match their expectations. Check with the user which modules they want tests written for.

6. Once you have a complete understanding of the problem and solution, use the template below to write the PRD. The PRD should be written as a local markdown file at $PRD_MD. Create the $ISSUES_DIR directory if it doesn't exist. Do NOT submit a GitHub issue or call any external service.

## Settings
$AGENT_DIR = agent~/
$ISSUES_DIR = $AGENT_DIR/issues/
$PRD_MD = $AGENT_DIR/issues/prd.md

<prd-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories & Requirements

A numbered list of user stories and related requirements. Each user story should be in the format below with related requirements indented.:

S1. As an <actor>, I <do some actions>, and <see some output> so that <benefit>
  R2. Account balances are formatted as USD, e.g. "$1,222,444.00"

<user-story-example>
S1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
  R1. Account balances are formatted as USD, e.g. "$1,222,444.00"
  R2. Negative balances use parentheses, e.g. "($222,333.00)"
S2. As an operator refreshing a test environment, I want a stale file reference to be logged and skipped, so that one bad row cannot block every future refresh
  R3. Stale file references must be sent to the logfile.
</user-story-example>

### Stories versus Requirements
A story describes someone doing something and the outcome they get, and is small enough that a slice of work could be built from it. Cover the user-visible value, not every aspect of the feature. Most features yield fewer than a dozen genuine stories; stop when you run out rather than padding the list.

Two tests before writing one:

- Read the "so that" clause. If the benefit merely restates the want, it is a requirement, not a story.
- Ask whether it describes someone doing something, or the system being built a certain way. The second is a requirement.

A developer or operator actor does not by itself make an item a requirement. For internal tooling, how the tool is operated is genuine user-visible value.

Anything failing these tests belongs in Requirements. Never state the same item in more than one section of the PRD.

### Requirements

Requirements are conditions the finished work must satisfy, written as plain declarative sentences with no "As an actor" framing. This is where constraints, qualities, and acceptance criteria live: error-handling policy, output format, ordering guarantees, configuration contracts, security and privacy conditions, performance expectations.

Requirements describe what must be true of the result, observable from outside. Implementation Decisions below describe how it is built. If an item names a module, an interface, or a technical choice, it is a decision, not a requirement.

Stories and requirements are both traceable, and issue files may reference either.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this PRD.

## Further Notes

Any further notes about the feature.

</prd-template>
