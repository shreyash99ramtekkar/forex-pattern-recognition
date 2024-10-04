from logger.FxPatternRecognitionLogger import FxPatternRecognitionLogger

fxstreetlogger = FxPatternRecognitionLogger()
logger = fxstreetlogger.get_logger(__name__)


def main():
    print('message')
    logger.debug("This is my message to the world");


if __name__ == "__main__":
    main()