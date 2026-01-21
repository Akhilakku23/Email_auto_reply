# import time
# from config import CHECK_INTERVAL
# from reader import read_unread_emails
# from sender import send_reply
# from model_ai import generate_ai_reply

# def main_loop():
#     replied_senders = set()  # avoid replying multiple times
    
#     while True:
#         try:
#             unread_emails = read_unread_emails()
#             if not unread_emails:
#                 print("No new emails. Waiting...")
            
#             for sender, subject, body in unread_emails:
#                 if sender not in replied_senders:
#                     reply_text = generate_ai_reply(subject, body)
#                     send_reply(sender, reply_text, subject)
#                     replied_senders.add(sender)
#         except Exception as e:
#             print("Error:", e)
        
#         time.sleep(CHECK_INTERVAL)

# if __name__ == "__main__":
#     print("Starting GPT-Powered Email Auto-Reply Assistant...")
#     main_loop()
import time
from config import CHECK_INTERVAL
from reader import read_unread_emails
from sender import send_reply
from reply_model import generate_reply
from model_ai import generate_ai_reply

def main_loop():
    replied_senders = set()

    while True:
        try:
            unread_emails = read_unread_emails()

            if not unread_emails:
                print("No new emails. Waiting...")

            for sender, subject, body in unread_emails:
                if sender in replied_senders:
                    continue

                # 1️⃣ Try rule-based reply first
                reply_text = generate_reply(subject, body)

                # 2️⃣ If no rule matched → use AI
                if reply_text is None:
                    print("No rule matched. Using AI reply.")
                    reply_text = generate_ai_reply(subject, body)
                else:
                    print("Rule-based reply used.")

                send_reply(sender, reply_text, subject)
                replied_senders.add(sender)

        except Exception as e:
            print("Error:", e)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("Starting Hybrid Email Auto-Reply Assistant...")
    main_loop()
