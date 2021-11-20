# | computer memory |
# |                 |
# |    2 104 105    |
# |    |            |
# +----+---+--------+
#      |   
# a ---+   
# 
# strings are just a sequence
# of characters, but computers
# don't understand characters,
# so people came up with common
# way to them characters in memory
# the ASCII standard:
# a  -> 97
# ...
# h  -> 104
# ...
# we also store the length of the
# string nearby, so print knows
# when to stop

a = 'hi'
print(a)

# this is not exactly the memory
# layout in python, but its close
