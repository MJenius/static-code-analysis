# Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
**Ans:**  
The easiest fixes were adding docstrings, renaming functions to snake_case, and correcting spacing issues since they were mostly stylistic. The hardest was replacing the bare `except:` and removing `eval()` because those required understanding proper exception handling and code security.

## 2. Did the static analysis tools report any false positives? If so, describe one example.
**Ans:**  
No major false positives were observed. All the issues flagged were valid, though a few style-related warnings like missing blank lines did not affect the functionality of the code.

## 3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
**Ans:**  
I would integrate Pylint, Flake8, and Bandit into a CI pipeline using GitHub Actions so they automatically run on every commit or pull request. Locally, I would enable them in my IDE to detect issues early during development.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
**Ans:**  
After applying the fixes, the code became cleaner, more readable, and easier to maintain. It now follows proper coding conventions, handles errors safely, and avoids insecure practices like `eval()`, improving both quality and robustness.
