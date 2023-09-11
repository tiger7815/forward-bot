import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQChAYUAw7KemilgEPykyLqj0y-8wWw2ythlERfecRfzIEosBvFm0_5ia73-5QWHKdwcgRT6Qsx6q7K9xFh_VcBLVlTybQMl9h9Ldposa4OC7lsHoD_WfpFxbpqX9Bdr-w0BOlS4-wT40t3PRQ-K_g_RA2jJXMOUyXGXMONl6DxTd0XJ3FA4xXzYagtakV3h7e8QhKyYA0-Y8ELDHEada-IyL9moKN8qJGvERokDKq0zs-aBJ33U6EfDKsdhxCYENgfy2Ne6AQZ01fuX5_jWlsjx6E94mCgPouOhYZo__Ys_8iPbWPiDZaHtztR-BsoVnA4BE-TLDy7xLq4iAoxsIB1K-qYC3gAAAAB1wruNAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
