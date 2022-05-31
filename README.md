# Auto_Labeling
## Scrapy에 Selenium 연동(image crawling)

**imgcrawler.py => naver crawler
**gcrawler.py => google craweler

**[구현한 부분]**
* Scrapy에 내장되어 있는 Spider와 Selenium과의 연동하여 지정한 URL(Naver image Search)을 open
* 사용자의 입력을 동적으로 받아들이는 부분(Keyboard input) 
* infite scroll down(page 끝까지 내려감)
* 큰이미지(_img)에 대해서 크롤링
* 디렉토리 생성 후 이미지 다운로드 

## GUI TOOL
**[구현한 부분]**
* 초기 화면 구성(크롤링, 자동라벨링 버튼 2개+추후 논의를 통해 변경 및 어떤 기능을 세분화하여 추가할지..) 
* 크롤링 버튼에 대해서 진행함
* Class 파일들을 한데 묶어 모듈화 하는 방법이 고민
* 우선적으로 네이버/구글/pexel/pixaby 4가지로 버튼을 세분화하여 버튼을 클릭 시, 크롤링이 이루어지는 방식으로 작동. 

* Amazon S3 데이터셋 공유 기능 탑재
* 주 동작 원리 Find 버튼과 Upload 버튼으로 구성
* Find() : 사용자가 로컬 컴퓨터에서 공유하고자 하는 데이터셋 폴더의 경로를 복사함
* Upload() : 사용자가 복사한 경로를 S3로 전송하여 다수의 사진들을 한번에 전송할 수 있음  



