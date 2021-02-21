"""
Challenge
Modify the lease agreement with your signature without changing the original lease variable.
"""

lease = '''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: 
'''

"""
Fei's Solution
"""

"""
21DDC Solution
"""
signature = "Dot"

new_lease = f'''
Dear Dot, 
This document validates that you are beholden to a monthly payment of rent for this house.
Rent is to be paid by the first of every month.
Fill in your signature to agree to these terms.
-------------
Please Sign Here: {signature} 
'''
print(new_lease)
