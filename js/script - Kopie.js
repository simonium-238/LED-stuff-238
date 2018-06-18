var currentMode = 'none';
var fullRGB;
var finalColor = [255,255,255];
var lastTypedColor = [255,255,255];

function out()
{
    $("#colorSpan").css("opacity", "0");
}

function hover()
{
    $("#debuggingSectionLeft").css("border", "border: solid 3px #d9d9d9");
    $("#colorSpan").css("opacity", "1");
}

function closeColorType()
{
    $("#editColor").css("display", "none");
    $("#debuggingSectionLeft").css("display", "block");
    $("canvas").css("pointer-events", "all");
    
    var r = document.getElementById("redInput").value;
    var g = document.getElementById("greenInput").value;
    var b = document.getElementById("blueInput").value;
    $("#red").text(r);
    $("#green").text(g);
    $("#blue").text(b);
    
    var rgbWritten = "rgba(" + r + "," + g + "," + b + "," + "0.8)";
    
    $(".light").css("background-color",rgbWritten);
    $(".light").css("box-shadow","0 0 60px 40px " + rgbWritten);
    
    rgbWritten = "rgb(" + r + "," + g + "," + b + ")";
    
    $("#debuggingSectionLeft").css("background-color", rgbWritten);
    $("#colorSpan").css("background-color", rgbWritten);
}

function funcEditChange()
{
    var r = document.getElementById("redInput").value;
    var g = document.getElementById("greenInput").value;
    var b = document.getElementById("blueInput").value;
    
    finalColor = [r,g,b];
    lastTypedColor = [r,g,b];
    
    var rgbWritten = "rgb(" + r + "," + g + "," + b + ")";
    
    $("#debuggingSectionLeft").css("background-color", rgbWritten);
    $("#colorSpan").css("background-color", rgbWritten);
    $("#colorPreview").css("background-color", rgbWritten);
}

function funcEditRGB()
{
    $("#debuggingSectionLeft").css("display", "none");
    $("#colorSpan").css("opacity", "0");
    $("#rgbCursor").css("display", "none");
    $("#editColor").css("display", "block");
    $("canvas").css("pointer-events", "none");
    $("#colorPreview").css("background-color", "rgb(" + lastTypedColor[0] + "," + lastTypedColor[1] + "," + lastTypedColor[2] + ")");
    document.styleSheets[0].addRule("input[type=range]::-webkit-slider-runnable-track", "background: linear-gradient(to right, rgb(0,0,0) , rgb(255, 255, 255))");
    document.getElementById("saturation").disabled = true;
}

function func1()
    {
        if(document.getElementById("red").innerHTML != "" && document.getElementById("green").innerHTML != "" && document.getElementById("blue").innerHTML != "")
        {
            //var offset = $("#canvas").offset();
            //var x = $("#rgbCursor").pageX - offset.left - 250;
            //var y = offset.top + 250 - $("#rgbCursor").pageY;
            //var ctx = document.getElementById("canvas").getContext("2d");
            //var rgb= ctx.getImageData(document.getElementById("rgbCursor").style.left - offset.left - 5,document.getElementById("rgbCursor").style.right - offset.right - 5, 1, 1).data;
            
            var hsv= RGBtoHSV(fullRGB);
            hsv[1] = document.getElementById("saturation").value / -100;
            var rgb= HSVtoRGB(hsv);
            finalColor= rgb;
            
            var rgbWritten = "rgb(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + ")";
            
            $("#debuggingSectionLeft").css("background-color", rgbWritten);
            $("#colorSpan").css("background-color", rgbWritten);
            
            rgbWritten = "rgba(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + "," + "0.8)";
            $(".light").css("background-color",rgbWritten);
            $(".light").css("box-shadow","0 0 60px 40px " + rgbWritten);
            
            $("#red").text(Math.round(rgb[0]));
            $("#green").text(Math.round(rgb[1]));
            $("#blue").text(Math.round(rgb[2]));
        }
    };

