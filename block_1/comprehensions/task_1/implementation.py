def flatten_list(matrix: list) -> list:
    """
    Преобразует матрицу (список списков) в линейный список.

    Args:
         matrix: список, элементами которого являются списки

    Returns:
        линейный список
    """
    return [matrix[i][j] for i in range(0, len(matrix)) for j in range(0, len(matrix[i]))]
