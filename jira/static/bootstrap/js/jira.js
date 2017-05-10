function checkform() { 
	var form = document.getElementById("form");
	for (i=0;i<form.length;i++){
		var ele = form.elements[i];
		var msg = ele.getAttribute('message');
		if(msg && ele.value == ""){
			document.getElementById(msg).classList.add("has-error");
			ele.placeholder="请输入内容";
			ele.focus(); 
			return false; 
		}
	}
	form.submit();
}

// function changeFrameHeight(){
//     var ifm= document.getElementById("myiframe"); 
//     ifm.height=document.documentElement.clientHeight;
// }
// window.onresize=function(){  
//      changeFrameHeight();  
// } 
function login(){
   var result = document.getElementById("username").value;
   var password = document.getElementById("password").value;
   if(result == ""  ){
     document.getElementById("sign").classList.add("has-error");
     return false;
   }
   if(password == ""  ){
    document.getElementById("pwd").classList.add("has-error");
     return false;
   }
  document.getElementById("loginsub").submit();
}

// window.onload = function () {
// 	var obj = document.getElementById('#assignee');
// 	var timer = null;
// 	obj.onkeyup = function() {
// 		search(); 
// 	}
// 	var search = function() {
// 		if (timer == null) { //先判断一下定时器是空才可以进行新的搜索
// 			timer = setTimeout(function() {
// 				val.innerHTML = val.innerHTML  + '<br>' + '1.开始搜索' + obj.value;
// 			}, 700);
// 		} else {
// 			//如果定时器是开启的，说明上一次搜索没有结束，不可以进行下一次搜索，清空定时器
// 			clearTimeout(timer);
// 			//重启定时器
// 			timer = setTimeout(function() {
// 				val.innerHTML = val.innerHTML  + '<br>' + '开始搜索: ' + obj.value;
// 			}, 700);
// 		}
		
// 	}
	
// }
	