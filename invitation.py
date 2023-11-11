#!/usr/bin/env python3
# Defining a function
def simple_invitation(mother, father, teacher, child, event):
    sample_text = f'''
Dear {mother} and {father}.
{teacher} and I would love to see you both as well as {child} at our {event} tomorrow evening. 

Best regards,
Principal G. Sturgis.
'''
    print(sample_text)

# Calling the function
simple_invitation(mother="Karen", father="John", teacher="Tom", child="Tina", event="Marriage")

