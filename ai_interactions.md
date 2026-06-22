# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used |                       AI-Suggested Test                              | Did It Pass?|            Your Reasoning            |
|-----------|-------------|---------------------------------------------------------------------|---------------|--------------------------------|
|Out of bounds| Add new section for edge test cases, testing negative and very large numbers as input| PASSED| When checking the negative numbers and large numbers, they still return the correct hints too low, or too high to the secret |

AI suggested text
Negative numbers:
Negative guess that's too low
Negative guess that's too high (compared to negative secret) 

|Decimal numbers| test decimals as guesses | Not immediately | Decimal numbers can be compared to the secret, and also nothing in the code handles decimals to round, therefore the logic still works. I had to update the AI to not round in the tests|

AI suggested text
Decimal inputs: Decimal that rounds down and is too high (75.9 → too high) 
Decimal that rounds down and is too low (40.5 → too low)
Decimal that rounds to equal the secret (50.3 → win)
Decimal just below secret (49.9 → too low) 

| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
