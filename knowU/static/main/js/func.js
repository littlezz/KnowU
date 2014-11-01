var oIcon = new Array();
oIcon[0] = $("a#like");
oIcon[1] = $("a#star");
oIcon[2] = $("a#folk");
function show_icon(i) {
    oIcon[i].animate({bottom:String(3*(i+1))+'rem'}, (1+i)*400);
}

/*
$(function(){
    $(window).scroll(function(){
        if ($(window).scrollTop() > 100){
            $("#gotop").css("visibility","visible");
        } else {
            $("#gotop").css("visibility","hidden");
        }
    });
    //当点击跳转链接后，回到页面顶部位置
    $("#gotop").click(function(){
        $('body,html').animate({scrollTop:0},500);
        return false;
    });
}); 
*/  

var list = function(id) {
    var oBtn = $(id);
    var bBtn = true;
    oBtn.click(function(ev) {
        // alert(String(3*(2+1))+"rem");
        var ev = ev || window.event;
        if (bBtn && !oBtn.hasClass("active")) {
            oBtn.addClass("active");
            for (var i = 0; i < oIcon.length; i++) {
                (function(e){
                    setTimeout(function(){
                        oIcon[e].animate(
                            {bottom:String(3*(e+1)+.5)+'rem'}, 
                            (1+e)*200,
                            function(){oIcon[e].animate({bottom:String(3*(e+1))+'rem'}, 150)}
                        );
                    }, (oIcon.length-e-1)*250+100);
                })(i);
                // oIcon[i].animate({bottom:String(3*(i+1))+"rem"}, (i+1)*400);
            }
            $("body").append("<div id='background' style='position:fixed;top:0;left:0;opacity:0;width:100%;height:100%;background-color:rgba(255,255,255,.6);z-index:1000'>")
            $("#background").animate({opacity:"1"}, 500);
        } else if (!bBtn && oBtn.hasClass("active")) {
            oBtn.removeClass("active");
            for (var i = 0; i < oIcon.length; i++) {
                oIcon[i].animate({bottom:"0rem"}, 300);
            }
            $("#background").animate({opacity:"0"}, 300, function(){$("#background").remove();});
            // setTimeout(function(){$("#background").remove();},500);
        }
        bBtn = !bBtn;
        ev.cancelBubble = true;
        ev.preventDefault();
    });
    $("body").click(function() {
        if (bBtn == false) {
            oBtn.removeClass("active");
            for (var i = 0; i < oIcon.length; i++) {
                oIcon[i].animate({bottom:"0rem"}, 300);
            } 
            $("#background").animate({opacity:"0"}, 300, function(){$("#background").remove();});
            bBtn = !bBtn;
        }
    });
    document.querySelector("div.control").onclick=function(ev){
        var ev =  ev || window.event;
        ev.cancelBubble = true;
    }
}("#control-button");


/*
var oinput = document.querySelector("#search-input");
var ohint = document.querySelector("#class-hint");
var obg = document.querySelector("#background");
oinput.onfocus = function() {
    if (oinput.value.replace_with_space().length != 0) {
        ohint.style.visibility = "visible";
        var svalue = oinput.value.replace_with_space();
        obg.style.visibility = "visible";
        load_class_hint(svalue);
    }
}
oinput.onkeyup = function() {
    if (oinput.value.replace_with_space().length != 0) {
        ohint.style.visibility = "visible";
        var svalue = oinput.value.replace_with_space();
        obg.style.visibility = "visible";
        load_class_hint(svalue);
    } else {
        ohint.style.visibility = "hidden";
        obg.style.visibility = "hidden";
    }
};
oinput.onblur = function() {
    ohint.style.visibility = "hidden";
    obg.style.visibility = "hidden";
};
*/