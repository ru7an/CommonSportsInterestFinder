var add_emo = "";
for (var i = 128512; i < 128592; i++) {
add_emo += '<button onclick="pick_emoji('+i+')" id="'+i+'">&#'+i+'; </button>';
}
document.getElementById("emobox").innerHTML = add_emo;

var xx = document.getElementById('msg-here-text');
function pick_emoji(em_num)
{	var num = em_num.toString();
    num = num.replace(' ','');
    var x = document.getElementById(num);
    xx.value += x.innerHTML;
}
function smileyshow()
{
    document.getElementById("emobox").classList.toggle('show_emoji');
}
if(localStorage.getItem('theme')=='light')
{
  document.getElementById('msg-here-text').style.color='black';
  document.getElementById('emobox').style.backgroundColor='white';
}
