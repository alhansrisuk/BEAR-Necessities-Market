"""
This file (test_mail.py) contains the unit tests for the Sendgrid mail functionality.
"""

"""
GIVEN a default sender email, a send-to email, a subject line, and body text
WHEN a sending an email
THEN check that the send_email method is appropriately called.
"""
def test_send_email(mail_with_send_email_mocked):
    # Calls mocked send_email with parameters for email addresses, subject line, and body text
    mail_with_send_email_mocked.send_email("default_from@test.com", "default_to@test.com", "subject_line_test", "text_body_test")

    # Verifies that it was called correctly
    mail_with_send_email_mocked.send_email.assert_called_with("default_from@test.com", "default_to@test.com", "subject_line_test", "text_body_test")