RGBtoHSV= function(color) {
        var r,g,b,h,s,v;
        r= color[0];
        g= color[1];
        b= color[2];
        min = Math.min( r, g, b );
        max = Math.max( r, g, b );


        v = max;
        delta = max - min;
        if( max != 0 )
            s = delta / max;        // s
        else {
            // r = g = b = 0        // s = 0, v is undefined
            s = 0;
            h = -1;
            return [h, s, undefined];
        }
        if( r === max )
            h = ( g - b ) / delta;      // between yellow & magenta
        else if( g === max )
            h = 2 + ( b - r ) / delta;  // between cyan & yellow
        else
            h = 4 + ( r - g ) / delta;  // between magenta & cyan
        h *= 60;                // degrees
        if( h < 0 )
            h += 360;
        if ( isNaN(h) )
            h = 0;
        return [h,s,v];
    };

HSVtoRGB= function(color) {
        var i;
        var h,s,v,r,g,b;
        h= color[0];
        s= color[1];
        v= color[2];
        if(s === 0 ) {
            // achromatic (grey)
            r = g = b = v;
            return [r,g,b];
        }
        h /= 60;            // sector 0 to 5
        i = Math.floor( h );
        f = h - i;          // factorial part of h
        p = v * ( 1 - s );
        q = v * ( 1 - s * f );
        t = v * ( 1 - s * ( 1 - f ) );
        switch( i ) {
            case 0:
                r = v;
                g = t;
                b = p;
                break;
            case 1:
                r = q;
                g = v;
                b = p;
                break;
            case 2:
                r = p;
                g = v;
                b = t;
                break;
            case 3:
                r = p;
                g = q;
                b = v;
                break;
            case 4:
                r = t;
                g = p;
                b = v;
                break;
            default:        // case 5:
                r = v;
                g = p;
                b = q;
                break;
        }
        return [r,g,b];
    }







