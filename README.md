# Expert System Mini Project - Adrian Aldridge

## Overview
This is an expert system that provides customers with recommendations for computers using rule-based forward chaining. I coded this in a VS-code environment using Python 3.14.2. 

### Files 
| File | Description 
|------|--------------
| `engine.py` | Core inference engine 
| `kb_loader.py` | Loads JSON knowledge base 
| `kb/laptop_rules.json` | KB rules
| `main.py` | Command-line interface 
| `tests/` | Folder for test cases 

## How To Run
In this directory run:
```text
python main.py
```
The system will prompt the user to collect facts and then provide recommendations. After displaying recommendations it will prompt the user to run again or quit. 

## Example Run
```text
Is portability important? (y/n): y
Do you need long battery life? (y/n): y
What is your budget? (high/medium/low): high
What will you primarily use the laptop for? (office/gaming/creative): office
Do you travel often? (y/n): n
Do you need linux compatibility? (y/n): n
Do you need macOS compatibility? (y/n): n
Do you need AI Acceleration? (y/n): n
Do you need a large screen? (y/n): n
Recommendation(s):
  premium_ultrabook
Specs:
  None
Rules Fired:
  Premium Ultrabook -> recommend:premium_ultrabook
Run the expert system again? (y/n): n
```

## Test Cases
Test cases are detailed under tests/README.txt, to run from the project directory use:
```text
python -m unittest discover -s tests
```
These test cases cover every rule as well as multiple rules firing at once and no rules firing. 
