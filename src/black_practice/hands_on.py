import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)


def divide_funds(total: int | float, parts: int | float) -> float | None:
    """Divides total funds into parts.

    Args:
        total (float, int): The total number.
        parts (float, int): The number to divide it to.

    Returns:
        float: The dividend for each parts.
        None: If there are errors
    """
    try:
        answer = total / parts
        logger.info("Calculation successful")
        logger.info("The result is: %s", answer)
        return answer
    except ZeroDivisionError as err:
        logger.exception(type(err).__name__)
    except TypeError as err:
        logger.exception(type(err).__name__)

    return None


if __name__ == "__main__":# pragma: no cover 
    divide_funds(100, 10)
    divide_funds(100, 0)
    divide_funds(10, 2.5)
    
