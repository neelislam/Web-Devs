version = input("Press Y and enter to know your Python version:")


if ( version == 'Y' or version == 'y'):
    import sys
    print("Your Python version is:")
    print (sys.version)
    print("Version info.")
    print (sys.version_info)
else:
    print("You didn't press Y or y. Exiting...")    