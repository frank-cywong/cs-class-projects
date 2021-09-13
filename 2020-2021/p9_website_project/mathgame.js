function randInt(max) {
	return Math.floor(Math.random() * (max + 1));
}
function generateQuestion() { 
	/* Question Types:
	0: a + b + c
	1: a + b - c
	2: a - b + c 
	3: a - (b + c)
	4: a - b - c
	5: a - (b - c)
	6: a + b * c
	7: a - b * c
	8: a * b + c 
	9: a * b - c
	10: (a + b) * c
	11: (a - b) * c
	12: a * (b + c) 
	13: a * (b - c)  
	14: a + b / c 
	15: a - b / c
	16: a / b + c 
	17: a / b - c
	18: (a + b) / c 
	19: (a - b) / c
	20: a / (b + c) 
	21: a / (b - c)
	22: a * b / c
	23: a / b * c
	*/
	var a,b,c,ans,temp,temp2;
	const digit2 = 99;
	const digit1 = 9;
	const h_digit2 = 49;
	var type = randInt(23);
	var ldarray = [1,1,1,2,2,3,4,5,6,7];
	switch (type) {
		case 0: // yes this code is a mess
			a = randInt(digit2);
			b = randInt(digit2);
			c = randInt(digit2);
			ans = a + b + c;
			break
		case 1:
			a = randInt(digit2);
			b = randInt(digit2);
			c = randInt(digit2);
			ans = a + b - c;
			break
		case 2:
			a = randInt(digit2);
			b = randInt(digit2);
			c = randInt(digit2);
			ans = a - b + c;
			break
		case 3:
			a = randInt(digit2);
			b = randInt(digit2);
			c = randInt(digit2);
			ans = a - (b + c);
			break
		case 4:
			a = randInt(digit2);
			b = randInt(digit2);
			c = randInt(digit2);
			ans = a - b - c;
			break
		case 5:
			a = randInt(digit2);
			b = randInt(digit2);
			c = randInt(digit2);
			ans = a - (b - c);
			break
		case 6:
			a = randInt(digit2);
			b = randInt(digit1);
			c = randInt(digit1);
			ans = a + b * c;
			break
		case 7:
			a = randInt(digit2);
			b = randInt(digit1);
			c = randInt(digit1);
			ans = a - b * c;
			break
		case 8:
			a = randInt(digit1);
			b = randInt(digit1);
			c = randInt(digit2);
			ans = a * b + c;
			break
		case 9:
			a = randInt(digit1);
			b = randInt(digit1);
			c = randInt(digit2);
			ans = a * b - c;
			break
		case 10:
			a = randInt(h_digit2);
			b = randInt(h_digit2);
			c = randInt(digit1);
			ans = (a + b) * c;
			break
		case 11:
			a = randInt(h_digit2);
			b = randInt(h_digit2);
			c = randInt(digit1);
			ans = (a - b) * c;
			break
		case 12:
			a = randInt(digit1);
			b = randInt(h_digit2);
			c = randInt(h_digit2);
			ans = a * (b + c);
			break
		case 13:
			a = randInt(digit1);
			b = randInt(h_digit2);
			c = randInt(h_digit2);
			ans = a * (b - c);
			break
		case 14:
			a = randInt(digit2);
			c = (randInt(digit1) + 1);
			b = c * randInt(digit2);
			ans = a + b / c;
			break
		case 15:
			a = randInt(digit2);
			c = (randInt(digit1) + 1);
			b = c * randInt(digit2);
			ans = a - b / c;
			break
		case 16:
			c = randInt(digit2);
			b = (randInt(digit1) + 1);
			a = b * randInt(digit2);
			ans = a / b + c;
			break
		case 17:
			c = randInt(digit2);
			b = (randInt(digit1) + 1);
			a = b * randInt(digit2);
			ans = a / b - c;
			break
		case 18:
			c = (randInt(digit1) + 1);
			temp = c * randInt(digit2);
			b = randInt(temp);
			a = temp - b;
			ans = (a + b) / c;
			break
		case 19:
			c = (randInt(digit1) + 1);
			a = randInt((c * digit2));
			b = a - (c * randInt(Math.floor(a / c)));
			ans = (a - b) / c;
			break
		case 20:
			b = randInt(digit1);
			c = (randInt(digit1) + 1);
			a = (b + c) * randInt(h_digit2);
			ans = a / (b + c);
			break
		case 21:
			temp = (randInt(digit1) + 1);
			c = (randInt(digit1) + 1);
			b = temp + c;
			a = temp * randInt(h_digit2);
			ans = a / (b - c);
			break
		case 22:
			temp = ldarray[randInt(9)];
			a = temp * randInt(digit1);
			temp2 = (randInt(digit1) + 1);
			b = temp2 * randInt(Math.floor(digit1 * 3 / temp2));
			c = temp * temp2;
			ans = a * b / c;
			break
		case 23:
			temp = ldarray[randInt(9)];
			c = temp * randInt(digit1);
			temp2 = (randInt(digit1) + 1);
			a = temp2 * randInt(Math.floor(digit1 * 3 / temp2));
			b = temp * temp2;
			ans = a * c / b;
			break
	}
	ans = Math.round(ans); // just in case of floating point
	return [a, b, c, ans, type];
}
function generateDisplayText(a, b, c, type) {
	var typearray = ["a + b + c", "a + b - c", "a - b + c",  "a - (b + c)", "a - b - c", "a - (b - c)", "a + b * c", "a - b * c", "a * b + c",  "a * b - c", "(a + b) * c", "(a - b) * c", "a * (b + c)",  "a * (b - c)",   "a + b / c",  "a - b / c", "a / b + c", "a / b - c", "(a + b) / c", "(a - b) / c", "a / (b + c)",  "a / (b - c)", "a * b / c", "a / b * c"];
	var typestring = typearray[type];
	typestring = typestring.replace("a",a.toString())
	typestring = typestring.replace("b",b.toString())
	typestring = typestring.replace("c",c.toString())
	return typestring
}
function newQuestion() {
	var questiondata = generateQuestion();
	var displaystring = generateDisplayText(questiondata[0],questiondata[1],questiondata[2],questiondata[4]);
	answer = questiondata[3];
	var question = document.getElementById("equation");
	question.innerHTML = displaystring;
	var answerelement = document.getElementById("answer");
	answerelement.value = "";
}
function handleTimer(mode) { // 0: start game/time, 1: stop game/time
	if (mode) {
		running = false;
		clearInterval(timerInterval);
		var question = document.getElementById("equation");
		var restartbutton = document.getElementById("restart");
		restartbutton.disabled = true;
		var startbutton = document.getElementById("startbutton");
		startbutton.disabled = false;
		question.innerHTML = "Time is Up.";
		checkHighScore();
	} else {
		running = true;
		timeleft = 90;
		var restartbutton = document.getElementById("restart");
		restartbutton.disabled = false;
		var startbutton = document.getElementById("startbutton");
		startbutton.disabled = true;
		adjustScore(0);
		var timeleftelement = document.getElementById("timeleft");
		newQuestion();
		timeleftelement.innerHTML = "Time left (s): " + (timeleft.toString());
		timerInterval = setInterval(timer, 1000);
	}
}
function timer() {
	timeleft -= 1;
	var timeleftelement = document.getElementById("timeleft");
	timeleftelement.innerHTML = "Time left (s): " + (timeleft.toString());
	if (timeleft == 0) {
		handleTimer(1);
	}
}
function adjustScore(mode) { // 0: set to 0, 1: increment by 1
	var scoreelement = document.getElementById("score");
	if (mode) {
		var score = parseInt((scoreelement.innerHTML.split(' '))[1], 10);
		score += 1;
		scoreelement.innerHTML = "Score: " + (score.toString());
	} else {
		scoreelement.innerHTML = "Score: 0";
	}
}
function checkHighScore() {
	var scoreelement = document.getElementById("score");
	var score = parseInt((scoreelement.innerHTML.split(' '))[1], 10);
	var highscoreelement = document.getElementById("highscore");
	var highscore = parseInt((highscoreelement.innerHTML.split(' '))[1], 10);
	if (score > highscore) {
		highscoreelement.innerHTML = "Highscore: " + (score.toString());
	}
}
function onAnswer() {
	var answerelement = document.getElementById("answer");
	var playeranswer = answerelement.value;
	if (playeranswer.toString() === answer.toString()) {
		adjustScore(1);
	} 
	newQuestion();
}
function init() {
	var timerInterval, running, timeleft, answer;
	running = false;
	var restartbutton = document.getElementById("restart");
	var startbutton = document.getElementById("startbutton");
	var answerelement = document.getElementById("answer");
	restartbutton.addEventListener("click", function() {handleTimer(1);});
	startbutton.addEventListener("click", function() {handleTimer(0);});
	answerelement.addEventListener("keyup", function(e) {
		if (e.keyCode == 13) {
			onAnswer();
		}
	});
	console.log("test");
}
window.onload = init;