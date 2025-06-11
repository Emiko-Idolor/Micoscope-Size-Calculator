def calculate_real_size(microscope_size, magnification):
    if magnification <= 0:
        raise ValueError("Magnification must be greater than 0")
    return microscope_size / magnification
