import tkinter as tk
import speedtest

# Function to perform the speed test
def speed_test_command():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    download_speed_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_speed_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping:.2f} ms")

# Create main window
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("400x300")
root.configure(background="#3b4370")

# Create title label
title_label = tk.Label(root, text="Internet Speed Test", font="Arial 16 bold", bg="#3b4370", fg="#ffffff")
title_label.pack(pady=10)

# Create labels for download speed, upload speed, and ping
download_speed_label = tk.Label(root, text="Download Speed: 0.00 Mbps", bg="#3b4370", fg="#ffd700")
download_speed_label.pack(pady=10)

upload_speed_label = tk.Label(root, text="Upload Speed: 0.00 Mbps", bg="#3b4370", fg="#ffd700")
upload_speed_label.pack(pady=10)

ping_label = tk.Label(root, text="Ping: 0.00 ms", bg="#3b4370", fg="#ffd700")
ping_label.pack(pady=10)

# Create button to start the speed test
start_button = tk.Button(root, text="Start Test", command=speed_test_command, font="Arial 12")
start_button.pack(pady=20)

# Run the main loop
root.mainloop()