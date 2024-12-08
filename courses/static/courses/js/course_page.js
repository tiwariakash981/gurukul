
var player;
document.onreadystatechange = function (){
    if(document.readyState == 'interactive'){
        player = document.getElementById('player')
        video_list = document.getElementById('video_list')
        maintainRatio()
    }
}

function maintainRatio(){
    var w = player.clientWidth
    var h = (w*9)/16;
    player.height=h;
    video_list.style.maxHeight = h + 'px'
    console.log(video_list)
}

window.onresize = maintainRatio
