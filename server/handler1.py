import asyncio
from datetime import datetime


class SaveHandler:

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        if not address.endswith('@fast.il'):
            return '550 not relaying to that domain'
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        time_str = str(datetime.now())[:19]
        for rcpt in envelope.rcpt_tos:
            file_name = f"{rcpt.split('@')[0]}/{time_str}-{envelope.mail_from}"
            with open(f"inbox/{file_name}", "w") as file:
                file.write(envelope.content.decode('utf8', errors='replace'))
        return '250 Message accepted for delivery'