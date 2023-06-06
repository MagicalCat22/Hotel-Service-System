def checkt(ans):
    if ans.count(1) == 0 and ans.count(2) == 0 and ans.count(3) == 0 and ans.count(4) == 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0:
        return 0
    if (ans.count(1) == 0 and ans.count(2) == 0 and ans.count(3) == 0 and ans.count(4) > 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0):
         return 1
    if (ans.count(1) > 0 and ans.count(2) > 0 and ans.count(3) == 0 and ans.count(4) == 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0) or \
        (ans.count(1) > 0 and ans.count(2) > 0 and ans.count(3) == 0 and ans.count(4) > 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0):
        return 2
    if (ans.count(1) == 0 and ans.count(2) == 0 and ans.count(3) > 0 and ans.count(4) == 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0):
        return 3
    if (ans.count(1) > 0 and ans.count(2) > 0 and ans.count(3) > 0 and ans.count(4) > 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0):
        return 4
    if(ans.count(1) == 0 and ans.count(2) == 0 and ans.count(3) == 0 and ans.count(4) == 0 and ans.count(5) > 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0):
        return 5
    if(ans.count(1) == 0 and ans.count(2) == 0 and ans.count(3) == 0 and ans.count(4) == 0 and ans.count(5) == 0 and ans.count(6) > 0 and ans.count(7) == 0 and ans.count(8) == 0 and ans.count(9) == 0):
        return 6
    if(ans.count(1) == 0 and ans.count(2) == 0 and ans.count(3) == 0 and ans.count(4) == 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) > 0 and ans.count(8) == 0 and ans.count(9) == 0):
        return 7
    if(ans.count(1) > 0 and ans.count(2) == 0 and ans.count(3) == 0 and ans.count(4) == 0 and ans.count(5) == 0 and ans.count(6) == 0 and ans.count(7) == 0 and ans.count(8) > 0 or ans.count(9) > 0):
        return 8