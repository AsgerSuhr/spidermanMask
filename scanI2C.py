import machine
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
 
print('Scan i2c bus...')
devices = i2c.scan()
 
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))
 
  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    dev_id = i2c.writeto(device, b'x9')
    print(dev_id)
    dev_id = i2c.readfrom_mem(device, 0x92, 1)
    print(dev_id)