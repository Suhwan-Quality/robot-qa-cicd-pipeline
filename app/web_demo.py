# typing은 Python에서 값의 타입 정보를 표현할 때 사용하는
# Python 표준 라이브러리입니다.
#
# 표준 라이브러리라는 것은 FastAPI처럼 별도로 만든 외부 기능이 아니라,
# Python을 설치하면 기본으로 함께 제공되는 기능이라는 뜻입니다.
#
# Annotated는 하나의 값에 다음 정보를 함께 표시할 때 사용합니다.
#
# 1. Python에서 사용할 데이터 타입
# 2. FastAPI가 값을 어디에서 가져와야 하는지에 대한 추가 정보
#
# 이후 다음 코드에서 사용합니다.
#
# email: Annotated[str, Form()]
#
# str
# → email 값은 Python 문자열입니다.
#
# Form()
# → email 값을 HTML Form 데이터에서 가져옵니다.
from typing import Annotated

# ============================================================
# FastAPI 실제 로그인 Web Demo
# 현재 학습 단계:
#   1. FastAPI 웹 애플리케이션 생성
#   2. GET /login 주소 등록
#   3. HTMLResponse를 이용해 HTML 화면 반환
#   4. 브라우저에 Login 제목 표시
#
# 아직 추가하지 않은 기능:
#   - Email 입력창
#   - Password 입력창
#   - Login 버튼
#   - 로그인 정상/실패 판정
# ============================================================


# fastapi 라이브러리에서 두 가지 기능을 가져옵니다.
#
# FastAPI
# → 웹 애플리케이션을 만들기 위한 클래스입니다.
#
# Form
# → HTML Form을 통해 전송된 입력값을
#   FastAPI 함수에서 받을 수 있도록 하는 기능입니다.
#
# HTML에는 다음 코드가 있습니다.
#
# <form action="/login" method="post">
#
# 이 Form 안에서 전송된 Email 값을
# Python의 email 변수로 받기 위해 Form을 사용합니다.
from fastapi import FastAPI, Form


# fastapi.responses 모듈 안에 있는
# HTMLResponse 클래스를 가져옵니다.
#
# FastAPI는 기본적으로 API 응답을 JSON 형식으로 처리합니다.
#
# HTMLResponse를 사용하지 않았을 때:
#   return "Login"
#
# 브라우저 표시:
#   "Login"
#
# HTMLResponse를 사용했을 때:
#   return "<h1>Login</h1>"
#
# 브라우저 표시:
#   Login이라는 글자가 큰 제목으로 표시됩니다.
#
# 즉, HTMLResponse는 Python 함수가 반환한 문자열을
# 일반 JSON 문자열이 아니라 HTML 문서로 전달할 때 사용합니다.
from fastapi.responses import HTMLResponse


# FastAPI 웹 애플리케이션 객체를 생성합니다.
#
# 오른쪽의 FastAPI()
#   → FastAPI 클래스를 실제로 실행하여
#     웹 애플리케이션 객체를 하나 만듭니다.
#
# 왼쪽의 app
#   → 생성된 웹 애플리케이션 객체를 저장할 변수 이름입니다.
#
# 전체 의미:
#   FastAPI 웹 애플리케이션을 만들고
#   그 결과를 app이라는 변수에 저장합니다.
#
# 이후 /login 같은 웹 주소는
# 모두 이 app 객체에 등록하게 됩니다.
app = FastAPI()

# ============================================================
# GET /login 주소 등록
# ============================================================

