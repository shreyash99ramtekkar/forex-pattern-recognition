
import requests
from constants import notifications_constants;

from logger.FxPatternRecognitionLogger import FxPatternRecognitionLogger

fxstreetlogger = FxPatternRecognitionLogger()
logger = fxstreetlogger.get_logger(__name__)

class Telegram:
    def __init__(self):
        self.token = notifications_constants.TELEGRAM_TOKEN;
        self.chat_id= notifications_constants.TELEGRAM_CHAT_ID
        self.base_url = "https://api.telegram.org/bot" + self.token 
    
    def sendMessage(self,message):
        url = self.base_url + "/sendMessage?chat_id=" + self.chat_id + "&text=" + message 
        print(requests.get(url).json()) # this sends the message

    def sendImageCaption(self,image_file,message):
        url = self.base_url+"/sendPhoto"
        parameters = {
                "chat_id": self.chat_id,
                "caption": message
            }
        resp = requests.get(url,params=parameters,files=image_file)
        print(resp.text)