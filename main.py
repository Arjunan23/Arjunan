import time
import scipy.stats as stats
import webbrowser
import os
import platform

def analyze_signal():
    print("📡 Initializing neural signal interface...")
    time.sleep(2)
    
    mu = 200
    sigma = 16  # std deviation
    threshold_1 = 210
    threshold_2 = 240

    # Conditional probability P(X > 240 | X > 210)
    prob = stats.norm.sf(threshold_2, loc=mu, scale=sigma) / stats.norm.sf(threshold_1, loc=mu, scale=sigma)

    print(f"📈 Signal probability computed: {prob*100:.4f}%")
    print("⚠️ Unusual signal strength detected!")
    time.sleep(2)

    # Play a prank (rickroll or surprise)
    print("🧠 Attempting signal decryption...")
    time.sleep(3)

    # Open Rickroll video
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)
    print("🎵 Signal decrypted successfully: Playing transmission...")

if __name__ == "__main__":
    analyze_signal()
