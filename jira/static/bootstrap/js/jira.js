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

function changeFrameHeight(){
    var ifm= document.getElementById("myiframe"); 
    ifm.height=document.documentElement.clientHeight;
}
window.onresize=function(){  
     changeFrameHeight();  
} 