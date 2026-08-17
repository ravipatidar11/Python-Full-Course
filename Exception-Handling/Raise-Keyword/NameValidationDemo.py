#NameValidationDemo.py <----- Main Program

from NameExcept import InValidNameError,ZeroLengthNameError,SpaceError

from NameValidation import validate_name

while(True):
    try:
        name=input("Enter You Name:")
        v_name=validate_name(name)
    except ZeroLengthNameError:
        print("U must Enter UR Name --- Try Agin")
    except InValidNameError:
        print("Ur Name is Invalid --- Try Again")
    except SpaceError:
        print("Don't Enter Space --- Try Agin")
    else:
        print("Valid Name is: {}".format(v_name))
        break