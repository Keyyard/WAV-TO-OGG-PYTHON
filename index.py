import soundfile as sf
import os
import glob

#input folder
input_folder = 'input'
#output folder
output_folder = 'output'

#check if output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".wav"):
            #read wav file
            data, samplerate = sf.read(os.path.join(root, file))
            #get file name
            file_name = os.path.splitext(os.path.basename(file))[0]
            #create output folder structure
            output_folder_structure = os.path.join(output_folder, root)
            if not os.path.exists(output_folder_structure):
                os.makedirs(output_folder_structure)
            #write ogg file
            sf.write(os.path.join(output_folder_structure, file_name + '.ogg'), data, samplerate)
