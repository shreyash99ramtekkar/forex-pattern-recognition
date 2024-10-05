from logger.FxPatternRecognitionLogger import FxPatternRecognitionLogger
from notifications.Telegram import Telegram;

fxstreetlogger = FxPatternRecognitionLogger()
logger = fxstreetlogger.get_logger(__name__)

telegram_obj = Telegram();


def main():
    logger.debug("This is my message to the world");
    telegram_obj.sendMessage('Pattern Recognition working')


if __name__ == "__main__":
    main()