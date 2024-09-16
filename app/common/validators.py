from app.errors.services import FileExtensionNotValid

class FileValidator:
    FILES = None
    VALID_IMG_EXT = ('.jpg', '.jpeg', '.png', '.tiff')
    VALID_FILE_EXT = ('.doc', '.docx', '.odt', '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt')
    VALID_VIDEO_EXT = ('.mp4',)

    VALID_EXT = ()

    def __init__(self, _types, files):
        if type(_types) == str:
            _type = list(_types)
        if 'img' in _types:
            self.VALID_EXT += self.VALID_IMG_EXT
        if 'file' in _types:
            self.VALID_EXT += self.VALID_FILE_EXT
        if 'video' in _types:
            self.VALID_EXT += self.VALID_VIDEO_EXT
        self.FILES = files

    

    def validate_ext(self):
        print(self.VALID_EXT)
        for file in self.FILES:
            if not file.name.lower().endswith(self.VALID_EXT):
                print("Nedozvoljena vrsta dokumenta")
                raise FileExtensionNotValid()
        return True

    def validate(self):
        self.validate_ext()
        return True

    def __str__(self) -> str:
        print(self.VALID_EXT)
        return 'self.VALID_EXT'