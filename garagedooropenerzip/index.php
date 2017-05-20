<?php 
	if(isset($_GET['trigger']) && $_GET['trigger'] == 1) {
		error_reporting(E_ALL);
		exec('gpio write 7 0');
		sleep(1);
		exec('gpio write 7 1');
	}
<!DOCTYPE html>
<html>
	<head>
		<title>Garage Opener</title>
		<link rel="apple-touch-icon" href="apple-touch-icon-iphone.png" />
		<link rel="apple-touch-icon" sizes="72x72" href="apple-touch-icon-ipad.png" />
		<link rel="apple-touch-icon" sizes="114x114" href="apple-touch-icon-iphone-retina-display.png" />
		<link rel="stylesheet" href="/css/style.css" type="text/css">
		<meta name="apple-mobile-web-app-capable" content="yes">  
	</head>
	<body>
		<form id="__f" action="POST" method="/garage/door/toggle">
			<input type="hidden" value="$_POST['state']" name="state" />
			<input type="submit" id="triggerBtn" />
		</form>
		
		
		<script>
			(function (doc) {
				const TRIGGER_BTN_ID = "#triggerBtn";
				const FORM_ELEMENT = doc.querySelector("#__f");
				
				doc.querySelector(TRIGGER_BTN_ID).onclick = event => makeRequest(event);
				
				function makeRequest (e) {
					e.preventDefault();
					
					const xhr = new XMLHttpRequest();
					xhr.open("POST", "/garage/door/toggle", true);
					xhr.onload = console.info;
					xhr.onerror = console.error;
					xhr.send(new FormData(FORM_ELEMENT));
				}
			})(document);
		</script>
	</body>
</html>

?>