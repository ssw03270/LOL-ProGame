import csv


class CsvClass:
    # Get video url and input them in csv
    def input_csv(self, video_list):
        f = open("video_list.csv", "w", buffering=-1, encoding=None, newline="")
        wr = csv.writer(f)

        # url of playlist
        for video_info in video_list:
            try:
                wr.writerow(video_info.values())
            except:
                print("encoding-error")
        f.close()

    def get_csv(self, file_name):
        f = open(file_name, "r")
        return list(csv.reader(f))