from abc import ABC, abstractmethod
import string

class Rule(ABC):
    @abstractmethod
    def check(self, password):
        pass

class LengthRule(Rule):
    def __str__(self): return "Length (min 8 chars)"
    def check(self, password):
        if len(password) < 8:
            return False
        return True

class UppercaseRule(Rule):
    def __str__(self): return "Uppercase Letter"
    def check(self, password):
        if any(l.isupper() for l in password):
            return True
        else:
            return False

class LowercaseRule(Rule):
    def __str__(self): return "Lowercase Letter"
    def check(self, password):
        if any(l.islower() for l in password):
            return True
        else:
            return False

class NumberRule(Rule):
    def __str__(self): return "Number"
    def check(self, password):
        if any(l.isdigit() for l in password):
            return True
        else:
            return False

class SpecialCharacterRule(Rule):
    def __str__(self): return "Special Character"
    def check(self, password):
        if any(l in string.punctuation for l in password):
            return True
        else:
            return False