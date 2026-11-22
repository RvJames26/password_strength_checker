# Password Strength Checker

A modular Python command-line tool that evaluates password strength using Object-Oriented Programming (OOP) principles.

## How to Run

```bash
python main.py
```

Enter passwords to evaluate in real time. Type `exit`, `quit`, or `q` to close the program.

## File Structure

```
password_strength_checker/
├── main.py           # Entry point — runs the interactive loop
├── password.py       # Pass class — handles secure password input
├── rules.py          # Rule classes — individual validation checks
└── checker_pass.py   # CheckerPass class — scores the password and evaluates strength
```

## Strength Rating

| Rules Passed | Rating |
| :--- | :--- |
| 0 – 3 | Weak |
| 4 – 5 | Medium |
| 6 – 7 | Strong |

## Rules Checked

1. **Length**: Minimum 8 characters.
2. **Uppercase**: Contains at least one uppercase letter (`A-Z`).
3. **Lowercase**: Contains at least one lowercase letter (`a-z`).
4. **Number**: Contains at least one digit (`0-9`).
5. **Special Character**: Contains at least one punctuation mark (`!@#$%^&*` etc.).
6. **Common Passwords**: Checks against top breached passwords from the NordPass dataset (including substring sequences).
7. **No Consecutive Repeats**: Flags sequences with 3 or more identical characters in a row (e.g., `aaa`, `111`).
