var canvas = document.getElementById("canvas");
var canvasRect = canvas.getClientRects()[0];
var ctx = canvas.getContext("2d")

var mouse = {
    startX: 0,
    startY: 0,
    x: 0,
    y: 0,
    color: "black",
    isDrawing: false
};

canvas.addEventListener("mousemove", function(e){
    var rect = e.target.getBoundingClientRect();
    mouse.x = e.pageX - canvasRect.x;
    mouse.y = e.pageY - canvasRect.y;

    if(mouse.isDrawing){
        ctx.beginPath();
        ctx.moveTo(mouse.startX * canvas.width / canvasRect.width, mouse.startY * canvas.height / canvasRect.height);
        ctx.lineTo(mouse.x * canvas.width / canvasRect.width, mouse.y * canvas.height / canvasRect.height);
        ctx.strokeStyle = mouse.color;
        ctx.stroke();
        mouse.startX = mouse.x;
        mouse.startY = mouse.y;
    }
})

canvas.addEventListener("mousedown", function (e) {
    mouse.isDrawing = true;
    mouse.startX = mouse.x;
    mouse.startY = mouse.y;
});
canvas.addEventListener("mouseup", function (e) {
    mouse.isDrawing = false;
});
canvas.addEventListener('mouseleave', function (e) {
    mouse.isDrawing = false;
});

function convert(){

}