from password import Pass
from rules import LengthRule, UppercaseRule, LowercaseRule, NumberRule, SpecialCharacterRule
from checker_pass import CheckerPass

input_password = Pass()
print(input_password)

rules = [LengthRule(), UppercaseRule(), LowercaseRule(), NumberRule(), SpecialCharacterRule()]

for rule in rules:
    result = rule.check(input_password.password)
    print(rule, result)

checker = CheckerPass(input_password.password)
print(checker.verify())
