
## Raw Observation of it working
At init:
```
Read 2 byte(s) from register 0x0 at address 0x53: 96,1
Writing 1 byte(s) to register 0x10 at address 0x53: 2
Read 1 byte(s) from register 0x10 at address 0x53: 2
Writing 1 byte(s) to register 0x11 at address 0x53: 0
Writing 2 byte(s) to register 0x13 at address 0x53: 137,74
Writing 2 byte(s) to register 0x15 at address 0x53: 0,100
```

At read TVOC:
```
Read 1 byte(s) from register 0x20 at address 0x53: 131
Read 6 byte(s) from register 0x20 at address 0x53: 129,2,174,0,148,2
```

At read AQI: 
```
Read 1 byte(s) from register 0x20 at address 0x53: 131
Read 6 byte(s) from register 0x20 at address 0x53: 129,2,176,0,151,2
```

At read ECO2:
```
Read 1 byte(s) from register 0x20 at address 0x53: 131
Read 6 byte(s) from register 0x20 at address 0x53: 129,2,176,0,150,2
```

## Reverse-Engineering how it works

### At Init:
- Reads 2 bytes from register `0x00`, validating device identity (96,1 are the correct bytes)
- Writes byte `2` to register `0x10`, turning the operating mode to on (sensing)
- Reads back byte `2` from register `0x10`, validating
