import pytest
from pages.facebook_page import FacebookPage
from aux_files.manage_files import get_test_cases as tc

@pytest.mark.parametrize("case",tc("facebook_login_test_cases.json"), ids=lambda x: x["id"])
def test_login_facebook(driver, case):
    # initialice the page
    fbPage = FacebookPage(driver)
    # open facebook page
    fbPage.go_to()
    # assert login fb page
    assert "Facebook - log in or sign up" in fbPage.get_page_title()

    # load the credentials by parameter
    fbPage.enter_credentials(case["email"], case["password"])
    # click login button
    fbPage.click_login()

    # get the description of the test case for the match
    des = case["description"]

    # assert according to description
    match des:
        case "Correct login":
            assert "https://www.facebook.com/two_step_verification/authentication/" in fbPage.get_current_url(), 'Did not reach the expected two-step verification page after login'
        case "Email not registred":
            assert fbPage.was_the_wrong_credentials(), "The 'Wrong Credentials Invalid username or password' message didn't show up"
        case "Empty Fields":
            assert fbPage.were_inputs_empty(), "The inputs were not empty"
