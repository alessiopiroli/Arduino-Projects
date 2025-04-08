import serial
import subprocess

microcontroller_port = 'your_com_port'
baud_rate = your_baud_rate

ser = serial.Seril(microcontroller_port, baud_rate, timeout = 1)

def run_script():
    print("Running the script")
    subprocess.run(['python', r'path_to_noise_script'])

try:
    while True:
        message = ser.readline().decode('utf-8').strip()
        if message == "RUN_SCRIPT":
            run_script()

except KeyboardInterrupt:
    printing("Quit")

finally:
    ser.close()
