import tempfile, subprocess, os

def pdf_to_text(file_object):

    pdf = file_object.read()

    tf = tempfile.NamedTemporaryFile()
    tf.write(pdf)
    tf.seek(0)

    output = tempfile.NamedTemporaryFile()

    if(len(pdf) > 0):
        out, err = subprocess.Popen(['pdftotext', '-layout', tf.name, output.name]).communicate()
        return output.read()

    else:
        return None


def all_pdf(root_dir):

    dir_list = os.walk(root_dir)
    file_path = []

    for root, dirs, files in dir_list:
        for file in files:
            file_path.append(os.path.join(root, file))

    return file_path





root = '/Users/Maxwell/PycharmProjects/Github/Rapid_Assessment_Tools/SharedFiles/Fordham/'


#pdf = pdf.decode('windows-1252')


#with open('output.txt', 'w') as f:
#    f.write(pdf)

