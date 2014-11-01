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
    var t = new Array();
    oBtn.click(function(ev) {
        // alert(String(3*(2+1))+"rem");
        var ev = ev || window.event;
        if (bBtn && !oBtn.hasClass("active")) {
            oBtn.addClass("active");
            for (var i = 0; i < oIcon.length; i++) {
                (function(e){
                    oIcon[e].stop();
                    t[e] = setTimeout(function(){
                        oIcon[e].animate({bottom:String(3*(e+1)+.5)+'rem'}, (1+e)*200,
                            function(){oIcon[e].animate({bottom:String(3*(e+1))+'rem'}, 150, 
                                function(){oIcon[e].children("span.text").animate({
                                    width:"80px", paddingRight:"16px"}, 300);
                            })}
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
                clearTimeout(t[i]);
                oIcon[i].children("span.text").stop().animate({width:"0", paddingRight:"0"}, 300);
                oIcon[i].stop().animate({bottom:"0rem"}, 300);
            }
            $("#background").stop().animate({opacity:"0"}, 300, function(){$("#background").remove();});
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
                clearTimeout(t[i]);
                oIcon[i].children("span.text").stop().animate({width:"0", paddingRight:"0"}, 300);
                oIcon[i].stop().animate({bottom:"0rem"}, 300);
            } 
            $("#background").stop().animate({opacity:"0"}, 300, function(){$("#background").remove();});
            bBtn = !bBtn;
        }
    });
    document.querySelector("div.control").onclick=function(ev){
        var ev =  ev || window.event;
        ev.cancelBubble = true;
    }


}("#control-button");

var favour_detail = function(id) {
    var oEdt = $(id);
    var bHul = true;
    var oUl = $("ul.favour");
    oEdt.click(function(ev) {
        // alert(String(3*(2+1))+"rem");
        var ev = ev || window.event;
        if (bHul && !oEdt.hasClass("active")) {
            oEdt.addClass("active");
            oUl.stop().slideDown();
            $("body").append("<div id='background' style='position:fixed;top:0;left:0;opacity:0;width:100%;height:100%;background-color:rgba(255,255,255,.6);z-index:400'>")
            $("#background").animate({opacity:"1"}, 500);
            $("a#edit").stop().css({display:"block"});
            $("a#logo").stop().animate({opacity:"0"},250,function(){$(this).css({display:"none"})});
            $("a#edit").animate({opacity:"1"},250);
        } else if (!bHul && oEdt.hasClass("active")) {
            oEdt.removeClass("active");
            oUl.stop().slideUp();

            $("#background").animate({opacity:"0"}, 300, function(){$("#background").remove();});
            $("a#logo").stop().css({display:"block"});
            $("a#edit").stop().animate({opacity:"0"},250,function(){$(this).css({display:"none"})});
            $("a#logo").animate({opacity:"1"},250);
            // setTimeout(function(){$("#background").remove();},500);
        }
        bHul = !bHul;
        ev.cancelBubble = true;
        ev.preventDefault();
    });
    $("body").click(function() {
        if (bHul == false) {
            oEdt.removeClass("active");
            oUl.stop().slideUp();
            $("#background").animate({opacity:"0"}, 300, function(){$("#background").remove();});
            $("a#logo").stop().css({display:"block"});
            $("a#edit").stop().animate({opacity:"0"},250,function(){$(this).css({display:"none"})});
            $("a#logo").animate({opacity:"1"},250);
            bHul = !bHul;
        }
    });
    document.querySelector("header").onclick=function(ev){
        var ev =  ev || window.event;
        ev.cancelBubble = true;
    }

    var bEdt = true;

    $("a#edit").click(function(ev){
        // alert(String(3*(2+1))+"rem");
        var ev = ev || window.event;
        if (bEdt && !oUl.hasClass("active")) {
            oUl.addClass("active");
            $(this).stop().animate({opacity:"0"},250, function(){
                $(this).text("取消")
                    .animate({opacity:"1"},250);
            });
        } else if (!bEdt && oUl.hasClass("active")) {
            oUl.removeClass("active");
            $(this).stop().animate({opacity:"0"},250, function(){
                $(this).text("编辑")
                    .animate({opacity:"1"},250);
            });
        }
        bEdt = !bEdt;
        ev.preventDefault();
    });
    $("a.delete").click(function(ev){
        var oLi = $(this).parent();
        oLi.slideUp(300, function(){
            oLi.remove();
        });
        ev.preventDefault();
    });

}("#favour-detail");



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