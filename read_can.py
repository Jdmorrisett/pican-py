import can
import time

def main():
  # Define CAN interface using MCP2515 and SPI on Raspberry Pi
  can_interface = "socketcan"
  channel = "can0"
  bus = can.interface.Bus(channel=channel, bustype=can_interface, bitrate=1000000)

  # Open a candump file for writing
  candump_filename = "candump.log"
  with open(candump_filename, "w") as candump_file:
    try:
      print("Press Ctrl+C to exit")
      while True:
        message = bus.recv(1)  # Receive CAN message with timeout of 1 second

        if message:
          candump_line = f"{message.timestamp}  {message.arbitration_id:08X}   {' '.join(format(byte, '02X') for byte in message.data)}"
          print(candump_line)
          candump_file.write(candump_line + "\n")
          candump_file.flush()

    except KeyboardInterrupt:
      print("\nExiting...")

if __name__ == "__main__":
  main()
