def check_my_quess(quess, condition):
  print "My quess %r , correct %r \t\t\t\t result %r" % (quess, condition, quess == condition)

# True and True
check_my_quess(True, True and True)
# False and True
check_my_quess(False, False and True)
# 1 == 1 and 2 == 1
check_my_quess(False, 1 == 1 and 2 ==1)
# "test" == "test"
check_my_quess(True, "test" == "test")
# 1 == 1 or 2 != 1
check_my_quess(True, 1 == 1 or 2!=1)
# True and 1 == 1
check_my_quess(True, True and 1 == 1)
# False and 0 != 0
check_my_quess(False, False and 0!=0)
# True or 1 == 1
check_my_quess(True, True or 1 == 1)
# "test" == "testing"
check_my_quess(False, "test" == "testing")
# 1 != 0 and 2 == 1
check_my_quess(False, 1 !=0 and 2==1)
# "test" != "testing"
check_my_quess(True, "test" != "testing")
# "test" == 1
check_my_quess(False, "test" == 1)
# not (True and False)
check_my_quess(True, not(True and False))
# not (1 == 1 and 0 != 1)
check_my_quess(False, not(1==1 and 0 != 1))
# not (10 == 1 or 1000 == 1000)
check_my_quess(False, not(10==1 or 1000 == 1000))
# not (1 != 10 or 3 == 4)
check_my_quess(False, not (1!=10 or 3==4))
# not ("testing" == "testing" and "Zed" == "Cool Guy")
check_my_quess(True, not ("testing" == "testing" and "Zed" == "Cool Guy"))
# 1 == 1 and (not ("testing" == 1 or 1 == 0))
check_my_quess(True, 1 == 1 and (not("testing" == 1 or 1==0)))
# "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
check_my_quess(False, "chunky" == "bacon" and (not(3==4 or 3==3)))
# 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
check_my_quess(False, 3==3 and (not("testing" == "testing" or "Python" == "Fun")))