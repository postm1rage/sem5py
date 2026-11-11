import time
from datetime import datetime
import schedule


def print_ku():
    hour = datetime.now().hour
    count = hour % 12 or 12
    print("Ку" * count)


def main():
    schedule.every().hour.at(":00").do(print_ku)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
