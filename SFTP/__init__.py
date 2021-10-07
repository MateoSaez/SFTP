import pysftp
import io

class Connection(pysftp.Connection):

    def __init__(self, host, username, pwd):
        super().__init__(host, username=username,password=pwd)
        self.file_names = []
        self.dir_names = []
        self.un_name = []
        self.walktree("", self._store_files_name, self._store_dir_name, self._store_other_file_types)

    def _store_files_name(self, fname):
        self.file_names.append(fname)

    def _store_dir_name(self, dirname):
        self.dir_names.append(dirname)

    def _store_other_file_types(self, name):
        self.un_name.append(name)

    def get_file(self, f_name):
        bf = io.BytesIO()
        self.getfo(f_name, bf)
        bf.seek(0)
        return bf