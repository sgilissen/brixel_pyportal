import time
from rpi_ws281x import Adafruit_NeoPixel, Color

# Configuration for the WS2812 LEDs (assuming a ring configuration)
LED_COUNT = 80        # Number of LEDs in your WS2812 ring
LED_PIN = 18          # GPIO pin connected to the data input of the WS2812 ring
LED_FREQ_HZ = 800000  # Frequency of the WS2812 LEDs
LED_DMA = 10          # DMA channel for the WS2812 LEDs
LED_BRIGHTNESS = 255  # Brightness (0-255)
LED_INVERT = False    # Invert signal (True or False)
LED_CHANNEL = 0       # Set to 1 for GPIOs 13, 19, 41, 45, or 53

# Create an instance of the Adafruit_NeoPixel class
strip = Adafruit_NeoPixel(
    LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL
)

# Initialize the strip
strip.begin()

# Define colors for the portal effect with different shades of blue
SHADES = [
    Color(0, 0, 0),
    Color(0, 0, 0),
    Color(0, 0, 0),
    Color(0, 0, 10),
    Color(0, 0, 20),
    Color(0, 0, 50),
    Color(0, 0, 100),
    Color(0, 0, 255),
    Color(0, 40, 255),
    Color(0, 60, 255),
    Color(0, 80, 255),
    Color(100, 255, 255),
    Color(200, 255, 255),
    #Color(200, 255, 255),
    # Add more shades of blue as needed
]

def rotate_shades():
    while True:
        for i in range(len(SHADES)):
            for j in range(len(strip)):
                strip.setPixelColor(j, SHADES[(i + j) % len(SHADES)])
            strip.show()
            time.sleep(0.1)  # Adjust the speed of rotation

if __name__ == "__main__":
    try:
        rotate_shades()
    except KeyboardInterrupt:
        # Turn off LEDs and exit gracefully on Ctrl+C
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

