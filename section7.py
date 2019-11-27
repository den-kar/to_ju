# #############################################################################
# ### Imports

import operator


# #############################################################################
# ### Resource Class

class Resource:
  def __init__(self, name, manufacturer, total, allocated):
    self._name = str(name).strip()
    self._manufacturer = str(manufacturer).strip()
    if self._validate_data(total, raise_error=True):
      self._total = total
    if self._validate_data(allocated, raise_error=True):
      self._allocated = allocated
  
  
  @property
  def name(self):
    return self._name
  
  @property
  def manufacturer(self):
    return self._manufacturer
  
  @property
  def total(self):
    return self._total
  
  @property
  def allocated(self):
    return self._allocated
  
  
  def __str__(self):
    return f'{self.__class__.__name__}({self.name})'
  
  def __repr__(self):
    return f'{self.__class__.__name__}(name={self.name}, manufacturer={self.manufacturer}, total={self.total}, allocated={self.allocated})'
  
  
  def _validate_data(self, n, to_compare=None, *, raise_error=False):
    try:
      if not isinstance(n, int):
        raise TypeError('value must be of type integer.')
      if n < 0:
        raise ValueError('n must be positive')
      if to_compare and n > to_compare:
        raise ValueError(f'value must be less than or equal to {to_compare}')
    except Exception as ex:
      print(ex)
      if raise_error:
        raise
      return False
    else:
      return True
  
  def _aggregate_data(self, n, to_update, op):
    return op(to_update, n)
  
  
  def claim(self, n):
    if self._validate_data(n, self._total):
      self._total = self._aggregate_data(n, self._total, operator.isub)
      self._allocated = self._aggregate_data(n, self._allocated, operator.iadd)
  
  def freeup(self, n):
    if self._validate_data(n, self._allocated):
      self._total = self._aggregate_data(n, self._total, operator.iadd)
      self._allocated = self._aggregate_data(n, self._allocated, operator.isub)
  
  def died(self, n):
    if self._validate_data(n, self.total):
      self._total = self._aggregate_data(n, self._total, operator.isub)
  
  def purchased(self, n):
    if self._validate_data(n):
      self._total = self._aggregate_data(n, self._total, operator.iadd)
  
  @property
  def category(self):
    return self.__class__.__name__.lower()


r1 = Resource('Intel Core i9-9900k', 'Intel', 50, 20)

# print(f'Start: total: {r1.total}, allocated: {r1.allocated}')
# r1.freeup(19)
# print(f'freeup(19): total: {r1.total}, allocated: {r1.allocated}')
# r1.died(30)
# print(f'died(30): total: {r1.total}, allocated: {r1.allocated}')
# r1.claim(19)
# print(f'claim(19): total: {r1.total}, allocated: {r1.allocated}')
# r1.purchased(30)
# print(f'purchased(30): total: {r1.total}, allocated: {r1.allocated}')
# r1.claim(100)
# print(f'claim(100): total: {r1.total}, allocated: {r1.allocated}')
# r1.freeup(100)
# print(f'freeup(100): total: {r1.total}, allocated: {r1.allocated}')
# r1.died(100)
# print(f'died(100): total: {r1.total}, allocated: {r1.allocated}')

# print(r1.__str__())
# print(r1.__repr__())


# #############################################################################
# ### CPU Class

class CPU(Resource):
  def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
    super().__init__(name, manufacturer, total, allocated)
    
    if self._validate_data(cores, raise_error=True):
      self._cores = cores
    self._socket = str(socket).strip()
    if self._validate_data(power_watts, raise_error=True):
      self._power_watts = power_watts
  
  @property
  def cores(self):
    return self._cores
  
  @property
  def socket(self):
    return self._socket
  
  @property
  def power_watts(self):
    return self._power_watts

cpu = CPU('Intel Core i9-9900k', 'Intel', 50, 20, 8, 'AM4', 94)
print(cpu.__repr__())

print(f'Start: total: {cpu.total}, allocated: {cpu.allocated}')
cpu.freeup(19)
print(f'freeup(19): total: {cpu.total}, allocated: {cpu.allocated}')
cpu.died(30)
print(f'died(30): total: {cpu.total}, allocated: {cpu.allocated}')
cpu.claim(19)
print(f'claim(19): total: {cpu.total}, allocated: {cpu.allocated}')
cpu.purchased(30)
print(f'purchased(30): total: {cpu.total}, allocated: {cpu.allocated}')
cpu.claim(100)
print(f'claim(100): total: {cpu.total}, allocated: {cpu.allocated}')
cpu.freeup(100)
print(f'freeup(100): total: {cpu.total}, allocated: {cpu.allocated}')
cpu.died(100)
print(f'died(100): total: {cpu.total}, allocated: {cpu.allocated}')

