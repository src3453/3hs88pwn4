import math

out = []
for i in range(256):
  out.append(int(math.sin(math.radians(float(i)/256*360))*127+128))

print(" ".join(["{:02X}".format(i) for i in out]))