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

class CommonPasswordRule(Rule):
    common_passwords = {
        # Numeric sequences
        "123456", "12345678", "123456789", "12345", "1234567890",
        "1234567", "123123", "111111", "000000", "1234", "112233",
        "123321", "654321", "666666", "7777777", "987654321",
        
        # Default credentials & words
        "password", "password123", "admin", "admin123", "administrator",
        "root", "user", "guest", "welcome", "login",
        
        # Keyboard patterns
        "qwerty", "quertyuiop", "asdfghjkl", "zxcvbnm",
        "1q2w3e4r", "qwerty123",
        
        # Fake complexity (satisfies upper/number/symbol rules but widely breached)
        "aa123456", "pass@123", "p@ssw0rd", "admin@123", "aa@123456",
        
        # Affection, names & phrases
        "iloveyou", "princess", "sunshine", "monkey", "dragon",
        "football", "baseball", "superman", "master", "shadow",
        "michael", "jessica", "charlie", "jordan", "daniel",
        
        # Tech & Pop culture
        "minecraft", "pokemon", "roblox", "starwars", "batman"
    }

    def __str__ (self): 
        return "Not a Common Password"

    def check(self, password):
        return password.lower() not in self.common_passwords