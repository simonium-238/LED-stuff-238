<?php
if(isset($_GET['data']))
{
    $data = $_GET['data'];
    $data = explode('.', $data);
    $mode  = $data[0];
    $hex = $data[1];
    $time = $data[2];
    echo shell_exec("^C");
    echo shell_exec("python /home/pi/controller.py '" . $mode . "' '" . $hex . "' '" . $time . "'");
}
?>