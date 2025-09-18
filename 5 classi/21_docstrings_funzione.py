def area_cerchio(r: float) -> float:
    """Calcola l'area di un cerchio di raggio r.

    Args:
        r: Il raggio (deve essere non negativo).

    Returns:
        L'area come float.

    Raises:
        ValueError: se r < 0.
    """
    if r < 0:
        raise ValueError("r deve essere >= 0")
    from math import pi
    return pi * r * r


print(area_cerchio.__doc__)
help(area_cerchio)  # mostra la docstring formattata