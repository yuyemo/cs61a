def divide(quotients,divisor):
    return {q:[d for d in divisor if d%q==0] for q in quotients}

