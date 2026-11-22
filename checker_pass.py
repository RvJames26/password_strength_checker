from rules import LengthRule, UppercaseRule, LowercaseRule, NumberRule, SpecialCharacterRule, CommonPasswordRule

class CheckerPass:
    def __init__(self, password):
        self.password = password
        self.rules = [LengthRule(), UppercaseRule(), LowercaseRule(), NumberRule(), SpecialCharacterRule(), CommonPasswordRule()]

    def verify(self):
        score = 0
        for rule in self.rules:
            if rule.check(self.password) is True:
                score += 1

        if score <= 3:
            return "Weak"
        elif score <= 5:
            return "Medium"
        else:
            return "Strong"