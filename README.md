# Password Strength Checker

A simple Python command-line tool that checks the strength of a password based on a set of rules.

## How to Run

```bash
python main.py
```

You will be prompted to enter a password. The program will check each rule and print a final strength rating.

## File Structure

```
password_strength_checker/
├── main.py           # Entry point — runs the program
├── password.py       # Pass class — handles user input
├── rules.py          # Rule classes — each checks one password requirement
└── checker_pass.py   # CheckerPass class — scores the password and returns a rating
```

## Strength Rating

| Rules Passed | Rating |
| :--- | :--- |
| 0 – 2 | Weak |
| 3 – 4 | Medium |
| 5 | Strong |

## Rules Checked

- Minimum 8 characters
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a number
- Contains a special character
