# Playwright에서 Page 타입과 expect 검증 기능을 가져온다.
#
# Page:
# Chromium 브라우저에서 열리는 페이지 또는 탭 하나를 의미한다.
#
# expect:
# 브라우저 화면의 실제 상태가
# 우리가 예상한 결과와 같은지 확인하는 기능이다.
from playwright.sync_api import Page, expect


# 함수 이름이 test_로 시작하기 때문에
# pytest가 자동으로 테스트 함수로 인식한다.
#
# 함수 이름의 의미:
# 유효한 이메일과 비밀번호를 입력해 로그인하면
# Dashboard가 정상적으로 표시되는지 검증한다.
#
# page:
# pytest-playwright가 준비한 브라우저 페이지 객체이다.
#
# page: Page:
# page 변수에 Playwright의 Page 객체가 들어온다는 뜻이다.
#
# -> None:
# 테스트 함수가 별도의 결과값을 return하지 않는다는 뜻이다.
def test_login_success_shows_dashboard(page: Page) -> None:

    # 현재는 실제 Web Application을 만들기 전 단계이므로
    # page.set_content()를 사용해
    # 학습용 로그인 화면을 브라우저에 직접 생성한다.
    #
    # 다음 단계에서는 FastAPI로 실제 Web 페이지를 만들고
    # page.goto("실제 주소") 방식으로 전환한다.
    page.set_content(
        """
        <h1>QA Demo Service</h1>

        <label for="email">
            Email
        </label>

        <input
            id="email"
            type="email"
        >

        <br><br>

        <label for="password">
            Password
        </label>

        <input
            id="password"
            type="password"
        >

        <br><br>

        <button
            type="button"
            onclick="login()"
        >
            Login
        </button>

        <p
            id="login-message"
            data-testid="login-message"
        >
        </p>

        <section
            id="dashboard"
            data-testid="dashboard"
            hidden
        >
            <h2>Dashboard</h2>

            <p>
                Welcome, QA User
            </p>
        </section>

        <script>
            function login() {
                const email =
                    document.getElementById("email").value;

                const password =
                    document.getElementById("password").value;

                if (
                    email === "qa@example.com"
                    &&
                    password === "Password123!"
                ) {
                    document.getElementById(
                        "dashboard"
                    ).hidden = false;

                    document.getElementById(
                        "login-message"
                    ).textContent = "";
                } else {
                    document.getElementById(
                        "login-message"
                    ).textContent =
                        "Invalid email or password";
                }
            }
        </script>
        """
    )


    # 화면에서 Email 입력칸을 찾아
    # email_input 변수에 Locator로 저장한다.
    #
    # get_by_label("Email"):
    # Email이라는 label과 연결된 입력 요소를 찾는다.
    #
    # HTML에서는 다음 두 부분이 연결되어 있다.
    #
    # <label for="email">Email</label>
    # <input id="email">
    #
    # label의 for 값과 input의 id 값이 같기 때문에
    # Playwright가 Email 입력칸을 정확히 찾을 수 있다.
    email_input = page.get_by_label(
        "Email"
    )


    # 화면에서 Password 입력칸을 찾아
    # password_input 변수에 Locator로 저장한다.
    #
    # 위와 마찬가지로:
    #
    # <label for="password">Password</label>
    # <input id="password">
    #
    # 두 요소가 연결되어 있기 때문에
    # get_by_label("Password")로 찾을 수 있다.
    password_input = page.get_by_label(
        "Password"
    )


    # 화면에서 Login 버튼을 찾아
    # login_button 변수에 Locator로 저장한다.
    #
    # "button":
    # 버튼 역할을 가진 요소를 찾는다.
    #
    # name="Login":
    # 버튼 중에서 화면에 Login이라고 표시된 요소를 찾는다.
    login_button = page.get_by_role(
        "button",
        name="Login",
    )


    # 로그인 성공 후 표시될 Dashboard 영역을 찾아
    # dashboard 변수에 Locator로 저장한다.
    #
    # HTML의 다음 속성과 연결된다.
    #
    # data-testid="dashboard"
    dashboard = page.get_by_test_id(
        "dashboard"
    )


    # 로그인하기 전에는 Dashboard가
    # 숨겨진 상태인지 먼저 검증한다.
    #
    # to_be_hidden():
    # 해당 요소가 화면에 보이지 않는 상태인지 확인한다.
    #
    # 로그인 전부터 Dashboard가 보이면
    # 요구사항에 맞지 않으므로 테스트는 FAIL이다.
    expect(dashboard).to_be_hidden()


    # Email 입력칸에 정상 계정을 입력한다.
    #
    # fill():
    # 텍스트 입력 요소에 원하는 값을 입력하는
    # Playwright 메서드이다.
    email_input.fill(
        "qa@example.com"
    )


    # Password 입력칸에 정상 비밀번호를 입력한다.
    password_input.fill(
        "Password123!"
    )


    # Login 버튼을 클릭한다.
    #
    # 버튼을 클릭하면 HTML 안의 login() 함수가 실행된다.
    login_button.click()


    # 정상 계정으로 로그인한 후
    # Dashboard가 화면에 표시됐는지 검증한다.
    #
    # to_be_visible():
    # 해당 요소가 실제 사용자 화면에 보이는지 확인한다.
    expect(dashboard).to_be_visible()


    # Dashboard 안에 있는 환영 문구도 검증한다.
    #
    # Dashboard 영역만 나타났지만
    # 내부 내용이 잘못된 경우까지 잡기 위한 검증이다.
    welcome_message = page.get_by_text(
        "Welcome, QA User"
    )

    expect(welcome_message).to_be_visible()