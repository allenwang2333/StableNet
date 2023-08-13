import os 
import shutil

def create_folder_if_not_exist(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def generate_files(split_file_path):
    index = 0
    for split_file in os.listdir(split_file_path):
        with open(split_file_path+'/'+split_file, 'r') as f:
            content = f.read()
            handle_file(content, index, split_file_path)
        index += 1

def handle_file(content, index, split_file_path):
    content = content.split('\n')
    if index % 3 == 0: # test set
        for i in content:
            file_name = i.split(' ')[0]
            if file_name != '':
                shutil.copy('PACS/' + file_name, 'DATASET/' + split_file_path + '/test' + file_name[file_name.find('/'):])
    if index % 3 == 1: # train
        for i in content:
            file_name = i.split(' ')[0]
            if file_name != '':
                shutil.copy('PACS/' + file_name, 'DATASET/' + split_file_path + '/train' + file_name[file_name.find('/'):])
    if index % 3 == 2: # val
        for i in content:
            file_name = i.split(' ')[0]
            if file_name != '':
                shutil.copy('PACS/' + file_name, 'DATASET/' + split_file_path + '/val' + file_name[file_name.find('/'):])
def main():
    folder_path = 'DATASET'
    # split_file_folder_path = 'split_compositional_dominant_sketch_target_photo'
    # split_file_folder_path = 'split_compositional_dominant_art_painting_target_sketch'
    # split_file_folder_path = 'split_compositional_dominant_cartoon_target_art_painting'
    split_file_folder_path = 'split_compositional_dominant_photo_target_cartoon'

    create_folder_if_not_exist(folder_path)

    split_path = folder_path + '/' + split_file_folder_path
    create_folder_if_not_exist(split_path)
    train_path = split_path + '/train'
    create_folder_if_not_exist(train_path)
    val_path = split_path + '/val'
    create_folder_if_not_exist(val_path)
    test_path = split_path + '/test'
    create_folder_if_not_exist(test_path)
    
    label_list = ['dog', 'elephant', 'giraffe', 'guitar', 'horse', 'house', 'person']
    for i in label_list:
        create_folder_if_not_exist(train_path + '/' + i)
        create_folder_if_not_exist(test_path + '/' + i)
        create_folder_if_not_exist(val_path + '/' + i)



    print("-----------------------------------------------")
    generate_files(split_file_folder_path)

if __name__ == '__main__':
    main()