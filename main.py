from password import Pass
from rules import LengthRule, UppercaseRule, LowercaseRule, NumberRule, SpecialCharacterRule, CommonPasswordRule
from checker_pass import CheckerPass

input_password = Pass()

rules = [LengthRule(), UppercaseRule(), LowercaseRule(), NumberRule(), SpecialCharacterRule(), CommonPasswordRule()]

for rule in rules:
    result = rule.check(input_password.password)
    print(f"{rule}: {'Pass' if result else 'Fail'}")

checker = CheckerPass(input_password.password)
print("Password Strength:", checker.verify())