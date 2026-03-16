# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I thought it was normal at first, as I entered a very low number.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hints were repetitive and unhelpful. Any number I entered returned 'GO higher!'
Even though the number had a lower number.
I think the hints were backwards.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The check_guess function had reversed return statements, that the AI rightfully corrected. 
I could verify this realtime when I tried the game in the live server before and after.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Pytests and running on live server.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran the pytest test_consistent_outcome_with_string_and_int_secret in test_game_logic.py. The test calls check_guess with the same numeric secret as an int and as a str (e.g., 50 vs "50") for win/too-high/too-low cases and asserts the outcomes match. 
- Did AI help you design or understand any tests? How?
Yes, helped me design the pytests.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire script top-to-bottom whenever the user interacts (clicks a button, types, or a widget value changes), so your app recomputes UI and logic repeatedly rather than keeping a persistent in-memory flow.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Rely on it a bit less. I was 90% dependent on it with this task.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI generated code is not 100% reliable. Everything has to be double checked.
