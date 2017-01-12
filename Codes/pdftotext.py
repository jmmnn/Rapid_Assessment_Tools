import tempfile, subprocess

def pdf_to_text(file_path):

    pdf = file_path.read()

    tf = tempfile.NamedTemporaryFile()
    tf.write(pdf)
    tf.seek(0)

    output = tempfile.NamedTemporaryFile()

    if(len(pdf) > 0):
        out, err = subprocess.Popen(['pdftotext', '-layout', tf.name, output.name]).communicate()
        return output.read()

    else:
        return None


pdf =  pdf_to_text(open('/Users/Maxwell/PycharmProjects/Github/Rapid_Assessment_Tools/SharedFiles/Fordham/RIA Cambodia/Docs Reviewed/Cambodia Industrial Development Policy 2015_2025.pdf', 'rb'))

pdf = pdf.decode('windows-1252')


with open('output.txt', 'w') as f:
    f.write(pdf)

