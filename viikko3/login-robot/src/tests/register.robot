*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
	Create User  kalle   kalle123
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Create User  kalle   kalle123
	Input New Command
	Create User  kalle   kalle123
	Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
	Create User  ka  kalle123
	Output Should Contain  Username must be at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
	Create User  ka113  kalle123
	Output Should Contain  Username must only contain letters

Register With Valid Username And Too Short Password
	Create User  kalle  lyhy7
	Output Should Contain  Password must be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
	Create User  kalle  kahdeksan
	Output Should Contain  Password must contain other characters than letters

*** Keywords ***
Input New Command And Create User
	Input New Command
	Create User  kalle   kalle123