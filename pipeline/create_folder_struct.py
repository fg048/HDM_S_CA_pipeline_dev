
try:
    from OS import *

except OSError:
    pass


class Folder_creator(Object):

    def __init__(self, r_path):
        self.root_path = r_path

    def create_folder(self, fpath, fname):
        pass

    def combo_onActivated(self, text):
        self.cmd = 'poly' + text + '()'


def main():
    folderstruct = Folder_creator()
    folderstruct.create_folder()


if __name__ == '__main__':
    main()
