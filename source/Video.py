import MainProcess

import os
from pytube import YouTube

class VideoClass:
    #Get video information with raw video
    def get_video_info(self, raw_video):
        video_list = []
        check_no_game = ["All", "Match", "Opening", "Draw"]
        for video in raw_video:
            original_title = video.find('a', {'title' : True})['title']
            check = False
            for checker in check_no_game:
                if checker in original_title:
                    check = True
                    continue
            if check:
                continue 

            video_original_title = original_title
            video_link = 'https://www.youtube.com' + video.find('a', {'href' : True})['href'] 
            video_img = 'https://img.youtube.com/vi/' + video_link[video_link.find('=') + 1:]  + '/mqdefault.jpg'
            video_world = self.get_world_video(self, original_title)
            video_teams = self.get_team_video(self, original_title, video_world)
            video_title = self.video_titling(self, original_title)
            video_additional = self.video_titling_additonal(self, original_title)
            video_info = {"original_title" : video_original_title, "title" : video_title, "additional_info" : video_additional, "link" : video_link, "img" : video_img, "teams" : video_teams, "world" : video_world}
            
            if video_additional == "error":
                continue
            video_list.append(video_info)
                
        return video_list

    #Titling video with original title
    def video_titling(self, original_title):
        pos = original_title.find("|")
        if pos == -1:
            pos = original_title.find("-")
        new_title = original_title[0:pos]
        return new_title

    #Titling video for additional
    def video_titling_additonal(self, original_title):
        pos = original_title.find("|")
        checker = ""
        if pos == -1:
            checker = "-"
        else:
            checker = "|"
        new_title = original_title.split(checker)
        try:
            return new_title[1]
        except:
            return "error"

    #Finding teams in each video
    def get_team_video(self, original_title, world):
        '''
        team_lck = ["GRF", "SB", "DYN", "SRB", "T1", "GEN", "DRX", "DWG", "KT", "APK", "HLE", "AF"]
        team_lcs = ["C9", "TL", "CLG", "DIG", "100", "GGS", "IMT", "FLY", "DIG", "EG", "TSM"]
        team_lec = ["G2", "MAD", "SK", "VIT", "RGE", "MSF", "XL", "S04", "FNC", "OG"]
        team_lpl = ["TES", "JDG", "FPX", "IG", "LNG", "LGD", "DMO", "VG", "JD", "ES", "OMG", "V5", "SN", "BLG", "RW", "WE"]
        team_list = {"LCK" : team_lck, "LCS" : team_lcs, "LEC" : team_lec, "LPL" : team_lpl}
        '''
        split_title = original_title.split(" ")
        
        team_01 = split_title[0]
        team_02 = split_title[2]

        team_in_video = []

        team_in_video.append(team_01)
        team_in_video.append(team_02)
        
        return team_in_video

    def get_world_video(self, original_title):
        world_list = ["LCK", "LCS", "LEC", "LPL"]
        world_in_video = ""
        for world in world_list:
            if world in original_title:
                world_in_video = world
                break

        return world_in_video
    
    #Downloading viedo.
    def download_video(self, video_link):
        try:
            stream = YouTube(video_link).streams.filter(file_extension='mp4', res='720p').first()
            stream.download(os.path.dirname(os.path.realpath(__file__)) + "/dir")
            return 0
        except:
            return -1