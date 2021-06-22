HEROKU = False  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    Bot_token = environ["Bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    Bot_token = "1722989298:AAF0mjgX_G1pI8R9_NnCg-Zk1Ui97XofkOk"
    ARQ_API_KEY = "DQDRUO-EGEFIC-TQQNNS-YWAHKA-ARQ"
