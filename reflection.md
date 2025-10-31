# Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
**Ans:**  
The easiest issues to fix were adding docstrings, renaming functions to snake_case, and correcting spacing errors since they only required formatting changes. The hardest were removing the `eval()` function and replacing the broad `except:` block, as they involved understanding code security and proper exception handling.

## 2. Did the static analysis tools report any false positives? If so, describe one example.
**Ans:**  
No major false positives were found. All the reported issues were valid and led to meaningful improvements in code quality. Some style warnings, like missing blank lines, were minor but still useful for maintaining consistency.

## 3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
**Ans:**  
I would integrate Pylint, Flake8, and Bandit into a CI pipeline using GitHub Actions so they automatically check every commit or pull request. Locally, I would also enable them in my IDE to catch errors early before pushing code.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
**Ans:**  
After applying the fixes, the code became more secure, readable, and maintainable. It now follows PEP 8 standards, handles exceptions safely, avoids unsafe functions like `eval()`, and properly manages files and logging, resulting in cleaner and more robust code.
