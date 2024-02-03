class AC:
    def AC_cool(self):
        pass
    def AC_hot(self):
        pass
    def AC_wind(self):
        pass
class mides_AC(AC):
    def AC_cool(self):
        print("美的空调制冷")
    def AC_hot(self):
        print("美的空调制热")
    def AC_wind(self):
        print("美的空调左右摆风")
class Gree_AC(AC):
    def AC_cool(self):
        print("格力空调制冷")
    def AC_hot(self):
        print("格力空调制热")
    def AC_wind(self):
        print("格力空调左右摆风")
def AC_hot(AC):
    AC.AC_hot()

Gree = Gree_AC()
mides = mides_AC()
AC_hot(Gree)
AC_hot(mides)