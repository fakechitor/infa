def printTime(secs : int) -> None:
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")


printTime(3599)
printTime(34262)