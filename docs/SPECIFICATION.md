![IA_Diagram](./imgs_for_document/IA_Diagram.jpg)

크게 “다른 View로의 이동”을 지시하는 코드와 “View 안에서의 동작”을 만드는 코드를 작성하면 된다. 다른 View로 이동하는 코드는 View 기준 화살표가 나가는 방향(검정색 화살표)의 코드를 작성하면 된다. 

이를테면, Top View에서는 4종류의 “이동” 동작을 만들어야 한다.

 

 

**① Top View**

- “이동”
  - ‘수정’ 버튼을 누르면, Creation View로 이동한다. (내용이 채워진 상태로)
  - ‘추가’ 버튼을 누르면, Creation View로 이동한다. (내용이 비워진 상태로)
  - 하위 카드를 가지고 있는 ‘폴더’를 누르면, Folder View로 이동한다.
  - 하위 카드가 없는 ‘카드’를 누르면, Quiz View로 이동한다.

 

- “Display 할 요소들”
  - 하위 카드를 가지고 있는 ‘폴더’, 하위 카드를 가지고 있지 않은 ‘카드’ (form으로) (내가 생성한 폴더 혹은 카드, 다운로드를 받은 폴더 혹은 카드)
  - 폴더(카드) form 안에서 display할 요소들 
    - 기본적으로, title, description, 하위 quiz의 개수, 성취도
    - 다운로드 받은 것일 경우 : like 버튼과 개수, download 버튼과 개수 추가 
  - ‘추가’ 버튼 (form으로)
  - ‘검색’ 버튼 (form으로)
  - ‘삭제’ 버튼 (상단 우측 조그맣게)

 

- “동작”
  - ‘검색’ 버튼을 누르면, 타인이 생성한 ‘폴더’ 혹은 ‘카드’ 검색과 다운로드 가능
  - ‘삭제’ 버튼을 누르면, ‘폴더’ 혹은 ‘카드’ 삭제 

 

**② Creation View**

- "이동"
- ‘뒤로’ 버튼을 눌렀을 때, 이전 View로 이동

 

- “Display 할 요소들”
  - Title (form)
  - Description (form)
  - Q&A 생성 (form)
    - Q&A 생성 form 안에서 display할 요소 : Q, A
    - ‘삭제’ 버튼 (우측 상단)



- “동작”
  - 카드의 질문과 답을 생성한다.
  - 카드 입력을 완료하면, 그 다음 카드 form이 자동 생성된다.

 

**③ Folder View**

- “이동”
  - ‘뒤로’ 버튼을 눌렀을 때, 이전 View로 이동
  - ‘카드’를 눌렀을 때, Quiz View로 이동

 

- “Display 할 요소들”
  - 하위 카드를 가지고 있는 ‘폴더’, 하위 카드를 가지고 있지 않은 ‘카드’ (form으로) (내가 생성한 폴더 혹은 카드, 다운로드를 받은 폴더 혹은 카드)
  - 폴더(카드) form 안에서 display할 요소들 : title, description, 하위 quiz의 개수, 성취도
  - ‘생성’ 버튼 (form 으로)

 

**④ Quiz View**

- “이동”
  - ‘공부하기’ 버튼을 눌렀을 때, Study View로 이동

 

- “Display 할 요소들”
  - 카드의 ‘Q’ 와 정답 입력란

 

- "동작"
  - 맨 첫 화면에서 숫자가 줄어드는 (3->2->1) 애니메이션 제공
  - 사용자가 입력한 답안에 대해 채점을 진행
  - 퀴즈를 마치거나, 중간에 ‘뒤로’ 버튼을 누르면 ‘성취도’를 보여줌.

 

**⑤ Study View**

- “이동”
  - ‘뒤로’ 버튼을 눌렀을 때, 2단계 이전 View로 이동. (Top View 혹은 Folder View)

 

- “Display 할 요소들”
  - 카드의 ‘Q’ swipe시 ‘A’

 

- "동작"
  - 사용자가 나갈 때까지, 해당 카드의 무한루프로 문제->(스와이프)->정답->(스와이프)->문제->.. 을 보여줌