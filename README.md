# PUSH-BUTTON-COUNTER
NAME : AAKINA LAKSHMI PRADEEP

COMPANY : CODTECH IT SOLUTIONS

INTERN ID : CT06WR44

DOMAIN : EMBEDDED SYSTEMS

DURATION : MARCH 30th, 2025 to MAY 15th, 2025 (6 WEEKS)

MENTOR : NEELA SANTHOSH

OVERVIEW : PUSH-BUTTON-COUNTER

To created a push-button counter using an embedded system microcontroller, here's a complete guide covering the hardware setup, software implementation, and displaying the count on an LCD or serial monitor.

---

### **Components Needed**
1. **Microcontroller**: Raspberry Pi, Arduino, or ESP32 (e.g., Raspberry Pi is used in this example).
2. **Push Button**: Connects to the GPIO pin.
3. **Resistors**: Use a pull-down resistor for stabilizing the button signal.
4. **LCD Display (Optional)**: To display the count (e.g., 16x2 LCD).
5. **Wires**: For connections.
6. **Power Supply**: Microcontroller's power source.

---

### **Circuit Diagram**
The basic setup includes:
1. Connect one terminal of the push button to the GPIO pin.
2. The other terminal of the push button is connected to **GND (ground)**.
3. A **pull-down resistor** (e.g., 10kΩ) is added between the GPIO pin and ground to avoid floating states.
4. If using an LCD display:
   - Connect the LCD to the I2C pins (SDA and SCL) or directly to digital pins for parallel communication.
  ![circuit design](https://github.com/user-attachments/assets/2e5fbf9a-d2aa-4997-92e4-00ea05148084)


