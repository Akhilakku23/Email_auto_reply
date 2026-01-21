def generate_reply(subject, body):
    subject = (subject or "").lower()
    body = (body or "").lower()

    if "payment" in subject or "invoice" in body:
        return (
            "Hello,\n\n"
            "Thank you for your message regarding payment or billing. "
            "I will review the details and get back to you shortly.\n\n"
            "Best regards,\n"
            "Akhil Saji"
        )

    elif "support" in subject or "help" in body or "issue" in body:
        return (
            "Hello,\n\n"
            "Thank you for reaching out for support. "
            "I have noted your concern and will assist you as soon as possible.\n\n"
            "Best regards,\n"
            "Akhil Saji"
        )

    elif "meeting" in subject or "schedule" in body:
        return (
            "Hello,\n\n"
            "Thank you for your email regarding the meeting. "
            "I will check my availability and get back to you shortly.\n\n"
            "Best regards,\n"
            "Akhil Saji"
        )

    else:
        return (
            "Hello,\n\n"
            "Thank you for your email. I have received your message "
            "and will get back to you shortly.\n\n"
            "Best regards,\n"
            "Akhil Saji"
        )
