from abc import ABC, abstractmethod
import string

class Rule(ABC):
    @abstractmethod
    def check(self, password):
        pass

class LengthRule(Rule):
    def check(self, password):
        if len(password) < 8:
            return False
        return True

class UppercaseRule(Rule):  
    def check(self, password):
        if any(l.isupper() for l in password):
            return True
        else:
            return False

class LowercaseRule(Rule):
    def check(self, password):
        if any(l.islower() for l in password):
            return True
        else:
            return False

class NumberRule(Rule):
    def check(self, password):
        if any(l.isdigit() for l in password):
            return True
        else:
            return False

class SpecialCharacterRule(Rule):
    def check(self, password):
        if any(l in string.punctuation for l in password):
            return True
        else:
            return False