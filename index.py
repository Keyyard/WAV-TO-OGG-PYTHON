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

#loop through all wav files in input folder
#for wav_file in glob.glob(os.path.join(input_folder, '*.wav')):
    #read wav file
#  data, samplerate = sf.read(wav_file)
    #get file name
#   file_name = os.path.splitext(os.path.basename(wav_file))[0]
    #write ogg file
#    sf.write(os.path.join(output_folder, file_name + '.ogg'), data, samplerate)

#loop through all wav files in input folders, there maybe even folders inside folders and create the same folder structures then output the oggs in correct places
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