# 브라우저가 GET 방식으로 /login 주소에 접속하면
# 바로 아래의 show_login_page() 함수를 실행하도록 등록합니다.
#
# 전체 접속 주소:
#   http://127.0.0.1:8000/login
#
# 이 한 줄은 다음 네 부분으로 나누어 이해할 수 있습니다.
#
# 1. @
#    → 바로 아래 함수를 특별한 기능과 연결하는
#      Python의 데코레이터 문법입니다.
#
#    여기서는 show_login_page() 함수를
#    FastAPI의 GET /login 주소와 연결합니다.
#
# 2. app
#    → 위에서 app = FastAPI()로 만든
#      FastAPI 웹 애플리케이션 객체입니다.
#
# 3. .get("/login")
#    → app 객체가 가지고 있는 get 기능을 사용하여
#      GET 방식의 /login 주소를 등록합니다.
#
# 4. response_class=HTMLResponse
#    → 아래 함수가 반환한 문자열을
#      HTML 형식의 응답으로 처리하라고 지정합니다.
#
# response_class는 우리가 임의로 만든 이름이 아닙니다.
# FastAPI의 get() 기능에 원래 정의되어 있는 매개변수입니다.
#
# HTMLResponse도 우리가 직접 만든 클래스가 아닙니다.
# 위에서 다음 import 코드로 가져온 FastAPI 제공 기능입니다.
#
# from fastapi.responses import HTMLResponse
# app이라는 FastAPI 웹서비스에 GET 방식의 /login 주소를 등록하고,
# 바로 아래 함수의 반환값은 HTMLResponse를 사용해 HTML 문서로 브라우저에 전달한다.
#
# ============================================================
# 로그인 검증에 사용할 정상 계정
# ============================================================
#
# 이번 학습용 로그인 Demo에서 사용할
# 정상 Email과 정상 Password를 미리 정해둡니다.
#
# 사용자가 Login 버튼을 눌렀을 때 전달된 값과
# 아래 정상 계정 값을 비교합니다.
#
# 변수 이름을 모두 대문자로 작성한 이유:
#
# Python에서는 프로그램 실행 중 변경하지 않을
# 고정된 값을 표현할 때 대문자 이름을 주로 사용합니다.
#
# VALID
# → 정상적인, 유효한
#
# EMAIL
# → 이메일
#
# PASSWORD
# → 비밀번호
#
# 따라서 다음과 같이 해석할 수 있습니다.
#
# VALID_EMAIL
# → 정상 계정의 Email
#
# VALID_PASSWORD
# → 정상 계정의 Password
VALID_EMAIL = "qa@example.com"
VALID_PASSWORD = "Password123!"

