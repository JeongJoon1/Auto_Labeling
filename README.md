# Auto_Labeling
## Scrapy에 Selenium 연동(naver image crawling)

**[구현한 부분]**
1. Scrapy에 내장되어 있는 Spider와 Selenium과의 연동하여 지정한 URL(Naver image Search)을 open
2. 사용자의 입력을 동적으로 받아들이는 부분(Keyboard input) 
3. infite scroll down(page 끝까지 내려감)
4. 큰이미지(_img)에 대해서 크롤링
5. 디렉토리 생성 후 이미지 다운로드 

**[해결해야 되는 부분]**  
* 이미지를 크롤링하고 파일을 생성하여 다운로드까지는 됐는데 일부 사진들이 깨지거나,파일은 있는데 이미지가 안보이는 이슈가 발생 
