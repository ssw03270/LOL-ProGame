import csv

class CsvClass:
    #Get video url and input them in csv
    def input_csv(self, video_list):
        f = open("video_list.csv", "w", "utf-8", newline= "")
        wr = csv.writer(f)

        #url of playlist
        for video_info in video_list:
            wr.writerow(video_info.values())
        f.close
    
    def get_csv(self, file_name):
        f = open(file_name, "r")
        return list(csv.reader(f))