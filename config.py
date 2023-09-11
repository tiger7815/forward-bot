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
    SESSION = os.environ.get("SESSION", "BQCR924ArSg4TglBmRLk0ZtxMnxUZrTU9NEZIWOHeU4us0LV8hsQMt2wBRiwDBfDSiUan84XONY1_jTDVe4AkPF-4K-ICFIKzS6Nvzv_Lg-fbQ0Mg32kRqKXizIYlN1bQ29VBHyLbPkgyB0ho19rg-CqZCQeb4s3wuq1LEobwx667V1rLfHHQpRE0GHD4X4ZZEYFeGvkgLMytPtyRdj9ve1ZaPHQRyHtFo0XNKtl895oxsPiO9-ZeGZ7no2Eg-XkHUZP6XZoFY1iyDVp1fQoKQYwgzIG3qxzXyQcvzkLB6Hs0gLIJnId36ZIptHQ1Vwlln5uCuVvBVrNToVfRcOTTvP8Gu424QAAAAFoyKurAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
