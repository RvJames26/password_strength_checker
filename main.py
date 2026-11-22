from password import Pass
from rules import LengthRule, UppercaseRule, LowercaseRule, NumberRule, SpecialCharacterRule

input_password = Pass()
print(input_password)

rules = [LengthRule(), UppercaseRule(), LowercaseRule(), NumberRule(), SpecialCharacterRule()]

for rule in rules:
    result = rule.check(input_password.password)
    print(rule, result)