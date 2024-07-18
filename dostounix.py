def unixFormat(file):
    WIN_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'

    try:
        with open(file, 'rb') as openfile:
            output = openfile.read()
        output = output.replace(WIN_LINE_ENDING, UNIX_LINE_ENDING)
        with open(file, 'wb') as openfile:
            openfile.write(output)
        print("Windows line endings removed from {}\n".format(file))
    except Exception as e:
        raise
    return

    # Calling the function with three arguments
unixFormat(file="$(Build.ArtifactStaginfDirectory)/*")
