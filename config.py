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
    SESSION = os.environ.get("SESSION", "BQBGgbbYXzSajv_XzCRDxHn7XWoeNf5yWFo-j6GaQsQlka2TosNtKvSwjcaY1w3giun-KhXX_GpDPncBCbhoSwqYyYTmNH5oUDMGVNPoBUXaipidTy8ouQDDqdHQ7GMlfh1LmILasASPeXFQiTX6eEz8gr9K376yCSN0LrRiWt6EDXAbj90Vz3KTiWWeD8wSugGet8MGTx5GI8fsqapxGI2f9LaXcQJ7wPk97Vvybfu_uJOKjJJvovwJVxn-YWCWoi-pWuKYJ7Q9j4LNJxqm7GhWtNTo_K7uXDJqTdC2Z-YxKiWfwdnZLJYjACRnVJgNbolXI9OzTIoQeiMf0mQIDZLodcK7jQA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
