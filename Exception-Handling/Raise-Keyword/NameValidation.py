# NameValidation.py <---- Module Name

from NameExcept import InValidNameError,ZeroLengthNameError,SpaceError

def validate_name(name):
    if (name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        if (len(name)==0):
            raise ZeroLengthNameError
        else:
            res=True
            for word in words:
                if (not word.isalpha()):
                    res=False
                    break
            if (res):
                return " ".join(words)
            else:
                raise InValidNameError