print(cpu.__str__())
print(cpu.__repr__())


# #############################################################################
# ### Storage Class

class Storage(Resource):
  def __init__(self, name, manufacturer, total, allocated, capacity_GB):
    super().__init__(name, manufacturer, total, allocated)
    if self._validate_data(capacity_GB, raise_error=True):
      self._capacity_GB = capacity_GB
  
  @property
  def capacity_GB(self):
    return self._capacity_GB

storage = Storage('Fak0_A320GB_7200', 'Western Digital', 50, 20, 320)
print(storage.__repr__())

print(f'Start: total: {storage.total}, allocated: {storage.allocated}')
storage.freeup(19)
print(f'freeup(19): total: {storage.total}, allocated: {storage.allocated}')
storage.died(30)
print(f'died(30): total: {storage.total}, allocated: {storage.allocated}')
storage.claim(19)
print(f'claim(19): total: {storage.total}, allocated: {storage.allocated}')
storage.purchased(30)
print(f'purchased(30): total: {storage.total}, allocated: {storage.allocated}')
storage.claim(100)
print(f'claim(100): total: {storage.total}, allocated: {storage.allocated}')
storage.freeup(100)
print(f'freeup(100): total: {storage.total}, allocated: {storage.allocated}')
storage.died(100)
print(f'died(100): total: {storage.total}, allocated: {storage.allocated}')

print(storage.__str__())
print(storage.__repr__())


# ### HDD Class

class HDD(Storage):
  def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
    super().__init__(name, manufacturer, total, allocated, capacity_GB)
    self._size = str(size).strip()
    if self._validate_data(rpm, raise_error=True):
      if not (rpm > 2000 and rpm < 10300):
        raise ValueError('no such HDD available')
      self._rpm = rpm
  
  @property
  def size(self):
    return self._size
  
  @property
  def rpm(self):
    return self._rpm

hdd = HDD('Fak0_A320GB_7200', 'Western Digital', 50, 20, 320, size=2.5, rpm=7200)
print(hdd.__repr__())

print(f'Start: total: {hdd.total}, allocated: {hdd.allocated}')
hdd.freeup(19)
print(f'freeup(19): total: {hdd.total}, allocated: {hdd.allocated}')
hdd.died(30)
print(f'died(30): total: {hdd.total}, allocated: {hdd.allocated}')
hdd.claim(19)
print(f'claim(19): total: {hdd.total}, allocated: {hdd.allocated}')
hdd.purchased(30)
print(f'purchased(30): total: {hdd.total}, allocated: {hdd.allocated}')
hdd.claim(100)
print(f'claim(100): total: {hdd.total}, allocated: {hdd.allocated}')
hdd.freeup(100)
print(f'freeup(100): total: {hdd.total}, allocated: {hdd.allocated}')
hdd.died(100)
print(f'died(100): total: {hdd.total}, allocated: {hdd.allocated}')

print(hdd.__str__())
print(hdd.__repr__())


# ### SSD Class

class SSD(Storage):
  def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
    super().__init__(name, manufacturer, total, allocated, capacity_GB)
    self._interface = str(interface).strip()
  
  @property
  def interface(self):
    return self._interface

ssd = SSD('Evo 830i 240GB', 'Samsung', 100, 250, 240, interface='PCIe NVMe 3.0 x4')
print(ssd.__repr__())

print(f'Start: total: {ssd.total}, allocated: {ssd.allocated}')
ssd.freeup(19)
print(f'freeup(19): total: {ssd.total}, allocated: {ssd.allocated}')
ssd.died(30)
print(f'died(30): total: {ssd.total}, allocated: {ssd.allocated}')
ssd.claim(19)
print(f'claim(19): total: {ssd.total}, allocated: {ssd.allocated}')
ssd.purchased(30)
print(f'purchased(30): total: {ssd.total}, allocated: {ssd.allocated}')
ssd.claim(100)
print(f'claim(100): total: {ssd.total}, allocated: {ssd.allocated}')
ssd.freeup(100)
print(f'freeup(100): total: {ssd.total}, allocated: {ssd.allocated}')
ssd.died(100)
print(f'died(100): total: {ssd.total}, allocated: {ssd.allocated}')

print(ssd.__str__())
print(ssd.__repr__())
