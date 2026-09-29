from nltk.chat.util import Chat, reflections
reflections ={
    "i am"  :"you are",
    "i was"  :"you were",
    "i "  :"you ",
    "i 'm"  :"you are",
    "i 'd"  :"you would",
    "i ll"  :"you will",
    "my"  :"your",
    "you are"  :"i am",
    "you were"  :"i was",
    "you ve"  :"i have",
    "youll"  :"ill",
    "yours"  :"my",
    "yours "  :"mine",
    "you"  :"me",
    "me"  :"you "
}
pairs=[
[r"my name is (.*)",["Hello %1, How are you today ?",]],
[r"hi|hey|hello",["Hello","Hey there",]],
[r"what is your name ?",["I am a bot created by Codingal Edu. pvt. Lim. you can call me Jarvis!",]],
[r"how are you ?",["I'm doing goodHow about You ?",]],
[r"sorry (.*)",["Its alright","Its OK, never mind",]]
[r"I am fine",["Great to hear that, How can I help you?",]],
[r"i'm (.*) doing good",["Nice to hear that","How can I help you?"],],
[r"(.*) age?",["I'm a computer program dude,Seriously you are asking me this?",]],
[r"what (.*) want ?",["Make me an offer I can't refuse",]],
[r"(.*) created ?",["Pratham created me using Python's NLTK library ","top secret"]],
[r"(.*)(location|city) ?",["Sahadara, Delhi NCR",]],
[r"how is weather in (.*)?",["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]],
[r"i work in (.*)?",["%1 is an Amazing company, I have heard about it. But they are in huge loss these days."]],
[r"(.*)raining in (.*)",["No rain since last week here in %2","Damn its raining too much"]],
[r"how (.*) health(.*)",["I'm a computer program, so I'm always healthy ",]],
[r"(.*) (sports|game) ?",["I'm a very big fan of Football and Cricket",]],
[r"who (.*) sportsperson ?",["Messy","Ronaldo","Roony","Vivat","M.S. Dhoni","Rohit"]],
[r"who (.*) movie|star|actor)?",["Benedict Cumberbatch"]],
]