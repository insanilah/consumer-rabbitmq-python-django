from multiprocessing import Process
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from consumers import article_notification_consumer, user_registration_consumer

if __name__ == "__main__":
    Process(target=article_notification_consumer).start()
    Process(target=user_registration_consumer).start()
