#method decorator
class My:
    count=0
    def increment(cls):
        cls.count+=1
        print(f"count is now {cls.count}")
print(cls.count)