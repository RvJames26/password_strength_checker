from rules import LengthRule, UppercaseRule, LowercaseRule, NumberRule, SpecialCharacterRule

class CheckerPass:
    def __init__(self, password):
        self.password = password
        self.rules = [LengthRule(), UppercaseRule(), LowercaseRule(), NumberRule(), SpecialCharacterRule()]

    def verify(self):
        score = 0
        for rule in self.rules:
            if rule.check(self.password) is True:
                score += 1

        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Medium"
        else:
            return "Strong"