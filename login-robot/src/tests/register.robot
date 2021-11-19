*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input Credentials  kalle  kalle123
    Input  login
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Register With Already Taken Username And Password
    Input  new
    Input Credentials  kalle  kalle123
    Input  new
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input  new
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least three letters long

Register With Valid Username And Too Short Password
    input  new 
    Input Credentials  kalle  1
    Output Should Contain  Password has to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    input  new
    Input Credentials  kalle  aaaaaaaaaa
    Output Should Contain  Password can't be only letters