window.onload = function(){
    document.getElementById("saturation").disabled = true;
    var canvas = document.getElementById("canvas");     //canvas als variable holen
    var ctx = canvas.getContext("2d");                  //2d-context aus canvas als variable holen
    var img = document.getElementById("imgWheel");      //rgb-ring als variable holen
    ctx.drawImage(img, 0, 0);                          //img koordinatenursprung (obere linke ecke) zeichnen
    
     $("#canvas").mousedown(function getPixelColor(e){ //wird auf den canvas geclickt... event e wird mitgegeben
        
        var offset = $(this).offset(); //offset relativ zur seite als variable holen
        var pixelColor = ctx.getImageData(e.pageX - offset.left, e.pageY - offset.top, 1, 1).data;  //weil ursprung von seite und canvas unterschedlich, wird das jeweilige offset von den seiten koordinaten abgezogen und an diesen koordinaten werden die pixeldaten gespeichert
        
        if(pixelColor[0] == 255 || pixelColor[1] == 255 || pixelColor[2] == 255) //beim rgb ring ist immer eine farbe auf 255. so stellt man fest ob der benutzer auf den ring gecklickt hat
        {
             //var pixelColorWritten = "rgb(" + pixelColor[0] + ", " + pixelColor[1] + ", " + pixelColor[2] + ")"; //werte aus dem pixelColor array so zusammenfügen, dass sie weiterverwendet werden können
            document.getElementById("saturation").disabled = false;
            document.styleSheets[0].addRule("input[type=range]::-webkit-slider-runnable-track", "background: linear-gradient(to right, rgb(" + pixelColor[0] + ", " + pixelColor[1] + ", " + pixelColor[2] + ") , rgb(255, 255, 255))");
            //$("#header").css("background-color", pixelColorWritten);
            
            fullRGB = [pixelColor[0],pixelColor[1],pixelColor[2]]
            var hsv= RGBtoHSV (fullRGB);
            hsv[1] = document.getElementById("saturation").value / -100;
            var rgb= HSVtoRGB(hsv);
            finalColor= rgb;
            
            var rgbWritten = "rgb(" + rgb[0] + ", " + rgb[1] + ", " + rgb[2] + ")";
            
            $("#debuggingSectionLeft").css("background-color", rgbWritten);
            $("#colorSpan").css("background-color", rgbWritten);
            
            $("#red").text(Math.round(rgb[0]));
            $("#green").text(Math.round(rgb[1]));
            $("#blue").text(Math.round(rgb[2]));
            
            rgbWritten = "rgba(" + Math.round(rgb[0]) + "," + Math.round(rgb[1]) + "," + Math.round(rgb[2]) + "," + "0.8)";
            $(".light").css("background-color",rgbWritten);
            $(".light").css("box-shadow","0 0 60px 40px " + rgbWritten);
            
            //var x = xUrsprung - e.pageX;
            //var y = yUrsprung - e.pageY;
            var x = e.pageX - offset.left - 250;
            var y = offset.top + 250 - e.pageY;
            //var s = Math.sqrt((offset.left +200 - x) * (offset.left +200 - x) - (offset.top + 200 - y) * (offset.top + 200 - y)); //Entfernung der zwei punkte 
            //var s = Math.sqrt(x * x + y * y);
            var alpha = Math.atan(y / x);
            if(alpha < 0)
            {
                alpha = alpha * -1;
            }
            var newX = Math.cos(alpha) * 204;
            if(x < 0 && newX >= 0 || x >= 0 && newX < 0)
            {
                newX = newX * -1;
            }
            var newY = Math.sin(alpha) * 204;
            if(y < 0 && newY >= 0 || y >= 0 && newY < 0)
            {
                newY = newY * -1;
            }

        $("#rgbCursor").css("left", offset.left + 250 + newX - 10); //weil der ursprung des cursors nicht in der mitte liegt stimmt pagex/y nicht ganz
        $("#rgbCursor").css("top",offset.top + 250 - newY - 10);
        $("#rgbCursor").css("display", "block");
        }
        $("#pageX").text(e.pageX);
        $("#pageY").text(e.pageY);
        $("#offX").text(offset.left);
        $("#offY").text(offset.top);
        
        
    });
    
    //Make the DIV element draggagle:
//dragElement(document.getElementById(("rgbCursor")));

    
    
    
    
    /*
function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id)) {
    //if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id).onmousedown = dragMouseDown;
  } else {
    //otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    var offset = $("canvas").offset();
      
    var x = elmnt.offsetLeft - pos1 - offset.left - 250;
    var y = offset.top + 250 - elmnt.offsetTop - pos2;
            
    var alpha = Math.atan(y / x);
    if(alpha < 0)
    {
        alpha = alpha * -1;
    }
    var newX = Math.cos(alpha) * 204;
    if(x < 0 && newX >= 0 || x >= 0 && newX < 0)
    {
        newX = newX * -1;
    }
    var newY = Math.sin(alpha) * 204;
    if(y < 0 && newY >= 0 || y >= 0 && newY < 0)
    {
        newY = newY * -1;
    }

    $("#rgbCursor").css("left", offset.left + 250 + newX - 10); //weil der ursprung des cursors nicht in der mitte liegt stimmt pagex/y nicht ganz
    $("#rgbCursor").css("top",offset.top + 250 - newY - 10);
      
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    //stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
} */





    
    
    //$("#rgbCursor").mousedown(function(e){
        //var offset = $("#canvas").offset(); //offset relativ zur seite als variable holen
        //var pixelColor = ctx.getImageData(e.pageX - offset.left, e.pageY - offset.top, 1, 1).data;  //weil ursprung von seite und canvas unterschedlich, wird das jeweilige offset von den seiten koordinaten abgezogen und an diesen koordinaten werden die pixeldaten gespeichert
        
        //$("#pageX").text(e.pageX);
        //$("#pageY").text(e.pageY);
    //});
    
    
    $("#toFunctionBar").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();

      var hash = this.hash;

      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        window.location.hash = hash;
      });
    }
  });
};

function singleColorBlinkChange()
{
    var speed = document.getElementById("singleColorBlinkInput").value;
    var speed = speed.replace(",", ".");
    var speed = speed * 2;

    document.styleSheets[0].addRule(".blink", "-webkit-animation: blink " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".blink", "-moz-animation: blink " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".blink", "-ms-animation: blink " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".blink", "animation: blink " + speed + "s linear infinite");
}

function singleColorBreatheChange()
{
    var speed = document.getElementById("singleColorBreatheInput").value;
    var speed = speed.replace(",", ".");

    document.styleSheets[0].addRule(".breathe", "-webkit-animation: breathe " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".breathe", "-moz-animation: breathe " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".breathe", "-ms-animation: breathe " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".breathe", "animation: breathe " + speed + "s linear infinite");
}

function singleColorFlashChange()
{
    var speed = document.getElementById("singleColorFlashInput").value;
    var speed = speed.replace(",", ".");
    var speed = speed * 2;

    document.styleSheets[0].addRule(".flash", "-webkit-animation: flash " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".flash", "-moz-animation: flash " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".flash", "-ms-animation: flash " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".flash", "animation: flash " + speed + "s linear infinite");
}

