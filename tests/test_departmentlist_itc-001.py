from pages.department_list_page import DepartmentListPage

def test_itc_001(driver):
    departmentList = DepartmentListPage(driver)
    departmentList.go_to()
    assert departmentList.get_empty_td_text() == "No departments found. Add a new one!", "The text in the empty TD is not as expected."