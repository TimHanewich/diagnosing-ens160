import time
import machine

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))
print(i2c.scan())

def loop() -> None:
    print("This loop does not place the ENS160 in operating mode 2 (reading). So be sure to do that before if you have not done it already!")
    start_at:int = time.ticks_ms()
    failures:int = 0
    while True:

        # read
        data = i2c.readfrom_memory(0x53, 0x20, 5) # AQI (1 byte), TVOC (2 bytes), ECO2 (2 bytes)

        # handle
        if data[0] == 0 and data[1] == 0 and data[2] == 0 and data[3] == 0 and data[4] == 0:
            failures = failures + 1
            seconds_elapsed:float = (time.ticks_ms() - start_at) / 60
            minutes_elapsed:float = seconds_elapsed / 60
            hours_elapsed:float = minutes_elapsed / 60
            failures_per_hour:float = failures / hours_elapsed
            print("No data! Sensor not working! That is now " + str(failures) + " failure(s) in " + str(minutes_elapsed) + " minutes, averaging " + str(round(failures_per_hour, 1)) + " failures per hour")
            print("Restoring operating mode to 2...")
            i2c.writeto_mem(0x53, 0x10, bytes([2]))
            print("Op Mode restores to 2. Waiting 10 seconds before proceeding...")
            time.sleep(10)
        else:
            print("Data collected successfully: " + str(data))

        # sleep 
        time.sleep(1)
