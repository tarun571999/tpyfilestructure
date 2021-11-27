import os
import sys
def main():
    if len(sys.argv)<2:
        name_list = os.listdir()
        dict_category = {}
        dict_category['PDF file names'] = []
        dict_category['Text file names'] = []
        dict_category['Video file names'] = []
        dict_category['Image file names'] = []
        dict_category['Zip file names'] = []
        dict_category['Music file names'] = []
        dict_category['Python file names'] = []
        dict_category['Folder names'] = []
        python_files = []
        for i in name_list:
            if str.lower(i[-4:]) in ['.mp4','.webm','.mkv','.flv','.vob','.gif','.avi']:
                dict_category['Video file names'].append(i)
            elif str.lower(i[-4:]) in ['.pdf']:
                dict_category['PDF file names'].append(i)
            elif str.lower(i[-4:]) in ['.txt']:
                dict_category['Text file names'].append(i)
            elif str.lower(i[-4:]) in ['.zip']:
                dict_category['Zip file names'].append(i)
            elif str.lower(i[-4:]) in ['.jpg','.jpeg','.png','.svg','.avif']:
                dict_category['Image file names'].append(i)
            elif str.lower(i[-4:]) in ['.mp3']:
                dict_category['Music file names'].append(i)
            elif str.lower(i[-3:]) in ['.py']:
                dict_category['Python file names'].append(i)   
            else:
                dict_category['Folder names'].append(i)

        for t,k in dict_category.items():
            print('-----------------------------')
            print('-----------',t,'-------------')
            for names in k:
                print(names)
            print('-----------------------------')
    else:
        print("The function doesnot require any arguments/parameters, please only type 'tpyfilestructure' and hit enter")        
if __name__ == "__main__":
    main()