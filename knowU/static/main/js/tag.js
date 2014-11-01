
var artag = $("#tag_choosing").children("div");
var tag = new Array();
for (var i = 0; i < artag.length; i++) {
    tag[i] = $("#" + artag[i]['id']);
};

$(document).ready(function(){
    tag_ready(tag, 500, 200);

    $("div.tag-choosing").children("div").click(function(){
        var oa = $(this).children("a");
        if (oa.hasClass("chosen")) {
            oa.removeClass("chosen");
            //delete
        } else {
            oa.addClass("chosen");
        }
    })
});

var tag_detail = function(id) {
    var oBtn = $(id);
    var bBtn = true;
    var oUl = $("ul.chosen");
    oBtn.click(function(ev) {
        // alert(String(3*(2+1))+"rem");
        var ev = ev || window.event;
        if (bBtn && !oBtn.hasClass("active")) {
            oBtn.addClass("active");
            oUl.stop().slideDown();
            $("body").append("<div id='background' style='position:fixed;top:0;left:0;opacity:0;width:100%;height:100%;background-color:rgba(255,255,255,.6);z-index:400'>")
            $("#background").animate({opacity:"1"}, 500);
            $("a#edit").stop().css({display:"block"});
            $("a#logo").stop().animate({opacity:"0"},250,function(){$(this).css({display:"none"})});
            $("a#edit").animate({opacity:"1"},250);
        } else if (!bBtn && oBtn.hasClass("active")) {
            oBtn.removeClass("active");
            oUl.stop().slideUp();

            $("#background").animate({opacity:"0"}, 300, function(){$("#background").remove();});
            $("a#logo").stop().css({display:"block"});
            $("a#edit").stop().animate({opacity:"0"},250,function(){$(this).css({display:"none"})});
            $("a#logo").animate({opacity:"1"},250);
            // setTimeout(function(){$("#background").remove();},500);
        }
        bBtn = !bBtn;
        ev.cancelBubble = true;
        ev.preventDefault();
    });
    $("body").click(function() {
        if (bBtn == false) {
            oBtn.removeClass("active");
            oUl.stop().slideUp();
            $("#background").animate({opacity:"0"}, 300, function(){$("#background").remove();});
            $("a#logo").stop().css({display:"block"});
            $("a#edit").stop().animate({opacity:"0"},250,function(){$(this).css({display:"none"})});
            $("a#logo").animate({opacity:"1"},250);
            bBtn = !bBtn;
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

}("#tag-detail");


/*
    $("div.tag-choosing").children("div").click(function(){
        var id_chosen = $(this).attr("id");
        // alert(id_chosen);
        var flg = 0;
        for (var i = 0; i < 3; i++) {
            if ( id_chosen == (tag[i].attr("id")) ) {
                tag_chosen(tag[i]);
            } else {
                tag_out(tag[i], 500, 200*flg++ + 200);
            }
        }

        setTimeout(function(){reset_all(tag)}, 1500);
    });
*/
function reset_all(tag) {
    for (var i = 0; i < tag.length; i++) {
        reset_tag(tag[i]);
    };
    tag_ready(tag, 500, 200);
}

function reset_tag(obj) {
    obj.animate({"left":"100%","margin-left":"1rem","margin-right":"0","opacity":"1"}, 0);
    obj.children("a").removeClass("chosen");
}

function tag_ready(tag, during, delay) {
    for (var i = 0; i < tag.length; i++) {
        tag_in(tag[i], during, i*delay);
    };
}


 /**
  * 标签进入动画
  * @param  {[type]} obj   [对象]
  * @param  {[type]} during  [所需时间]
  * @param  {[type]} delay [延迟]
  * @return {[type]}       
  */
function tag_in(obj, during, delay) { 
	var $tag = obj;
	// var offset = $panel.offset()-$panel.width();
	// var x= offset.left;
	// var y= offset.top;
    setTimeout(function(){
        $tag.animate({left:"0",marginLeft:"-.5rem"}, during, function(){
            $tag.animate({marginLeft:"0"},100);})
    }, delay);
	// $panel.animate({left:0},fx);
	// $panel.offset({ top: y, left: x });
}

 /**
  * 标签退出动画
  * @param  {[type]} obj   [标签]
  * @param  {[type]} during  [所需时间]
  * @param  {[type]} delay [延迟]
  * @return {[type]}       
  */
function tag_out(obj, during, delay) {
    var $tag = obj;
    setTimeout(function(){
        $tag.animate({left:"-100%",marginRight:"1rem"},during);
        }, delay);
}
