# ============================================================
# Playwright 실제 URL E2E 테스트
# 1단계: FastAPI 로그인 페이지 접속 및 화면 표시 확인
# ============================================================
#
# 이번 테스트의 목적:
#
# 지금까지 Playwright 기초 학습에서는 다음 코드를 사용.
#
# page.set_content("<h1>Login</h1>")
#
# page.set_content()
# → 테스트 코드 안에서 임시 HTML 화면을 직접 만들었습니다.
#
# 이번에는 임시 화면을 만드는 것이 아니라,
# 우리가 FastAPI로 실제 실행한 로그인 웹페이지에 접속합니다.
#
# 실제 접속 주소:
#
# http://127.0.0.1:8000/login
#
# 테스트 흐름:
#
# pytest 실행
# → Playwright가 Chromium 브라우저 준비
# → 실제 FastAPI /login 주소 접속
# → FastAPI가 로그인 HTML 반환
# → 브라우저에 Login 화면 표시
# → Playwright가 Login 제목 탐색
# → 화면에 보이는지 자동 검증
# → PASS 또는 FAIL 판정
# ============================================================


# playwright.sync_api에서 Page와 expect를 가져옵니다.
#
# playwright
# → Microsoft가 제공하는 Web UI 자동화 도구
#
# 터미널에서 설치했던 다음 패키지와 관련된 기능
#
# pip install pytest-playwright
#
# 그리고 Chromium 브라우저도 다음 명령으로 설치했습니다.
#
# python -m playwright install chromium
#
#
# sync_api
# → Playwright의 동기식 API를 의미
#
# 동기식은 작성한 코드가 위에서 아래로
# 한 줄씩 순서대로 실행되는 방식입니다.
#
# 예:
#
# 1. 페이지 접속
# 2. Login 제목 찾기
# 3. 화면 표시 여부 검증
#
# 현재 학습 단계에서는 실행 순서를 이해하기 쉬운
# sync_api 방식을 사용합니다.
#
#
# Page
# → Playwright 브라우저의 웹페이지 한 개를 표현하는 클래스입니다.
#
# 쉽게 말하면 Chromium 브라우저에서 열린
# 하나의 탭을 다루는 기능입니다.
#
# Page를 사용하면 다음 작업을 할 수 있습니다.
#
# 1. 실제 URL로 이동
# 2. 입력창 찾기
# 3. 글자 입력
# 4. 버튼 클릭
# 5. 화면의 글자 확인
# 6. URL 확인
# 7. 스크린샷 저장
#
#
# expect
# → 실제 결과가 기대 결과와 일치하는지
#   자동으로 확인하는 Playwright 검증 기능입니다.
#
# QA 관점으로 보면 다음과 같습니다.
#
# Expected Result
# → Login 제목이 화면에 보여야 한다.
#
# Actual Result
# → 현재 브라우저 화면에서 Login 제목을 찾는다.
#
# expect가 Expected와 Actual을 비교하여
# 테스트를 PASS 또는 FAIL로 판정하는 구조
#
#
# from A import B
# → A라는 위치에서 B라는 기능을 가져오겠다는
#   Python의 import 문법입니다.
#
# 따라서 아래 한 줄은 다음 의미입니다.
#
# Playwright의 동기식 API 모듈에서
# Page 클래스와 expect 검증 기능을 가져온다.
from playwright.sync_api import Page, expect

