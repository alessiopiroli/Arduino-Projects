import serial
import subprocess

microcontroller_port = 'COM4'
baud_rate = 9600

ser = serial.Seril(microcontroller_port, baud_rate, timeout = 1)

def run_script():
    print("Executing the Python script...")
    subprocess.run(['python', r'\Users\aless\Desktop\Arduino projects\noise_script.py'])

try:
    while True:
        message = ser.readline().decode('utf-8').strip()
        if message == "RUN_SCRIPT":
            run_script()

except KeyboardInterrupt:
    printing("Exiting...")

finally:
    ser.close()
