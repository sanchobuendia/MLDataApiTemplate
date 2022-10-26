from loguru import logger


def sum(num_1, num_2):
    try:
        result = num_1 + num_2
        return {"result": result}
    except:
        raise Exception("Error to sum numbers")