# ============================================================
# 테스트 함수 정의
# ============================================================
def test_login_page_is_displayed(page: Page) -> None:

    # def
    # → Python에서 함수를 만들 때 사용하는 문법입니다.
    #
    # 함수는 여러 줄의 코드를 하나의 작업으로 묶은 것입니다.
    #
    # 현재 함수가 담당하는 하나의 작업:
    #
    # FastAPI 로그인 페이지에 접속한 뒤
    # Login 제목이 화면에 표시되는지 검증한다.
    #
    #
    # test_login_page_is_displayed
    # → 이 테스트 함수의 이름입니다.
    #
    # 이름을 나누면 다음과 같습니다.
    #
    # test
    # → pytest가 실행할 테스트라는 뜻입니다.
    #
    # login_page
    # → 로그인 페이지가
    #
    # is_displayed
    # → 표시되는지 확인한다.
    #
    # 전체 의미:
    #
    # 로그인 페이지가 화면에 표시되는지 테스트한다.
    #
    #
    # pytest는 함수 이름이 test_로 시작하면
    # 테스트 함수라고 자동으로 판단합니다.
    #
    # 따라서 다음 이름은 테스트로 실행됩니다.
    #
    # test_login_page_is_displayed
    #
    # 반대로 다음처럼 test_로 시작하지 않으면
    # pytest가 일반 함수로 판단하여 자동 실행하지 않습니다.
    #
    # login_page_is_displayed
    #
    #
    # 함수 이름 마지막의 :
    # → 다음 줄부터 함수 내부 코드가 시작된다는 뜻입니다.
    #
    # Python은 중괄호가 아니라 들여쓰기를 사용하여
    # 함수 안에 포함된 코드를 구분합니다.


    # --------------------------------------------------------
    # page는 어디에서 오는가?
    # --------------------------------------------------------
    #
    # page는 우리가 직접 만든 변수가 아닙니다.
    #
    # 다음처럼 직접 작성하지 않았습니다.
    #
    # page = Page()
    #
    # pytest-playwright가 테스트를 실행할 때
    # 실제 Chromium 페이지 객체를 자동으로 만들어
    # 이 함수의 page 자리에 전달
    #
    # 이것을 pytest fixture 주입이라고 합니다.
    #
    # 이전에 배웠던 robot_device fixture와 원리가 비슷
    #
    # 기존 Mock Device 테스트:
    #
    # def test_motor_status(robot_device):
    #
    # pytest가 conftest.py에서 robot_device fixture를 찾아
    # 테스트 함수에 자동으로 전달했습니다.
    #
    # 이번 Playwright 테스트:
    #
    # def test_login_page_is_displayed(page: Page):
    #
    # pytest-playwright가 page fixture를 찾아
    # 브라우저 페이지 객체를 자동으로 전달합니다.
    #
    # 즉 실행 흐름은 다음과 같습니다.
    #
    # pytest가 테스트 함수 확인
    # → 함수 매개변수에 page가 있는지 확인
    # → pytest-playwright가 page fixture 준비
    # → Chromium 브라우저 실행
    # → 새 브라우저 페이지 생성
    # → 생성한 페이지를 page 변수에 전달
    # → 테스트 함수 실행


    # --------------------------------------------------------
    # page: Page의 의미
    # --------------------------------------------------------
    #
    # page
    # → 테스트 함수 내부에서 사용할 변수 이름입니다.
    #
    # :
    # → 변수의 타입 정보를 작성할 때 사용하는 기호입니다.
    #
    # Page
    # → 이 page 변수에는 Playwright의 Page 객체가
    #   들어온다는 타입 힌트입니다.
    #
    # 따라서 다음 코드는:
    #
    # page: Page
    #
    # 다음과 같이 읽을 수 있습니다.
    #
    # page라는 변수는 Playwright의 Page 타입이다.
    #
    # 주의:
    #
    # Page라고 작성했다고 브라우저가 생성되는 것은 아닙니다.
    #
    # 실제 브라우저와 페이지를 만들어 전달하는 것은
    # pytest-playwright의 page fixture입니다.
    #
    # Page는 개발자와 VS Code에
    # page가 어떤 종류의 객체인지 알려주는 역할입니다.
    #
    # 타입 힌트가 있기 때문에 VS Code에서
    # page.을 입력했을 때 다음 기능들에 대해 자동 완성 기능을 제공
    #
    # page.goto()
    # page.get_by_role()
    # page.get_by_label()
    # page.screenshot()


    # --------------------------------------------------------
    # -> None의 의미
    # --------------------------------------------------------
    #
    # -> None
    # → 이 함수가 별도의 결과값을 return하지 않는다는
    #   Python 타입 힌트입니다.
    #
    # 일반 함수는 다음처럼 결과를 반환할 수 있습니다.
    #
    # def add_number() -> int:
    #     return 10
    #
    # 하지만 pytest 테스트 함수는 일반적으로
    # 값을 return해서 PASS/FAIL을 판단하지 않습니다.
    #
    # 대신 expect 또는 assert를 사용해 검증합니다.
    #
    # 검증 성공:
    # → 테스트 PASS
    #
    # 검증 실패:
    # → 테스트 FAIL
    #
    # 따라서 현재 테스트 함수는 return 값이 없으므로
    # -> None을 작성합니다.


    # ========================================================
    # 1. 실제 FastAPI 로그인 페이지로 이동
    # ========================================================

    # page.goto()
    # → 현재 Playwright 브라우저 페이지를
    #   지정한 웹 주소로 이동시키는 기능입니다.
    #
    # goto는 "그곳으로 이동한다"는 의미입니다.
    #
    # page
    # → pytest-playwright가 전달한 Chromium 페이지입니다.
    #
    # .
    # → page 객체가 가지고 있는 기능을 사용한다는 뜻입니다.
    #
    # goto
    # → URL로 이동하는 Playwright Page 기능입니다.
    #
    # ()
    # → goto 기능에 필요한 값을 전달하는 괄호입니다.
    #
    # 괄호 안의 문자열:
    #
    # "http://127.0.0.1:8000/login"
    #
    # → Playwright 브라우저가 접속할 실제 주소입니다.
    #
    #
    # 주소를 나누면:
    #
    # http
    # → 웹 통신 방식입니다.
    #
    # 127.0.0.1
    # → 현재 자신의 컴퓨터를 의미하는 로컬 주소입니다.
    #
    # 8000
    # → Uvicorn FastAPI 서버가 사용하는 포트 번호입니다.
    #
    # /login
    # → FastAPI에 등록한 로그인 페이지 경로입니다.
    #
    #
    # 이 주소에 접속하면 FastAPI의 다음 코드와 연결됩니다.
    #
    # @app.get("/login", response_class=HTMLResponse)
    # def show_login_page() -> str:
    #
    # 실제 요청 흐름:
    #
    # Playwright 브라우저
    # → GET /login 요청 전송
    # → FastAPI가 @app.get("/login") 경로 탐색
    # → show_login_page() 함수 실행
    # → 로그인 HTML 문자열 반환
    # → HTMLResponse로 브라우저에 전달
    # → Login 화면 표시
    #
    #
    # 기존 page.set_content()와 차이:
    #
    # page.set_content()
    # → 테스트 코드에서 임시 HTML을 직접 생성합니다.
    # → FastAPI 서버를 거치지 않습니다.
    #
    # page.goto()
    # → 실제 실행 중인 FastAPI 주소에 접속합니다.
    # → 브라우저와 서버가 실제로 통신합니다.
    #
    # 따라서 page.goto()를 사용하는 이번 테스트가
    # 실제 URL 기반 E2E 테스트의 시작입니다.
    page.goto("http://127.0.0.1:8000/login")

    # ========================================================
    # 2. 화면에서 Login 제목 찾기
    # ========================================================

    # page.get_by_role()
    # → 화면 요소의 의미와 역할을 기준으로
    #   HTML 요소를 찾는 Playwright Locator 기능입니다.
    #
    # Locator
    # → 브라우저 화면에서 특정 요소를 가리키는 대상입니다.
    #
    # 쉽게 말하면:
    #
    # Playwright가 클릭하거나 확인할 화면 요소를
    # 찾아서 가리키는 표지판입니다.
    #
    #
    # 현재 FastAPI 로그인 HTML에는 다음 코드가 있습니다.
    #
    # <h1>Login</h1>
    #
    # h1
    # → HTML에서 가장 중요한 제목입니다.
    #
    # 브라우저와 Playwright는 h1 요소를
    # heading 역할로 이해합니다.
    #
    #
    # get_by_role("heading", name="Login")
    #
    # "heading"
    # → 제목 역할을 가진 요소를 찾습니다.
    #
    # name="Login"
    # → 그중 화면에 Login이라고 표시된 요소를 찾습니다.
    #
    # 따라서 전체 의미는:
    #
    # 화면에서 Login이라는 이름을 가진 제목 요소를 찾는다.
    #
    #
    # 왜 h1 태그를 직접 찾지 않는가?
    #
    # 다음처럼 CSS 방식으로 찾을 수도 있습니다.
    #
    # page.locator("h1")
    #
    # 하지만 화면에 h1이 여러 개 있거나
    # HTML 구조가 변경되면 어떤 제목인지 알기 어려울 수 있습니다.
    #
    # get_by_role()은 사용자가 화면에서 인식하는
    # 요소의 의미와 이름을 기준으로 찾습니다.
    #
    # QA 자동화에서는 다음과 같은 장점이 있습니다.
    #
    # 1. 테스트 코드의 의도가 명확합니다.
    # 2. 실제 사용자가 인식하는 방식과 비슷합니다.
    # 3. HTML 구조가 조금 바뀌어도 유지될 가능성이 높습니다.
    #
    #
    # 찾은 Locator를 login_heading 변수에 저장합니다.
    #
    # login_heading
    # → Login 제목을 가리키는 Locator 변수 이름입니다.
    #
    # =
    # → 오른쪽에서 찾은 Locator를
    #   왼쪽 변수에 저장합니다.
    #
    # 아직 이 줄에서는 PASS/FAIL을 판정하지 않습니다.
    #
    # 화면에서 Login 제목을 찾아
    # 나중에 검증할 수 있도록 변수에 저장하는 단계입니다.
    login_heading = page.get_by_role("heading", name="Login")

    # ========================================================
    # 3. Login 제목이 실제로 보이는지 검증
    # ========================================================

    # expect()
    # → 실제 결과를 기대 결과와 비교하는
    #   Playwright의 검증 기능입니다.
    #
    # 위에서 import한 다음 expect를 사용합니다.
    #
    # from playwright.sync_api import Page, expect
    #
    #
    # expect(login_heading)
    # → 위에서 찾은 Login 제목 Locator를
    #   검증 대상으로 지정합니다.
    #
    #
    # .to_be_visible()
    # → 그 요소가 브라우저 화면에 실제로 보이는지 확인합니다.
    #
    # visible은 영어로 "보이는"이라는 뜻입니다.
    #
    # 따라서 다음 코드는:
    #
    # expect(login_heading).to_be_visible()
    #
    # 다음처럼 읽을 수 있습니다.
    #
    # Login 제목이 화면에 보일 것이라고 기대하고 검증한다.
    #
    #
    # 검증 결과:
    #
    # Login 제목을 찾았고 화면에 보임
    # → Expected Result와 Actual Result가 일치
    # → 테스트 PASS
    #
    # Login 제목이 없음
    # → 테스트 FAIL
    #
    # Login 제목은 있지만 숨겨져 있음
    # → 테스트 FAIL
    #
    # FastAPI 서버에 접속하지 못함
    # → page.goto() 단계에서 테스트 FAIL
    #
    #
    # expect는 바로 실패시키기 전에
    # 짧은 시간 동안 요소가 나타나는지 기다립니다.
    #
    # 웹페이지는 로딩 시간이 필요할 수 있기 때문입니다.
    #
    # 요소가 제한 시간 안에 나타나면 PASS,
    # 나타나지 않으면 오류 메시지와 함께 FAIL이 됩니다.
    expect(login_heading).to_be_visible()

    # 전체 실행 흐름
    #
    # 1. pytest가 test_login_e2e.py를 찾는다.
    #
    # 2. 이름이 test_로 시작하는 함수를 찾는다.
    # 
    # 3. 함수 매개변수에서 page를 발견한다.
    # 
    # 4. pytest-playwright가 Chromium을 실행한다.
    # 
    # 5. 새 브라우저 페이지를 만들어 page 변수로 전달한다.
    # 
    # 6. page.goto()가 실제 FastAPI /login 주소에 접속한다.
    # 
    # 7. FastAPI의 show_login_page()가 로그인 HTML을 반환한다.
    # 
    # 8. page.get_by_role()이 Login 제목을 찾는다.
    # 
    # 9. expect().to_be_visible()이 화면 표시 여부를 검증한다.
    # 
    # 10. 조건이 맞으면 pytest가 PASS로 판정한다.


