*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Register
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  ville
    Set Password  ville
    Set Password Confirmation  ville
    Submit Register
    Register Should Fail With Message  Password must contain other characters than letters

Register With Nonmatching Password And Password Confirmation
# ...
    Set Username  user
    Set Password  ville123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Fail With Message  Password and confirmation does not match

Login After Successful Registration
# ...
    Set Username  test
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Register
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  test
    Set Password  ville123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
# ...
    Set Username  uusi
    Set Password  ville123
    Set Password Confirmation  kalle123
    Submit Register
    Click Link  Login
    Set Username  uusi
    Set Password  ville123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open