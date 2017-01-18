import tempfile, subprocess, os

class pdf_to_text():

    def __init__(self, root_path):
        self.root_path = root_path
        self.files = []

    def all_pdf(self):

        dir_list = os.walk(self.root_path)
        file_path = []

        for root, dirs, files in dir_list:
            for file in files:
                self.files.append(os.path.join(root, file))

    def pdf_to_text(self):

        self.all_pdf()

        for file in self.files:

            output = tempfile.NamedTemporaryFile()
            output_file = os.path.split(file)[0] + '/' + os.path.split(file)[1].replace('.pdf', '.txt')

            out, err = subprocess.Popen(['pdftotext', '-layout', file, output.name]).communicate()

            pdf = output.read()

            print(pdf)

            pdf = pdf.decode('windows-1252')

            with open(output_file, 'w') as f:
                f.write(pdf)


root_path = '/Users/maxwelllee54/GitHubs/Rapid_Assessment_Tools/SharedFiles/Fordham/RIA Liberia'

pdf = pdf_to_text(root_path).pdf_to_text()
