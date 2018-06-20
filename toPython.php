<?php
if(isset($_GET['mode']))
{
    $mode = $_GET['mode'];
    $currentMode = $_GET['currentMode'];

    if($currentMode != 'none')
    {
        if($currentMode != 'noEffect')
        {
            //echo shell_exec("ps -ef | grep python | exec: kill -9 {}\;");
            echo shell_exec("kill $(ps aux | grep '[p]ython' | awk '{print $2'})");
        }
        echo shell_exec("python /home/pi/controller/shutdown.py");
    }

    switch ($mode) {
        case 'noEffect':
            echo shell_exec("python /home/pi/controller/static.py '" . $hex . "'");
            break;
        case 'singleColorBlink':
            echo shell_exec("python /home/pi/controller/blink.py '" . $hex . "' '" . $time . "'");
            break;
        case 'rgbFade':
            echo shell_exec("python /home/pi/controller/fading.py '" . $time . "'");
            break;
    }
}




if(isset($_GET['turnOff']))
{
    $currentMode == $_GET['turnOff'];
    if($currentMode == 'noEffect')
    {
        echo shell_exec("python /home/pi/controller/shutdown.py");
    }
    else
    {
        echo shell_exec("kill $(ps aux | grep '[p]ython' | awk '{print $2'})");
        echo shell_exec("python /home/pi/controller/shutdown.py");
    }
}
unset($_GET['mode']);
unset($_GET['turnOff']);
?>