# ============================================================
# Playwright 실제 URL E2E 테스트
# 2단계: 정상 계정 로그인 성공 확인
# ============================================================

def test_valid_login_success(page: Page) -> None:
    # --------------------------------------------------------
    # 이 테스트 함수의 목적
    # --------------------------------------------------------
    #
    # 사용자가 실제로 로그인하는 전체 과정을
    # Playwright가 자동으로 수행합니다.
    #
    # 자동 수행 순서:
    #
    # 1. FastAPI 로그인 페이지 접속
    # 2. Email 입력창 찾기
    # 3. 정상 Email 입력
    # 4. Password 입력창 찾기
    # 5. 정상 Password 입력
    # 6. Login 버튼 찾기
    # 7. Login 버튼 클릭
    # 8. Dashboard 제목 확인
    # 9. Welcome 메시지 확인
    #
    # 페이지 접속부터 로그인 결과 확인까지
    # 하나의 사용자 흐름을 처음부터 끝까지 검증하므로
    # E2E, 즉 End-to-End 테스트라고 합니다.


    # --------------------------------------------------------
    # page는 어디에서 오는가?
    # --------------------------------------------------------
    #
    # page는 우리가 직접 만든 변수가 아닙니다.
    #
    # pytest-playwright가 Chromium 브라우저를 실행하고,
    # 새 브라우저 페이지를 생성한 뒤
    # 이 함수의 page 매개변수로 자동 전달합니다.
    #
    # 이전 테스트의 page와 이번 테스트의 page는
    # 각각 새롭게 준비되므로 서로의 화면 상태가 섞이지 않습니다.
    #
    # Page는 다음 import 문에서 가져온
    # Playwright의 페이지 타입입니다.
    #
    # from playwright.sync_api import Page, expect



    # ========================================================
    # 우리가 만든 이름과 Playwright 제공 기능 구분
    # ========================================================
    #
    # 아래 테스트 코드에는 두 종류의 이름이 함께 나옵니다.
    #
    # 1. 우리가 직접 정한 변수 이름과 테스트 데이터
    # 2. Playwright에서 미리 제공하는 기능 이름
    #
    #
    # 우리가 직접 정한 변수 이름:
    #
    # email_input
    # password_input
    # login_button
    # dashboard_heading
    # welcome_message
    #
    # 위 이름들은 Playwright가 반드시 사용하라고 정한 이름이 아닙니다.
    # 코드 작성자가 내용을 쉽게 알아보기 위해 직접 붙인 이름입니다.
    #
    # 예를 들어 email_input은 아래처럼 바꿔도 됩니다.
    #
    # email_box = page.get_by_label("Email")
    # email_box.fill("qa@example.com")
    #
    # 단, 변수 이름을 변경했다면 이후 사용하는 코드에서도
    # 같은 이름으로 일관되게 작성해야 합니다.
    #
    #
    # Playwright에서 제공하는 기능 이름:
    #
    # page.goto()
    # page.get_by_label()
    # page.get_by_role()
    # page.get_by_text()
    # fill()
    # click()
    # expect()
    # to_have_value()
    # to_be_visible()
    # wait_for_timeout()
    #
    # 위 기능 이름들은 Playwright 라이브러리에
    # 이미 정해져 있는 이름이므로 임의로 바꾸면 안 됩니다.
    #
    # 예를 들어 fill()을 write_text()처럼 임의로 바꾸면
    # Playwright에 그런 기능이 없기 때문에 오류가 발생합니다.
    #
    #
    # 우리가 직접 정한 테스트 데이터와 기대값:
    #
    # "qa@example.com"
    # "Password123!"
    # "Dashboard"
    # "Welcome, QA User"
    #
    # 위 문자열은 테스트 목적에 맞게 우리가 직접 작성한 값입니다.
    #
    #
    # 핵심 정리:
    #
    # email_input
    # → 우리가 만든 변수 이름
    #
    # fill()
    # → Playwright가 제공하는 입력 기능
    #
    # "qa@example.com"
    # → 우리가 정한 테스트 입력값
    #
    # expect()
    # → Playwright에서 가져온 검증 기능
    #
    # to_have_value()
    # → 입력창의 실제 value를 비교하는
    #   Playwright의 Locator 검증 기능
    #

    # ========================================================
    # 1. 실제 FastAPI 로그인 페이지 접속
    # ========================================================

    # page.goto()
    # → Playwright 브라우저를 지정한 URL로 이동시킵니다.
    #
    # page
    # → pytest-playwright가 만들어준 브라우저 페이지입니다.
    #
    # .
    # → page 객체가 가지고 있는 기능을 사용한다는 뜻입니다.
    #
    # goto()
    # → 지정한 웹 주소로 이동하는 Playwright 기능입니다.
    #
    # 접속 흐름:
    #
    # Playwright
    # → GET /login 요청
    # → FastAPI의 @app.get("/login") 실행
    # → show_login_page() 실행
    # → 로그인 HTML 반환
    # → 브라우저에 Login 화면 표시
    page.goto("http://127.0.0.1:8000/login")

    # ========================================================
    # 2. Email 입력창 찾기
    # ========================================================

    # page.get_by_label()
    # → 화면에 표시된 Label 이름을 기준으로
    #   연결된 입력창을 찾는 Playwright 기능입니다.
    #
    # 현재 FastAPI 로그인 HTML에는 다음 연결이 있습니다.
    #
    # <label for="email">Email</label>
    # <input id="email" name="email" ...>
    #
    # label의 for="email"과
    # input의 id="email"이 서로 같기 때문에
    # Playwright는 Email Label과 입력창의 관계를 이해합니다.
    #
    # get_by_label("Email")
    # → Email이라는 Label에 연결된 입력창을 찾습니다.
    #
    # 찾은 입력창은 email_input 변수에 저장합니다.
    #
    # 이 줄에서는 아직 Email을 입력하지 않습니다.
    # 입력할 대상을 먼저 찾아 저장하는 단계입니다.
    email_input = page.get_by_label("Email")


    # ========================================================
    # 3. Password 입력창 찾기
    # ========================================================

    # Password 입력창도 Email과 같은 원리로 찾습니다.
    #
    # FastAPI HTML:
    #
    # <label for="password">Password</label>
    # <input id="password" name="password" type="password">
    #
    # label의 for="password"와
    # input의 id="password"가 연결되어 있습니다.
    #
    # get_by_label("Password")
    # → Password Label에 연결된 입력창을 찾습니다.
    #
    # 찾은 입력창을 password_input 변수에 저장합니다.
    password_input = page.get_by_label("Password")


    # ========================================================
    # 4. Login 버튼 찾기
    # ========================================================

    # page.get_by_role()
    # → HTML 요소의 의미와 화면에 표시된 이름을 기준으로
    #   요소를 찾는 Playwright Locator 기능입니다.
    #
    # 현재 FastAPI HTML:
    #
    # <button type="submit">Login</button>
    #
    # button
    # → 브라우저와 Playwright가 button 역할로 이해합니다.
    #
    # name="Login"
    # → 버튼 안에 표시된 Login 글자를 기준으로 찾습니다.
    #
    # 따라서 전체 의미는:
    #
    # 화면에서 Login이라는 이름의 버튼을 찾는다.
    #
    # 찾은 버튼을 login_button 변수에 저장합니다.
    login_button = page.get_by_role("button", name="Login")


    # ========================================================
    # 5. 정상 Email 자동 입력
    # ========================================================

    # fill()
    # → Playwright가 입력창에 글자를 입력하는 기능입니다.
    #
    # email_input
    # → 앞에서 찾은 Email 입력창 Locator입니다.
    #
    # .fill("qa@example.com")
    # → Email 입력창을 비운 뒤
    #   qa@example.com이라는 문자열을 입력합니다.
    #
    # 사람이 키보드로 입력하는 작업을
    # Playwright가 자동으로 수행하는 것입니다.
    #
    # qa@example.com은 web_demo.py에 미리 정한
    # 정상 Email과 같은 값입니다.
    #
    # VALID_EMAIL = "qa@example.com"

    # --------------------------------------------------------
    # email_input.fill()의 출처를 정확히 구분
    # --------------------------------------------------------
    #
    # email_input
    # → 직접 만든 변수 이름입니다.
    #
    # 이 변수에는 아래 Playwright 코드가 찾은
    # Email 입력창 Locator가 저장되어 있습니다.
    #
    # email_input = page.get_by_label("Email")
    #
    #
    # fill()
    # → 직접 만든 함수가 아닙니다.
    #
    # Playwright의 Locator 객체가 기본으로 제공하는
    # 입력 기능입니다.
    #
    # get_by_label()로 입력창을 찾으면 그 결과는
    # Locator 객체가 되며, Locator에는 fill() 기능이 있습니다.
    #
    #
    # "qa@example.com"
    # → Playwright가 정한 값이 아닙니다.
    #
    # 정상 로그인 테스트를 위해 직접 선택한
    # 테스트 입력 데이터입니다.
    #
    #
    # 따라서 아래 코드는 다음처럼 읽습니다.
    #
    # 우리가 email_input이라고 이름 붙인 Email 입력창에
    # Playwright의 fill() 기능을 사용하여
    # 우리가 정한 qa@example.com 값을 입력한다.
    #
    email_input.fill("qa@example.com")


    # ========================================================
    # 6. 정상 Password 자동 입력
    # ========================================================

    # password_input
    # → 앞에서 찾은 Password 입력창 Locator입니다.
    #
    # fill("Password123!")
    # → 정상 Password를 자동으로 입력합니다.
    #
    # Password 입력창은 HTML에서 type="password"이므로
    # 브라우저 화면에는 실제 글자가 아니라
    # 점 또는 동그라미 형태로 가려져 표시됩니다.
    #
    # 하지만 Playwright는 실제 문자열
    # Password123!을 입력하고 있습니다.
    #
    # Password123!은 web_demo.py에 미리 정한
    # 정상 Password와 같은 값입니다.
    #
    # VALID_PASSWORD = "Password123!"

    # --------------------------------------------------------
    # password_input.fill()의 출처를 정확히 구분
    # --------------------------------------------------------
    #
    # password_input
    # → 직접 만든 변수 이름입니다.
    #
    # 이 변수에는 Password 입력창 Locator가 저장되어 있습니다.
    #
    #
    # fill()
    # → Playwright의 Locator가 제공하는 입력 기능입니다.
    #
    # 우리가 직접 정의한 함수가 아니므로
    # 이름을 임의로 변경하면 안 됩니다.
    #
    #
    # "Password123!"
    # → 우리가 정상 로그인 테스트를 위해 직접 정한
    #   Password 테스트 데이터입니다.
    #
    #
    # 따라서 아래 코드는 다음처럼 읽습니다.
    #
    # 우리가 password_input이라고 이름 붙인 Password 입력창에
    # Playwright의 fill() 기능을 사용하여
    # 우리가 정한 Password123! 값을 입력한다.
    #
    password_input.fill("Password123!")


    # ========================================================
    # 7. 입력값이 정상적으로 들어갔는지 확인
    # ========================================================

    # expect(email_input)
    # → Email 입력창을 검증 대상으로 지정합니다.
    #
    # to_have_value("qa@example.com")
    # → 입력창의 실제 value 값이
    #   qa@example.com과 같은지 확인합니다.
    #
    # 실제 입력값과 기대 입력값이 같으면 PASS하고,
    # 다르면 이 지점에서 테스트가 FAIL합니다.

    # --------------------------------------------------------
    # expect(...).to_have_value()의 출처를 정확히 구분
    # --------------------------------------------------------
    #
    # expect
    # → 아래 import 문에서 가져온 Playwright 검증 기능입니다.
    #
    # from playwright.sync_api import Page, expect
    #
    #
    # email_input
    # → 직접 만든 변수 이름이며,
    #   Email 입력창 Locator가 저장되어 있습니다.
    #
    #
    # expect(email_input)
    # → Email 입력창 Locator를 검증 대상으로 지정합니다.
    #
    #
    # to_have_value()
    # → 직접 만든 함수가 아닙니다.
    #
    # Playwright가 입력창과 같은 Locator의 실제 value를
    # 기대값과 비교하기 위해 제공하는 검증 기능입니다.
    #
    # 정확히는 expect()에 Locator를 전달했을 때 사용할 수 있는
    # Playwright Locator 검증 메서드입니다.
    #
    #
    # "qa@example.com"
    # → 우리가 직접 정한 기대값입니다.
    #
    #
    # 따라서 아래 코드는 다음처럼 읽습니다.
    #
    # Email 입력창의 실제 value가
    # 우리가 기대한 qa@example.com과 같은지
    # Playwright가 자동으로 검증한다.
    #
    expect(email_input).to_have_value("qa@example.com")


    # Password 입력창에도 정상 Password가 들어갔는지
    # 같은 방법으로 확인합니다.
    #
    # 브라우저 화면에서는 비밀번호가 점으로 가려져 있어도
    # 입력창 내부의 실제 value는 Password123!입니다.

    # --------------------------------------------------------
    # Password to_have_value() 검증의 출처
    # --------------------------------------------------------
    #
    # expect()
    # → Playwright가 제공하는 검증 기능
    #
    # password_input
    # → 우리가 만든 Password 입력창 변수
    #
    # to_have_value()
    # → Playwright가 제공하는 실제 value 비교 기능
    #
    # "Password123!"
    # → 우리가 직접 정한 기대값
    #
    #
    # Password 입력창은 화면에서 점으로 가려져 보여도
    # 입력창 내부에는 실제 value가 저장되어 있습니다.
    #
    # Playwright는 화면에 보이는 점의 개수를 확인하는 것이 아니라
    # 입력창 내부의 실제 value를 기대값과 비교합니다.
    #
    expect(password_input).to_have_value("Password123!")


    # ========================================================
    # 8. Login 버튼 자동 클릭
    # ========================================================

    # click()
    # → Playwright가 해당 화면 요소를 클릭하는 기능입니다.
    #
    # login_button
    # → 앞에서 찾은 Login 버튼 Locator입니다.
    #
    # Login 버튼의 type은 submit입니다.
    #
    # 따라서 버튼을 클릭하면 Form 안에 있는 다음 값이
    # FastAPI 서버로 전송됩니다.
    #
    # email=qa@example.com
    # password=Password123!
    #
    # HTML Form 설정:
    #
    # action="/login"
    # method="post"
    #
    # 실제 요청:
    #
    # POST /login
    #
    # FastAPI에서는 다음 함수가 실행됩니다.
    #
    # @app.post("/login")
    # def process_login(...)
    login_button.click()


    # ========================================================
    # 9. 로그인 성공 화면에서 Dashboard 제목 찾기
    # ========================================================

    # Login 버튼을 클릭하면 FastAPI의 if 조건이 실행됩니다.
    #
    # if email == VALID_EMAIL and password == VALID_PASSWORD:
    #
    # 현재 입력한 Email과 Password가 모두 정상 값이므로
    # 조건 결과는 True가 됩니다.
    #
    # FastAPI가 다음 HTML을 반환합니다.
    #
    # <h1>Dashboard</h1>
    # <p>Welcome, QA User</p>
    #
    # get_by_role("heading", name="Dashboard")
    # → Dashboard라는 이름을 가진 제목 요소를 찾습니다.
    #
    # 찾은 제목을 dashboard_heading 변수에 저장합니다.
    dashboard_heading = page.get_by_role(
        "heading",
        name="Dashboard",
    )


    # ========================================================
    # 10. 로그인 성공 안내 문구 찾기
    # ========================================================

    # page.get_by_text()
    # → 브라우저 화면에 표시된 실제 글자를 기준으로
    #   요소를 찾는 Playwright Locator 기능입니다.
    #
    # "Welcome, QA User"
    # → 정상 로그인 성공 화면에 표시되는 안내 문구입니다.
    #
    # 찾은 요소를 welcome_message 변수에 저장합니다.
    welcome_message = page.get_by_text("Welcome, QA User")


    # ========================================================
    # 11. Dashboard 제목이 보이는지 검증
    # ========================================================

    # expect(dashboard_heading)
    # → Dashboard 제목을 검증 대상으로 지정합니다.
    #
    # to_be_visible()
    # → 해당 제목이 브라우저 화면에 실제로 보이는지 확인합니다.
    #
    # Dashboard가 보이면:
    # → 정상 로그인 성공
    # → 이 검증 PASS
    #
    # Dashboard가 보이지 않으면:
    # → 정상 로그인 결과가 기대와 다름
    # → 테스트 FAIL
    expect(dashboard_heading).to_be_visible()


    # ========================================================
    # 12. Welcome 메시지가 보이는지 검증
    # ========================================================

    # 정상 로그인에서는 Dashboard 제목만 확인하는 것이 아니라
    # 사용자 환영 문구도 함께 확인합니다.
    #
    # Expected Result:
    #
    # Welcome, QA User가 화면에 보여야 한다.
    #
    # Actual Result:
    #
    # Playwright가 현재 브라우저 화면에서
    # Welcome, QA User를 찾는다.
    #
    # 기대 결과와 실제 결과가 같으면 PASS합니다.
    # to_have_value()
    # → 입력창의 실제 value를 비교하는
    #   Playwright의 Locator 검증 기능
    expect(welcome_message).to_be_visible()


    # ========================================================
    # 13. 스크린샷 확보를 위한 임시 화면 대기
    # ========================================================

    # page.wait_for_timeout()
    # → 지정한 시간만큼 브라우저 화면을 유지합니다.
    # → Playwright Page가 제공하는 임시 대기 기능입니다.
    #
    # 괄호 안의 숫자는 밀리초 단위입니다.
    #
    # 1000밀리초 = 1초
    # 3000밀리초 = 3초
    #
    # 이번에는 Dashboard 결과 화면을 직접 확인하고
    # 포트폴리오용 스크린샷을 확보하기 위해
    # 테스트 종료 전에 3초 동안 화면을 유지합니다.
    #
    # 주의:
    #
    # 이 코드는 테스트 결과를 검증하는 코드가 아닙니다.
    # 교육과 스크린샷 확보를 위한 임시 대기 코드입니다.
    #
    # 나중에 GitHub Actions CI에 연결할 때는
    # 불필요한 실행 시간을 줄이기 위해 제거할 수 있습니다.
    page.wait_for_timeout(10000)



