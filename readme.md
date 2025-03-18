# TFT Backseater
## 시즌 14 대응
현재까지 수집된 데이터는 시즌13데이터로, 곧 시즌 14가 출시되기 때문에 데이터 수집 코드를 리펙토링 하는 것에 집중   
>> 시즌 14가 시작하자마자 데이터를 크롤링 한다음에 동작할 수 있도록 하는 것이 목표 !
>> 메인 언어 영어 & 한국어 / 서비스 홍보 목적으로는 영어가 좋은데, 개발하면서 디버깅하기엔 한국어가 편하고.. 두 언어를 잘 연동할 방법을 모색해야함  
##  개요
인공지능이 당신의 플레이를 보고 롤토체스(전략적 팀 전투) 실시간으로 훈수둡니다.  

챗봇 버전으로 먼저 핵심 기능 개발 후 VLM으로 확장할 예정
### 크롤링
크롤링 대상: lolchess.gg / metatft.com 두개 사이트 크롤링  
크롤링 목적: 최신 패치노트 / 메타덱 / 빌드업 / 선호 아이템 / 선호 증강 수집

### 기능

#### 패치노트 요약
입력: 패치노트
결과: 사용자 질문에 따른 결과

#### 아이템 추천
입력: 챔피언, 현재 아이템 상황
결과: 완성 아이템 + (조합식)

#### 챔피언 추천
입력: 현재 기물 목록
결과: 조합에 맞는 챔피언

#### 기댓값
입력: 현재 레벨, 챔피언 이름
결과: 골드 기댓값 (기물수 고려 X)

#### 기댓값2
입력: 현재 레벨, 챔피언 이름, 기물현황
결과: 골드 기댓값
