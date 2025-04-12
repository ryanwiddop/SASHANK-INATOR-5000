import poplib
from email.parser import BytesParser
import sys

def check_pop3(server, username, password):
    try:
        # Connect to the POP3 server
        pop_conn = poplib.POP3(server)
        pop_conn.user(username)
        pop_conn.pass_(password)

        # Get the number of messages in the mailbox
        num_messages = len(pop_conn.list()[1])

        result = {
            "num_messages": num_messages,
            "subject": None,
            "from": None,
            "to": None
        }

        # Retrieve the headers of the first message
        if num_messages > 0:
            response, lines, octets = pop_conn.retr(1)
            msg_content = b'\r\n'.join(lines)
            msg = BytesParser().parsebytes(msg_content)
            result["subject"] = msg['subject']
            result["from"] = msg['from']
            result["to"] = msg['to']

        # Close the connection
        pop_conn.quit()
        return True, None
    except Exception as e:
        return False, e

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     sys.exit(1)

    server = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    result = check_pop3(server, username, password)
    if result[0]:
        print(f"succeeded with {username}")
        sys.exit(0)
    else:
        print(result[1])
        sys.exit(result[1])