import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "13949344"))
API_HASH = os.getenv("API_HASH", "408723003ad67fa8ab01ccc7f53e24ad")
SESSION = os.getenv("SESSION", "BAAwsHAmAK4Dz1hikUduCrzYXuorZuRgxIBOjoy_RPD_WUtDiNcbUd_dpHbFzlQwmm-6JGkEm9Khy2FWVdaL7SuT1flIG9hRt0LPrb1xy2mWNc9n7uHTsEropKw8_CqGunoACCAVC-2n5-XGRoOPUSc3UKExmx1gfpYJhnFZ4V4x5xZOFKtaaVBdfu1lIh5YxGjbWLjdVLTsjSubYl883p6NYV8VSh2-ASNuG0-02XmImxMpLZAXChESZcYrkcivL0D6ikiomYxuzGrCwY0SEL2WQYTmef_wbSSKeRq-r8pRoxMHfTFRHALthy3ny5HFvIgmvox1ITQvTGa-04c4z5wGAAAAAYXLxXsA")
HNDLR = os.getenv("HNDLR", "/")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AsadAlexaVCBot"))
call_py = PyTgCalls(bot)
