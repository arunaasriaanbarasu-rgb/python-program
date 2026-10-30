seat=int(input())
seatnumber=seat%8
match seatnumber:
  case 1:
    print("LB")
  case 2:
    print("MB")
  case 3:
    print("UB")
  case 4:
    print("LB")
  case 5:
    print("MB")
  case 6:
    print("UB")
  case 7:
    print("SL")
  case 0:
    print("SU")
  case _:
    print("INVALID")