@app.get("/login", response_class=HTMLResponse)
def show_login_page() -> str:
    # def
    #   → Python에서 함수를 정의할 때 사용하는 문법입니다.
    #
    # show_login_page
    #   → 함수 이름입니다.
    #
    # 이름을 나누면:
    #   show       = 보여준다
    #   login_page = 로그인 페이지를
    #
    # ()
    #   → 이 함수가 외부에서 전달받는 값이
    #     현재는 없다는 의미입니다.
    #
    # -> str
    #   → 이 함수가 실행된 후
    #     문자열을 반환한다는 타입 힌트입니다.
    #
    # 마지막의 :
    #   → 함수 내부 코드가 시작된다는 의미입니다.
    #
    # 이 함수는 서버가 시작되는 순간 바로 실행되지 않습니다.
    # 서버 시작 시에는 /login 주소와 연결만 됩니다.
    #
    # 실제 실행 시점:
    #   브라우저가 GET /login 요청을 보냈을 때


    # return은 함수가 만든 결과를
    # 함수를 호출한 위치로 돌려주는 Python 문법입니다.
    #
    # HTML 문서는 여러 줄로 작성해야 읽기 편하므로
    # 큰따옴표 세 개(""" ... """)를 사용합니다.
    #
    # Python 입장에서 아래 HTML 전체는
    # 하나의 긴 문자열입니다.
    return """

    <!DOCTYPE html>

    <html lang="en">

        <head>
            <meta charset="UTF-8">

            <title>QA Demo Login</title>
        </head>


        <body>

            <!--
                h1은 페이지에서 가장 중요한 큰 제목입니다.

                화면에는 Login이라는 큰 제목이 표시됩니다.

                나중에 Playwright에서는 다음처럼 찾을 수 있습니다.

                page.get_by_role("heading", name="Login")
            -->
            <h1>Login</h1>


            <!--
                form은 여러 개의 입력값을 하나로 묶어서
                서버에 전송하기 위한 HTML 영역입니다.

                앞으로 이 form 안에 다음 요소를 추가합니다.

                1. Email 입력창
                2. Password 입력창
                3. Login 버튼

                사용자가 Login 버튼을 누르면
                form 안에 입력한 Email과 Password가
                FastAPI 서버로 전송됩니다.
            -->
            <form action="/login" method="post">

             <!--
                label은 입력창의 이름과 용도를
                사용자에게 알려주는 HTML 태그입니다.

                for="email"은 아래 입력창의
                id="email"과 연결됩니다.

                두 값이 모두 email로 같기 때문에
                브라우저와 Playwright가
                이 Label과 입력창의 관계를 이해할 수 있습니다.
            -->
            <label for="email">Email</label>


            <!--
                input은 사용자가 값을 직접 입력할 수 있는
                HTML 입력창을 만드는 태그입니다.

                이번 입력창에서는 사용자가
                이메일 주소를 입력하게 됩니다.

                input은 <input>으로 시작한 뒤
                </input>으로 닫지 않는 HTML 태그입니다.
                사용자가 값을 직접 입력할 수 있는 입력창을 만드는 HTML 태그

                아래에 작성한 id, name, type, required는
                input의 동작과 역할을 설정하는 HTML 속성입니다.

                id는 HTML 화면 안에서 특정 요소를 구분하기 위한 고유한 이름
                name은 Form을 서버로 전송할 때 사용할 데이터 이름
                type은 입력창이 이메일 주소를 입력하는 용도라는 것을 브라우저 알려준다
                required는 이 입력창을 비워두면 안 된다는 뜻
             -->
            <input
                id="email"
                name="email"
                type="email"
                required
            >
            <!--
                br은 줄을 바꾸기 위한 HTML 태그입니다.

                현재 Email 입력창 다음에 바로 Password Label을 작성하면
                Email 입력창과 Password 글자가 같은 줄에 붙어서
                표시될 수 있습니다.

                <br>을 한 번 사용하면 한 줄을 바꾸고,
                두 번 사용하면 한 줄 정도의 여백을 만들 수 있습니다.

                br은 input과 마찬가지로 내부 내용이 없는 태그이므로
                </br> 종료 태그를 작성하지 않습니다.

                현재는 CSS를 배우는 단계가 아니므로
                화면을 간단히 구분하기 위해 <br><br>을 사용합니다.
            -->
            <br><br>


            <!--
                label은 입력창이 어떤 값을 받는지
                사용자에게 알려주는 이름표 역할을 합니다.

                화면에는 Password라는 글자가 표시됩니다.

                for="password"는 앞으로 추가할
                id="password" 입력창과 이 Label을 연결하겠다는 의미입니다.

                현재는 아직 id="password" 입력창을 만들지 않았기 때문에
                Password라는 글자만 화면에 표시됩니다.

                다음 단계에서 Password 입력창을 추가하면
                다음 두 값이 서로 연결됩니다.

                label의 for="password"
                input의 id="password"

                나중에 Playwright에서는 다음 코드로
                Password 입력창을 찾을 수 있습니다.

                page.get_by_label("Password")
            -->
            <label for="password">Password</label>

            <!--
                input은 사용자가 값을 직접 입력할 수 있는
                HTML 입력창을 만드는 태그입니다.

                이번 input은 비밀번호를 입력하는 용도로 사용합니다.

                id="password"
                → 현재 HTML 화면에서 이 입력창을 구분하는 고유한 이름입니다.

                위에 작성한 Password Label의
                for="password"와 같은 값을 사용합니다.

                label의 for="password"
                        ↓ 연결
                input의 id="password"

                이 연결 덕분에 사용자가 Password 글자를 클릭하면
                Password 입력창으로 커서가 이동합니다.

                나중에 Playwright에서도 다음 코드로
                Password 입력창을 찾을 수 있습니다.

                page.get_by_label("Password")


                name="password"
                → Login 버튼을 눌러 Form 데이터를 서버에 전송할 때
                  이 입력값에 사용할 데이터 이름입니다.

                사용자가 Password123!을 입력하면
                서버에는 개념적으로 다음과 같이 전달됩니다.

                password=Password123!

                나중에 FastAPI에서는 이 name 값을 기준으로
                password라는 Python 변수에서 입력값을 받게 됩니다.


                type="password"
                → 이 입력창을 비밀번호 입력용으로 설정합니다.

                사용자가 Password123!을 입력해도
                브라우저 화면에는 실제 글자가 그대로 보이지 않고
                점 또는 동그라미 형태로 가려져 표시됩니다.

                주의:
                type="password"는 화면에서 글자를 숨기는 기능입니다.
                비밀번호를 암호화해서 저장하는 기능은 아닙니다.


                required
                → Password 입력창을 비워두면 안 된다는 뜻입니다.

                나중에 Login 버튼을 누를 때 비밀번호가 비어 있으면
                브라우저가 Form 전송을 막고 입력을 요구합니다.
            -->
            <input
                id="password"
                name="password"
                type="password"
                required
            >
            <!--
                br은 HTML 화면에서 줄을 바꾸는 태그입니다.

                Password 입력창 바로 뒤에 버튼을 작성하면
                Password 입력창과 Login 버튼이 같은 줄에
                붙어서 표시될 수 있습니다.

                <br><br>을 사용하여 줄을 바꾸고
                입력창과 버튼 사이에 간단한 간격을 만듭니다.

                현재는 CSS를 배우기 전이므로
                임시로 br 태그를 사용합니다.
            -->
            <br><br>


            <!--
                button은 사용자가 클릭할 수 있는
                HTML 버튼을 만드는 태그입니다.

                시작 태그:
                    <button type="submit">

                화면에 표시할 글자:
                    Login

                종료 태그:
                    </button>

                따라서 브라우저 화면에는
                Login이라는 글자가 들어 있는 버튼이 표시됩니다.


                type="submit"
                → 이 버튼이 단순한 일반 버튼이 아니라
                  현재 form의 입력값을 서버로 전송하는 버튼이라는 뜻입니다.

                사용자가 Login 버튼을 클릭하면
                현재 form 안에 있는 다음 값들을 모읍니다.

                1. name="email" 입력값
                2. name="password" 입력값

                그리고 form 시작 태그에 작성한 설정을 확인합니다.

                action="/login"
                → 입력값을 /login 주소로 전송합니다.

                method="post"
                → POST 방식으로 전송합니다.

                최종적으로 발생하는 요청:

                POST /login


                나중에 Playwright에서는 다음처럼
                화면에 보이는 버튼 이름을 기준으로 찾습니다.

                page.get_by_role("button", name="Login")

                그리고 다음처럼 자동으로 클릭합니다.

                page.get_by_role("button", name="Login").click()
            -->
            <button type="submit">Login</button>
            <!--
                사용자가 클릭하면 현재 Form의 Email과 Password 값을 POST 방식으로 /login 주소에 전송하는 Login 버튼을 만든다.
            -->

            </form>

        </body>

    </html>
    """

