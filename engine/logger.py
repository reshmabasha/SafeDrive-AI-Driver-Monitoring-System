import csv
import os
from datetime import datetime


class EventLogger:

    def __init__(self):

        self.log_dir = "logs"
        self.log_file = os.path.join(self.log_dir, "events.csv")

        os.makedirs(self.log_dir, exist_ok=True)

        if not os.path.exists(self.log_file):

            with open(self.log_file, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Risk Score",
                    "Driver Status",
                    "Reason"
                ])

    def log(self, reason, risk_score, driver_status):

        with open(self.log_file, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                risk_score,
                driver_status,
                reason
            ])
