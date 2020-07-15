age = 18    # initialize age to 18
stage = ''  # set stage empty

if age < 2:   # test age and set a stage
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age > 65:
    stage = 'elder'

print('You\'re a %s' % stage)   # output a message with according stage
