class dog:
    def run(self):
        print("It runs")
    def bark(self):
        print("It Barks Badly")

class cat:
    def cute(self):
        print("Cats Are Cute")
    def bark(self):
        print("Cts don't bark")
def bark_test(ani):
    ani.bark()

dg= dog()
ct=cat()

bark_test(dg)
bark_test(ct)
