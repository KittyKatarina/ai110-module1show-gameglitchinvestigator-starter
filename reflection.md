# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game looks like a simple guessing game with two buttons and a checkbox. The buttons were for guessing and to start a new game, and the checkbox was to enable or disable hints. Theres also developer debug info as well as difficulty settings, easy, normal, and hard. I notice the expected range changes when selecting the difficulty, from 1-20, 1-100, and 1-50 each with varying numbers of guesses.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The hints are wrong, and seemed not based on our guessed number. Sometimes clicking the submit guess button needed two clicks to register. Whenever a new game is started, it looks like we always have less attempts. New game button does not register new game sometimes, and it seems the difficulty parameters don't affect the secret number's range or the number of total attempts.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess 40| "go lower"       | "go higher"     | none                   |
|new game| new game to start| No new game if game finished| none       |
|difficulty| change in range| range still 0-100 | none                 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 

The AI suggested how on even numbered attempts the secret is changed from int to string, giving the TypeError and printing the wrong hint.
I was able to verify this by asking Claude to further explain and verify what is going on and it lead me to the specific if statement on line
158 in app.py. The AI explained on even numbered attempts the secret is changed to a string, and when check_guess() is called with the secret number as a string the comparison for the guess to the secret is an int and string comparison, causing the TypeError. The AI further explained how when the
error is caught and handled, the string comparison done afterwards would also give the wrong logic, as comparing numbers in strings
such as "8" > "75" would return true, since "String comparison is lexicographic (alphabetical/dictionary order), not numeric", so in this example
the "8" > "7" is being compared, which would return true even though its false for "8" > "75"

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI suggested the Go higher and Go lower hints were switched, however after reviewing I was able to verify that the logic should be correct, as when a guess is higher or lower, the correct messages were in the correct logical place. The AI was misleading in the idea that the logic was incorrect, however I did identified two error messages that looked correct but the actual English was wrong, as they were "Too low, go lower" and "Too high, go higher" which have the second parts of the statements switched. The AI was incorrect about the logic being wrong however missed the incorrect message statements.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
