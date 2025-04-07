import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
button_pin = 18  # GPIO pin connected to the button
counter = 0

# LCD setup (optional)
try:
    from lcd_library import LCD  # Import your LCD library
    lcd = LCD()  # Initialize LCD
    use_lcd = True
except ImportError:
    print("LCD library not found. Defaulting to serial monitor.")
    use_lcd = False

# Set up button pin with pull-down resistor
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Press the button to increment the counter. Press Ctrl+C to exit.")
    if use_lcd:
        lcd.clear()
        lcd.display("Counter: 0")

    while True:
        if GPIO.input(button_pin) == GPIO.HIGH:
            counter += 1
            print(f"Counter: {counter}")
            
            # Update LCD (if connected)
            if use_lcd:
                lcd.display(f"Counter: {counter}")
                
            time.sleep(0.3)  # Debounce delay
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()
    if use_lcd:
        lcd.clear()
