def val(value):
    if not (len(value) >= 9 and len(value) < 14):
        raise ValueError("Telefon Raqam xato kritilgan!!!z")

    else:
        return True
