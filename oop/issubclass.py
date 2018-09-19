class Base:
    pass
class Derived(Base):
    pass

print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d = Derived()
b = Base()

print(isinstance(b,Derived))
print(isinstance(d,Base))