function rgbFadeChangeSlow()
{
    var speed = 10;
    
    document.styleSheets[0].addRule(".rgbFade", "-webkit-animation: rgbFade " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".rgbFade", "-moz-animation: rgbFade " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".rgbFade", "-ms-animation: rgbFade " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".rgbFade", "animation: rgbFade " + speed + "s linear infinite");
}
function rgbFadeChangeFast()
{
    var speed = 1;
    
    document.styleSheets[0].addRule(".rgbFade", "-webkit-animation: rgbFade " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".rgbFade", "-moz-animation: rgbFade " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".rgbFade", "-ms-animation: rgbFade " + speed + "s linear infinite");
    document.styleSheets[0].addRule(".rgbFade", "animation: rgbFade " + speed + "s linear infinite");
}






/*
function getpostArray(rgb, mode, intervall)
{
    var hex1 = rgb[0].toString(16);
    var hex2 = rgb[1].toString(16);
    var hex3 = rgb[2].toString(16);
    
    var hex = hex1 + hex2 + hex3;
    
    
    if(intervall != null)
    {
        var postArray = [];
        postArray['mode'] = mode;
        postArray['hex'] = hex;
        postArray['intervall'] = intervall;
        
        var jsonStuff = [
	        { "make":"hex", "model":hex },
            { "make":"mode", "model":mode },
            { "make":"intervall","model": intervall}
        ];
        
    }
    else
    {
        var postArray = [];
        postArray['mode'] = mode;
        postArray['hex'] = hex;
        postArray['intervall'] = null;
        
        var jsonStuff = [
	       { "make":"hex", "model":hex },
           { "make":"mode", "model":mode }
        ];
        
    }
    
    return postArray;
}
*/




function toHex(rgb)
{
    var hex1 = rgb[0].toString(16);
    var hex2 = rgb[1].toString(16);
    var hex3 = rgb[2].toString(16);
    
    var hex = hex1 + hex2 + hex3;
    
    return hex;
}






function noEffect()
{
    var mode = "noEffect";
	var hex = toHex(finalColor);
    var time = document.getElementsByName("rgbFadeInput").value;
    
    var data = mode + "." + hex + "." + time + "." + currentMode;
    
    $.ajax({
        url: 'toPython.php',
        data: 'data='+data,
        success: function() {
            alert("It might works...");
        }
    });
}

function singleColorBlink()
{
	$.post("192.168.8.2/home/pi/controller.py", getJsonStuff(finalColor, "singleColorBlink", document.getElementById("singleColorBlinkInput").value.replace(",", ".")), function()
    {
        alert("It might works.");
    });
    event.preventDefault();
}

function singleColorBreathe()
{
	$.post("192.168.8.2/home/pi/controller.py", getJsonStuff(finalColor, "singleColorBreathe", document.getElementById("singleColorBreatheInput").value.replace(",", ".")), function()
    {
        alert("It might works.");
    });
    event.preventDefault();
}

function singleColorFlash()
{
	$.post("192.168.8.2/home/pi/controller.py", getJsonStuff(finalColor, "singleColorFlash", document.getElementById("singleColorFlashInput").value.replace(",", ".")), function()
    {
        alert("It might works.");
    });
    event.preventDefault();
}

function rgbFade()
{
    var mode = "rgbFade";
	//var hex = toHex(finalColor);
    var radios = document.getElementsByName('rgbFadeInput');

    for (var i = 0, length = radios.length; i < length; i++)
    {
        if (radios[i].checked)
        {
            // do whatever you want with the checked radio
            var time = radios[i].value;

            // only one radio can be logically checked, don't check the rest
            break;
        }
    }
    //var time = document.getElementsByName("rgbFadeInput").value;
    
    //var data = mode + "." + hex + "." + time + "." + currentMode;
    
    $.ajax({
        url: '/var/www/html/toPython.php',
        //data: 'data='+data,
        data: {mode: mode,currentMode: currentMode,time: time},
        success: function() {
            alert("It might work...");
        }
    });
    currentMode = mode;
}










function turnOff()
{
    $.ajax({
        url: 'toPython.php',
        data: 'turnOff='+currentMode,
        success: function() {
            alert("It might work...");
        }
    });
    currentMode = 'none';
}