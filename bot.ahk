#singleInstance Force
#NoEnv
#Warn

^!s:: 
Loop
{ 
	Sleep, 40001 
	
	Send, pls fish
	Send, {Enter}
	Sleep, 100
	
	Send, pls hunt
	Send, {Enter}
	Sleep, 100
	
	Send, pls dig
	Send, {Enter}
	Sleep, 100

	Send, pls deposit all
	Send, {Enter}
	Sleep, 100

} 
return

^q::
	Exit