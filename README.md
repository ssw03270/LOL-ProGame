# LOL-ProGame
LOL-ProGame은 롤 공식 경기 하이라이트를 손쉽게 볼 수 있는 간단한 프로그램입니다.

![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/allgame.PNG)

## In Program

### Crawling
영상의 크롤링을 위해 유튜브 채널 중 하나인 [롤 스포츠 하이라이트](https://www.youtube.com/user/KazaLoLLCSHighlights/videos) 를 이용했습니다. 

셀레니움이 작동하는 모습 : 
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/selenium.PNG)

대회별로, 팀별로 영상을 분류했고 이를 통해 영상을 찾기 편하도록 만들었습니다.
추가적으로 크롤링의 속도를 위해 최근 2년까지의 기록만을 크롤링하도록 설정해뒀습니다. 

가공된 데이터는 csv 파일에 저장 :
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/csvfile.PNG)

만약 csv 파일이 없거나 크롤링을 하지 않았다면 아래와 같은 에러 메시지를 띄우게 됩니다.
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/error.PNG)


### Process
프로그램 내에서 영상의 검색과 다운로드가 가능합니다. 물론 검색하지 않고 모든 영상을 보는 것도 가능합니다.

검색하지 않고 모든 게임을 보여주는 모습 : 
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/allgame.PNG)

특정 검색어를 통해 검색하는 모습 :
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/search.PNG)

다운로드 된 영상들 :
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/download-video.PNG)

브라우저에서 실행되는 영상 :
![alt text](https://github.com/ssw03270/LOL-ProGame/blob/hotfix/src/forReadme/playing-video.PNG)

## Additionalally
README 파일 작성은 처음입니다. 
그리고 프로젝트 완료 이후 몇 달 만에 쓰게 된 탓에 그냥 대충대충 썼습니다. 
혹시 문제가 있거나, 개선 사항이 보인다면 알려주세요.