# ============================================================
# Playwright 실제 URL E2E 테스트
# 3단계: 잘못된 Password 로그인 실패 확인
# ============================================================


def test_invalid_login_failure(page: Page) -> None:
    # --------------------------------------------------------
    # 이 테스트 함수의 목적
    # --------------------------------------------------------
    #
    # 이번 테스트에서는 정상 Email과 잘못된 Password를 사용하여
    # 로그인에 실패하는 흐름을 Playwright로 자동 검증합니다.
    #
    # 자동 수행 순서:
    #
    # 1. 실제 FastAPI 로그인 페이지 접속
    # 2. Email 입력창 찾기
    # 3. Password 입력창 찾기
    # 4. Login 버튼 찾기
    # 5. 정상 Email 입력
    # 6. 잘못된 Password 입력
    # 7. 입력값 검증
    # 8. Login 버튼 클릭
    # 9. Login Failed 제목 확인
    # 10. Invalid email or password 문구 확인
    # 11. Back to Login 링크 확인
    #
    #
    # 정상 로그인 테스트와의 차이:
    #
    # 정상 로그인:
    #
    # Email 정상
    # Password 정상
    # → FastAPI if 조건 True
    # → Dashboard 화면
    #
    # 비정상 로그인:
    #
    # Email 정상
    # Password 비정상
    # → FastAPI if 조건 False
    # → else 실행
    # → Login Failed 화면


    # --------------------------------------------------------
    # 함수 선언 설명
    # --------------------------------------------------------
    #
    # def
    # → Python에서 함수를 정의하는 기본 문법입니다.
    #
    #
    # test_invalid_login_failure
    # → 직접 정한 테스트 함수 이름입니다.
    #
    # 이름을 나누면:
    #
    # test
    # → pytest가 실행할 테스트
    #
    # invalid_login
    # → 비정상 로그인
    #
    # failure
    # → 실패 결과
    #
    # 전체 의미:
    #
    # 비정상 로그인의 실패 결과를 테스트한다.
    #
    #
    # 함수 이름이 test_로 시작하기 때문에
    # pytest가 테스트 함수로 자동 수집합니다.
    #
    #
    # page
    # → pytest-playwright가 자동으로 만들어 전달하는
    #   브라우저 페이지 객체입니다.
    #
    #
    # Page
    # → playwright.sync_api에서 import한
    #   Playwright Page 타입입니다.
    #
    #
    # -> None
    # → 이 테스트 함수는 별도의 값을 return하지 않는다는
    #   Python 타입 힌트입니다.
    #
    # 테스트 결과는 return 값이 아니라
    # expect() 검증 결과로 PASS 또는 FAIL을 판단합니다.



    # ========================================================
    # 1. 실제 FastAPI 로그인 페이지 접속
    # ========================================================

    # page.goto()
    # → Playwright의 Page 객체가 제공하는 URL 이동 기능입니다.
    #
    # page
    # → pytest-playwright가 전달한 브라우저 페이지 객체
    #
    # goto()
    # → Playwright Page가 제공하는 기능
    #
    # "http://127.0.0.1:8000/login"
    # → 우리가 직접 정한 테스트 대상 URL
    #
    #
    # 실제 요청 흐름:
    #
    # Playwright 브라우저
    # → GET /login
    # → FastAPI @app.get("/login") 실행
    # → 로그인 HTML 반환
    # → 브라우저에 Login 화면 표시
    page.goto("http://127.0.0.1:8000/login")


    # ========================================================
    # 2. Email 입력창 찾기
    # ========================================================

    # page.get_by_label()
    # → Playwright Page가 제공하는 Locator 탐색 기능입니다.
    #
    # 화면의 Label 이름을 기준으로
    # 연결된 입력창을 찾습니다.
    #
    #
    # FastAPI HTML:
    #
    # <label for="email">Email</label>
    # <input id="email" name="email" type="email">
    #
    # label의 for="email"과
    # input의 id="email"이 연결되어 있습니다.
    #
    #
    # page.get_by_label("Email")
    # → Email Label과 연결된 입력창 Locator를 찾습니다.
    #
    #
    # email_input
    # → 직접 만든 변수 이름입니다.
    #
    # 이 변수 안에는 Email 입력창 Locator가 저장됩니다.
    #
    #
    # 구분:
    #
    # email_input
    # → 우리가 만든 변수 이름
    #
    # get_by_label()
    # → Playwright Page가 제공하는 기능
    #
    # "Email"
    # → 우리가 정한 탐색 조건
    email_input = page.get_by_label("Email")


    # ========================================================
    # 3. Password 입력창 찾기
    # ========================================================

    # page.get_by_label("Password")
    # → Password Label과 연결된 입력창을 찾습니다.
    #
    #
    # password_input
    # → 직접 만든 변수 이름입니다.
    #
    # 이 변수에는 Password 입력창 Locator가 저장됩니다.
    #
    #
    # 구분:
    #
    # password_input
    # → 우리가 만든 변수
    #
    # get_by_label()
    # → Playwright Page 제공 기능
    #
    # "Password"
    # → 우리가 정한 탐색 조건
    password_input = page.get_by_label("Password")


    # ========================================================
    # 4. Login 버튼 찾기
    # ========================================================

    # page.get_by_role()
    # → HTML 요소의 역할과 화면 이름을 기준으로
    #   요소를 찾는 Playwright Page 기능입니다.
    #
    #
    # FastAPI HTML:
    #
    # <button type="submit">Login</button>
    #
    #
    # "button"
    # → 버튼 역할의 요소를 찾습니다.
    #
    # name="Login"
    # → 화면에 Login이라고 표시된 버튼을 찾습니다.
    #
    #
    # login_button
    # → 우리가 직접 만든 변수 이름입니다.
    #
    # 이 변수에는 Login 버튼 Locator가 저장됩니다.
    login_button = page.get_by_role("button", name="Login")


    # ========================================================
    # 5. 정상 Email 자동 입력
    # ========================================================

    # email_input
    # → 우리가 만든 변수 이름
    #
    # 이 변수에는 Email 입력창 Locator가 들어 있습니다.
    #
    #
    # fill()
    # → Playwright Locator가 제공하는 입력 기능입니다.
    #
    # 우리가 직접 만든 함수가 아닙니다.
    #
    #
    # "qa@example.com"
    # → 우리가 테스트 데이터로 직접 정한 정상 Email입니다.
    #
    # web_demo.py의 정상 Email:
    #
    # VALID_EMAIL = "qa@example.com"
    #
    #
    # 전체 의미:
    #
    # Email 입력창에 Playwright의 fill() 기능을 사용하여
    # qa@example.com을 자동으로 입력한다.
    email_input.fill("qa@example.com")


    # ========================================================
    # 6. 잘못된 Password 자동 입력
    # ========================================================

    # password_input
    # → 우리가 만든 Password 입력창 변수
    #
    #
    # fill()
    # → Playwright Locator가 제공하는 입력 기능
    #
    #
    # "WrongPassword"
    # → 우리가 직접 정한 비정상 Password 테스트 데이터
    #
    #
    # web_demo.py에 정의된 정상 Password는 다음과 같습니다.
    #
    # VALID_PASSWORD = "Password123!"
    #
    # 이번에 입력하는 값:
    #
    # WrongPassword
    #
    # 두 값이 서로 다르기 때문에 로그인 검증 결과는
    # False가 됩니다.
    #
    #
    # 비교 결과:
    #
    # password == VALID_PASSWORD
    #
    # "WrongPassword" == "Password123!"
    #
    # → False
    #
    #
    # Email 비교는 True이지만 Password 비교가 False이므로:
    #
    # True and False
    # → 전체 조건 False
    # → FastAPI else 실행
    # → Login Failed 화면 반환
    password_input.fill("WrongPassword")


    # ========================================================
    # 7. Email 입력값 검증
    # ========================================================

    # expect()
    # → playwright.sync_api에서 가져온
    #   Playwright 검증 기능입니다.
    #
    #
    # email_input
    # → 우리가 만든 Email 입력창 Locator 변수입니다.
    #
    #
    # to_have_value()
    # → Playwright가 제공하는 Locator 값 검증 기능입니다.
    #
    # 입력창 내부의 실제 value가
    # 괄호 안의 기대값과 같은지 확인합니다.
    #
    #
    # "qa@example.com"
    # → 우리가 직접 정한 기대값입니다.
    #
    #
    # 전체 의미:
    #
    # Email 입력창에 실제로 들어간 값이
    # qa@example.com과 같은지 확인한다.
    expect(email_input).to_have_value("qa@example.com")


    # ========================================================
    # 8. 잘못된 Password 입력값 검증
    # ========================================================

    # expect()
    # → Playwright 검증 기능
    #
    # password_input
    # → 우리가 만든 Password 입력창 Locator 변수
    #
    # to_have_value()
    # → Playwright Locator 값 검증 기능
    #
    # "WrongPassword"
    # → 우리가 직접 정한 기대값
    #
    #
    # 브라우저 화면에서는 Password가 점으로 가려져 있지만
    # Playwright는 입력창 내부의 실제 value를 확인합니다.
    expect(password_input).to_have_value("WrongPassword")


    # ========================================================
    # 9. Login 버튼 자동 클릭
    # ========================================================

    # login_button
    # → 우리가 만든 Login 버튼 Locator 변수
    #
    #
    # click()
    # → Playwright Locator가 제공하는 클릭 기능입니다.
    #
    # 사람이 마우스로 버튼을 클릭하는 동작을
    # Playwright가 자동으로 수행합니다.
    #
    #
    # Login 버튼은 type="submit"이므로
    # 버튼을 클릭하면 Form 데이터가 서버로 전송됩니다.
    #
    # 실제 전송 데이터:
    #
    # email=qa@example.com
    # password=WrongPassword
    #
    # 실제 요청:
    #
    # POST /login
    #
    #
    # FastAPI process_login() 함수가 실행되고
    # if 조건을 확인합니다.
    #
    # if email == VALID_EMAIL and password == VALID_PASSWORD:
    #
    # Email은 맞지만 Password가 다르기 때문에
    # 전체 조건은 False가 됩니다.
    #
    # 따라서 else 영역이 실행됩니다.
    login_button.click()


    # ========================================================
    # 10. Login Failed 제목 찾기
    # ========================================================

    # FastAPI의 else가 실행되면 다음 HTML이 반환됩니다.
    #
    # <h1>Login Failed</h1>
    # <p>Invalid email or password</p>
    # <a href="/login">Back to Login</a>
    #
    #
    # page.get_by_role()
    # → Playwright Page가 제공하는 요소 탐색 기능
    #
    # "heading"
    # → 제목 역할 요소 탐색
    #
    # name="Login Failed"
    # → 화면에 Login Failed라고 표시된 제목 탐색
    #
    #
    # login_failed_heading
    # → 우리가 직접 만든 변수 이름입니다.
    #
    # 이 변수에는 Login Failed 제목 Locator가 저장됩니다.
    login_failed_heading = page.get_by_role(
        "heading",
        name="Login Failed",
    )


    # ========================================================
    # 11. 실패 안내 문구 찾기
    # ========================================================

    # page.get_by_text()
    # → 화면에 표시된 실제 글자를 기준으로
    #   요소를 찾는 Playwright Page 기능입니다.
    #
    #
    # "Invalid email or password"
    # → FastAPI 로그인 실패 화면에 표시되는 문구입니다.
    #
    #
    # invalid_message
    # → 우리가 직접 만든 변수 이름입니다.
    #
    # 로그인 실패 문구 Locator를 저장합니다.
    invalid_message = page.get_by_text(
        "Invalid email or password"
    )


    # ========================================================
    # 12. Back to Login 링크 찾기
    # ========================================================

    # 현재 실패 화면의 HTML:
    #
    # <a href="/login">Back to Login</a>
    #
    # a 태그는 브라우저와 Playwright에서
    # link 역할로 인식됩니다.
    #
    #
    # page.get_by_role("link", name="Back to Login")
    #
    # "link"
    # → 링크 역할의 요소를 찾습니다.
    #
    # name="Back to Login"
    # → 화면에 Back to Login이라고 표시된 링크를 찾습니다.
    #
    #
    # back_to_login_link
    # → 우리가 직접 만든 변수 이름입니다.
    #
    # 해당 변수에는 Back to Login 링크 Locator가 저장됩니다.
    back_to_login_link = page.get_by_role(
        "link",
        name="Back to Login",
    )


    # ========================================================
    # 13. Login Failed 제목 표시 여부 검증
    # ========================================================

    # expect()
    # → Playwright 검증 기능
    #
    # login_failed_heading
    # → 우리가 만든 Login Failed 제목 Locator 변수
    #
    # to_be_visible()
    # → Playwright가 제공하는 가시성 검증 기능
    #
    #
    # Login Failed 제목이 화면에 보이면:
    # → 기대 결과와 실제 결과 일치
    # → 검증 PASS
    #
    # 보이지 않으면:
    # → 검증 FAIL
    expect(login_failed_heading).to_be_visible()


    # ========================================================
    # 14. 실패 안내 문구 표시 여부 검증
    # ========================================================

    # Expected Result:
    #
    # Invalid email or password가 화면에 보여야 한다.
    #
    # Actual Result:
    #
    # Playwright가 현재 화면에서 해당 문구를 찾습니다.
    #
    # 문구가 보이면 PASS하고,
    # 보이지 않으면 FAIL합니다.
    expect(invalid_message).to_be_visible()


    # ========================================================
    # 15. Back to Login 링크 표시 여부 검증
    # ========================================================

    # 이번 단계에서는 Back to Login 링크를 클릭하지 않고,
    # 실패 화면에 정상적으로 표시되는지만 확인합니다.
    #
    # 링크가 화면에 보이면 PASS합니다.
    expect(back_to_login_link).to_be_visible()


    # ========================================================
    # 16. 포트폴리오 스크린샷을 위한 임시 대기
    # ========================================================

    # page.wait_for_timeout()
    # → Playwright Locator 기능이 아니라
    #   Playwright Page 객체가 제공하는 대기 기능입니다.
    #
    #
    # 10000
    # → 우리가 직접 정한 대기 시간입니다.
    #
    # 단위는 밀리초입니다.
    #
    # 1000밀리초 = 1초
    # 10000밀리초 = 10초
    #
    #
    # 로그인 실패 화면을 직접 확인하고
    # 스크린샷을 촬영하기 위해 10초 동안 유지합니다.
    #
    # 이 코드는 PASS/FAIL 검증을 위한 필수 코드는 아닙니다.
    # 포트폴리오 증빙 확보를 위한 임시 코드입니다.
    page.wait_for_timeout(10000)


