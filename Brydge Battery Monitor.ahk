#Persistent
#SingleInstance Force

Menu, Tray, Tip, Brydge Battery Monitor

CheckBatteryStatus() {
    PowerShellCommand := "
    (
        Get-PnpDevice -FriendlyName '*Brydge*' | ForEach-Object {
            $local:test = $_ | 
            Get-PnpDeviceProperty -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' | 
                Where Type -ne Empty;
            if ($test) {
                Get-PnpDeviceProperty -InstanceId $($test.InstanceId) -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' | % Data
            }
        }
    )"

    BatteryPercentage := RunPowerShellCommand(PowerShellCommand)
    BatteryPercentage := RegExReplace(BatteryPercentage, "[^\d]")
    
    if (BatteryPercentage != "")
    {
        BatteryIcon := Round(BatteryPercentage) . ".ico"
        IconPath := A_ScriptDir "\Icons\" . BatteryIcon

        if (FileExist(IconPath)) {
            Menu, Tray, Icon, %IconPath%
        } else {
            MsgBox, Error: Icon file %IconPath% not found!
            Menu, Tray, Icon, error.ico
        }
    }
    else
    {
        MsgBox, Error: Failed to retrieve battery percentage!
        Menu, Tray, Icon, error.ico
    }
}

SetTimer, CheckBatteryStatus, 60000  ; Run every 60 seconds
CheckBatteryStatus()
Return

RunPowerShellCommand(command)
{
    Shell := ComObjCreate("WScript.Shell")
    psCommand := "powershell -NoLogo -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -Command """ . command . """"
    outputFile := A_Temp "\PSOut_" . A_Now . ".txt"
    Shell.Run(psCommand . " > """ outputFile """ 2>&1", 0, true)
    FileRead, result, %outputFile%
    FileDelete, %outputFile%
    return result
}
