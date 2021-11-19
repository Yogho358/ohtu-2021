*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle1
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Welcome Page Should Be Open
    
Register With Too Short Username And Valid Password
    Set Username    ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  kalle2
    Set Password  ka
    Set Password Confirmation  ka
    Submit Registration
    Register Should Fail With Message  Password must be at least 8 charcters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle3
    Set Password  kalle123
    Set Password  kalle321
    Submit Registration
    Register Should Fail With Message  Passwords don't match

Login After Succesful Registration
    Set Username  kalle4
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Go To Login Page
    Set Username  kalle4
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle5
    Set Password  kal
    Set Password Confirmation  kal
    Submit Registration
    Go To Login Page
    Set Username  kalle5
    Set Password  kal
    Submit Credentials
    Login Should Fail With Message  Invalid username or password