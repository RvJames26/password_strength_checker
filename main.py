from password import Pass
from rules import LengthRule, UppercaseRule, LowercaseRule, NumberRule, SpecialCharacterRule, CommonPasswordRule, NoRepeatRule
from checker_pass import CheckerPass

while True:

    input_password = Pass()
    if input_password.password.lower() in ("exit", "quit", "q"):
        break

    rules = [LengthRule(), UppercaseRule(), LowercaseRule(), NumberRule(), SpecialCharacterRule(), CommonPasswordRule(), NoRepeatRule()]

    for rule in rules:
        result = rule.check(input_password.password)
        print(f"{rule}: {'Pass' if result else 'Fail'}")

    checker = CheckerPass(input_password.password)
    print("Password Strength:", checker.verify())