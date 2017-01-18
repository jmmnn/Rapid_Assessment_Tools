import tempfile, subprocess, os

class pdf_to_text():

    def __init__(self, root_path):
        self.root_path = root_path
        self.files = []

    def find_all(self):

        dir_list = os.walk(self.root_path)
        file_path = []

        for root, dirs, files in dir_list:
            for file in files:
                self.files.append(os.path.join(root, file))

    def convert(self):

        self.find_all()

        for file in self.files:

            output = tempfile.NamedTemporaryFile()
            output_file = os.path.split(file)[0] + '/' + os.path.split(file)[1].replace('.pdf', '.txt')

            out, err = subprocess.Popen(['pdftotext', '-layout', file, output.name]).communicate()

            pdf = output.read()

            pdf = pdf.decode('windows-1252')

            with open(output_file, 'w') as f:
                f.write(pdf)


root_path = '/Users/maxwelllee54/GitHubs/Rapid_Assessment_Tools/SharedFiles/Fordham'

pdf = pdf_to_text(root_path).convert()