# ============================================================
# POST /login 요청 처리
# ============================================================

# 사용자가 Login 버튼을 클릭하면
# HTML form에 작성한 다음 설정에 따라 요청이 발생합니다.
#
# form 설정:
#
# <form action="/login" method="post">
#
# action="/login"
# → 입력 데이터를 /login 주소로 전송합니다.
#
# method="post"
# → GET이 아니라 POST 방식으로 전송합니다.
#
# 따라서 Login 버튼을 클릭하면 브라우저가
# FastAPI 서버에 다음 요청을 보냅니다.
#
# POST /login
#
# @app.post("/login")은 바로 아래의 process_login() 함수를
# POST /login 요청과 연결하는 FastAPI 데코레이터입니다.
#
# 기존 코드:
#
#   @app.get("/login")
#
# 역할:
#   로그인 화면을 브라우저에 보여줍니다.
#
# 새 코드:
#
#   @app.post("/login")
#
# 역할:
#   사용자가 Login 버튼을 눌러 전송한 요청을 처리합니다.
#
# 같은 "/login" 주소를 사용하지만
# GET과 POST는 서로 다른 HTTP 요청이므로
# FastAPI는 두 함수를 구분해서 실행합니다.
#
# response_class=HTMLResponse
#   → process_login() 함수가 반환한 문자열을
#     JSON이 아닌 HTML 화면으로 브라우저에 전달합니다.
#
# POST 방식으로 /login 요청이 들어오면
# 바로 아래 process_login() 함수를 실행합니다.
#
# response_class=HTMLResponse
# → 함수가 반환한 문자열을 HTML 문서로 전달합니다.
@app.post("/login", response_class=HTMLResponse)
def process_login(
    # HTML Form에서 name="email"로 전송된 값을 받습니다.
    #
    # email
    # → Python 함수 안에서 사용할 변수 이름입니다.
    #
    # Annotated[...]
    # → email 값에 타입 정보와 FastAPI 처리 정보를
    #   함께 연결합니다.
    # → 타입에 추가 설명을 붙이는 Python 기능
    #
    # [
    # → Annotated 안에 넣을 정보 시작
    #
    # str
    # → email 값은 문자열로 사용합니다.
    #
    # Form()
    # → email 값을 JSON이나 URL이 아니라
    #   HTML Form 데이터에서 가져오라고 FastAPI에 알려줍니다.
    #
    # HTML 입력창의 다음 속성과 연결됩니다.
    #
    # name="email"
    #
    # HTML:
    #   <input name="email">
    #
    # Python:
    #   email: Annotated[str, Form()]
    # ]
    # → Annotated 정보 종료
    #
    # HTML Form에서 email이라는 이름으로 전송된 값을 가져와서 Python의 문자열 변수 email에 저장한다.
    # 사용자가 Submit을 누르면 FastAPI가 전송된 Email과 Password를 받아서, 미리 정해둔 정상 계정과 비교한 후 로그인 성공 또는 실패를 결정한다.
    # Submit으로 전송된 로그인 입력값을 FastAPI가 받아서, Python으로 비교할 수 있게 만들어 주는 연결 부분
    email: Annotated[str, Form()],

    # --------------------------------------------------------
    # Password Form 데이터 받기
    # --------------------------------------------------------

    # 사용자가 Login 버튼을 누르면
    # HTML의 name="password"에 입력된 값도
    # POST /login 요청으로 서버에 전송됩니다.
    #
    # HTML:
    #   <input name="password">
    #
    # Python:
    #   password: Annotated[str, Form()]
    #
    # password
    # → 전달받은 Password 값을 저장할 Python 변수입니다.
    #
    # str
    # → Password 값을 문자열로 사용합니다.
    #
    # Form()
    # → POST 요청의 Form 데이터에서
    #   password라는 이름의 값을 가져옵니다.
    password: Annotated[str, Form()],
) -> str:
    # Email과 Password가 모두 정상적으로 전달되어야
    # process_login() 함수가 여기까지 실행됩니다.
    #
    # 실제 Password 값은 보안상 브라우저 화면에 표시하지 않습니다.
    #
    # 대신 함수가 정상 실행되었다는 메시지를 표시하여
    # Email과 Password가 모두 전달되었다는 것을 확인합니다.
    #
    # 위 설명과 Login Data Received 화면은
    # Email과 Password가 FastAPI까지 정상적으로 전달되는지
    # 확인하기 위해 사용했던 이전 학습 단계입니다.
    #
    # 이번 단계에서는 전달받은 Email과 Password를
    # 미리 정해둔 정상 계정과 실제로 비교한 뒤,
    # 로그인 성공 화면 또는 로그인 실패 화면을 반환합니다.

    # ========================================================
    # if / else를 사용한 로그인 성공·실패 판단
    # ========================================================

    # if는 영어로 "만약"이라는 뜻입니다.
    #
    # Python에서는 다음과 같이 사용합니다.
    #
    # if 조건:
    #     조건이 맞을 때 실행할 코드
    # else:
    #     조건이 맞지 않을 때 실행할 코드
    #
    # 현재 로그인 기능에 적용하면 다음 뜻입니다.
    #
    # 만약 사용자가 입력한 Email과 Password가
    # 미리 정해둔 정상 계정과 모두 같다면:
    #     로그인 성공 화면을 보여줍니다.
    # 그렇지 않다면:
    #     로그인 실패 화면을 보여줍니다.

    # --------------------------------------------------------
    # 첫 번째 비교: Email이 같은지 확인
    # --------------------------------------------------------

    # email
    # → 사용자가 로그인 화면에서 입력한 Email 값입니다.
    #
    # VALID_EMAIL
    # → 위에서 미리 정해둔 정상 Email 값입니다.
    #
    # ==
    # → 왼쪽 값과 오른쪽 값이 같은지 비교합니다.
    #
    # 따라서 다음 코드는
    # 사용자가 입력한 Email과 정상 Email이 같은지 확인합니다.
    #
    # email == VALID_EMAIL
    #
    # 두 값이 같으면 결과는 True입니다.
    # 두 값이 다르면 결과는 False입니다.

    # --------------------------------------------------------
    # 두 번째 비교: Password가 같은지 확인
    # --------------------------------------------------------

    # password
    # → 사용자가 로그인 화면에서 입력한 Password 값입니다.
    #
    # VALID_PASSWORD
    # → 위에서 미리 정해둔 정상 Password 값입니다.
    #
    # 따라서 다음 코드는
    # 사용자가 입력한 Password와 정상 Password가 같은지 확인합니다.
    #
    # password == VALID_PASSWORD

    # --------------------------------------------------------
    # and: 두 조건이 모두 맞아야 함
    # --------------------------------------------------------

    # and는 영어로 "그리고"라는 뜻입니다.
    #
    # 로그인에서는 Email만 맞아도 안 되고,
    # Password만 맞아도 안 됩니다.
    #
    # Email과 Password가 모두 맞아야 로그인 성공이므로
    # 두 비교 조건 사이에 and를 사용합니다.
    #
    # email == VALID_EMAIL and password == VALID_PASSWORD
    #
    # 결과는 다음과 같습니다.
    #
    # Email 정상 + Password 정상
    # → True and True
    # → 전체 조건 True
    # → 로그인 성공
    #
    # Email 정상 + Password 비정상
    # → True and False
    # → 전체 조건 False
    # → 로그인 실패
    #
    # Email 비정상 + Password 정상
    # → False and True
    # → 전체 조건 False
    # → 로그인 실패
    #
    # Email 비정상 + Password 비정상
    # → False and False
    # → 전체 조건 False
    # → 로그인 실패

    # --------------------------------------------------------
    # = 한 개와 == 두 개의 차이
    # --------------------------------------------------------

    # = 한 개
    # → 변수에 값을 저장합니다.
    #
    # 예:
    # VALID_EMAIL = "qa@example.com"
    #
    # == 두 개
    # → 두 값이 같은지 비교합니다.
    #
    # 예:
    # email == VALID_EMAIL

    # --------------------------------------------------------
    # 콜론(:)과 들여쓰기
    # --------------------------------------------------------

    # if 조건문의 마지막에는 콜론(:)을 작성합니다.
    #
    # 콜론은 조건 작성이 끝났고,
    # 다음 줄부터 조건이 맞을 때 실행할 코드가
    # 시작된다는 뜻입니다.
    #
    # if 아래에 포함되는 코드는
    # 반드시 공백 4칸으로 들여쓰기합니다.
    #
    # Python은 중괄호가 아니라 들여쓰기를 보고
    # 어떤 코드가 if 또는 else에 포함되는지 구분합니다.

    # 사용자가 입력한 Email이 정상 Email과 같고,
    # 사용자가 입력한 Password도 정상 Password와 같다면
    # 전체 조건이 True가 됩니다.
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        # 이 부분은 if 조건이 True일 때만 실행됩니다.
        #
        # 즉 Email과 Password가 모두 정상 계정과 같은 경우입니다.
        #
        # return은 다음 두 가지 역할을 합니다.
        #
        # 1. 아래 HTML 문자열을 브라우저에 반환합니다.
        # 2. process_login() 함수 실행을 여기에서 끝냅니다.
        #
        # 브라우저에는 다음 내용이 표시됩니다.
        #
        # Dashboard
        # Welcome, QA User
        #
        # 나중에 Playwright에서는 다음과 같이 검증할 수 있습니다.
        #
        # page.get_by_role("heading", name="Dashboard")
        # expect(page.get_by_text("Welcome, QA User")).to_be_visible()
        return """
        <h1>Dashboard</h1>
        <p>Welcome, QA User</p>
        """

    else:
        # else는 영어로 "그렇지 않다면"이라는 뜻입니다.
        #
        # 위의 if 조건 결과가 False일 때 실행됩니다.
        #
        # 즉 다음 중 하나에 해당하면 로그인에 실패합니다.
        #
        # 1. Email만 틀림
        # 2. Password만 틀림
        # 3. Email과 Password가 모두 틀림
        #
        # 보안을 위해 어떤 값이 틀렸는지 각각 알려주지 않고
        # 다음 공통 문구를 표시합니다.
        #
        # Invalid email or password
        #
        # return을 만나면 실패 HTML을 브라우저에 반환하고
        # process_login() 함수 실행을 끝냅니다.
        #
        # Back to Login 링크를 클릭하면
        # GET /login 주소로 돌아가 다시 로그인할 수 있습니다.
        #
        # 나중에 Playwright에서는 다음과 같이 검증할 수 있습니다.
        #
        # expect(page.get_by_text("Invalid email or password")).to_be_visible()
        # page.get_by_role("link", name="Back to Login").click()
        return """
        <h1>Login Failed</h1>
        <p>Invalid email or password</p>
        <a href="/login">Back to Login</a>
        """