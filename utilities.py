# Function to convert WindowsPath to PosixPath

from pathlib import Path, WindowsPath

def windows_to_posix(path):
    """Converts a Windows path to a POSIX path.

    Args:
        path (str or Path): The path to convert.

    Returns:
        str: The POSIX path.
    """

    # Check if the path is a WindowsPath object
    if isinstance(path, WindowsPath):
        # Convert the WindowsPath object to a POSIX path
        return path.as_posix()
    elif isinstance(path, Path):
        # If it's a Path object, it might be a WindowsPath or PosixPath, use as_posix() to get POSIX path
        return path.as_posix()
    elif isinstance(path, str):
        # If it's a string, try to convert it to a Path object
        try:
            # Attempt to convert the path to a Path object. 
            # If it's a Windows path, it will be converted to a WindowsPath object.
            path = Path(path)
            # If it's a WindowsPath object, convert to POSIX
            if isinstance(path, WindowsPath):
                return path.as_posix()
            else:
                # If it's not a WindowsPath, just return the string
                return path
        except:
            # If the conversion fails, just return the original string
            return path
    else:
        # If the path is not a string, Path, or WindowsPath, return the original path
        return path
    
