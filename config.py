import os
import logging
class Config:                                                                   
    API_ID          = "10551685"
    API_HASH        = "477dff815fdc7cba803c1bc02c459d03"
    BOT_TOKEN       = "6400468647:AAGzWdp0hHnPvwPol7iXQ-NlABDXCNcWIyY"
    BOT_SESSION     = "forwardbot"
    OWNER_ID        = "1975696269"
    SESSION         = "BQBGgbbYXzSajv_XzCRDxHn7XWoeNf5yWFo-j6GaQsQlka2TosNtKvSwjcaY1w3giun-KhXX_GpDPncBCbhoSwqYyYTmNH5oUDMGVNPoBUXaipidTy8ouQDDqdHQ7GMlfh1LmILasASPeXFQiTX6eEz8gr9K376yCSN0LrRiWt6EDXAbj90Vz3KTiWWeD8wSugGet8MGTx5GI8fsqapxGI2f9LaXcQJ7wPk97Vvybfu_uJOKjJJvovwJVxn-YWCWoi-pWuKYJ7Q9j4LNJxqm7GhWtNTo_K7uXDJqTdC2Z-YxKiWfwdnZLJYjACRnVJgNbolXI9OzTIoQeiMf0mQIDZLodcK7jQA"
    DATABASE_URI    = "mongodb+srv://power:power@cluster0.ncgr0eh.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME   = "Cluste0"
    COLLECTION_NAME = "Data"
    TO_CHANNEL      = "-1001643263442"
    BOT_USERNAME    = "forwardbypj_bot"





def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
