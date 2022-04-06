var img = new Image();
var k = 3;
// img.src = "./images/05.jpg";
function submitK() {
    var x = document.getElementById("kvalue").value;
    // console.log(x);
    if (isNaN(x) || x < 2) {
        alert('重新输入');
    } else {
        k = x;
        document.getElementById("kvalue").disabled = "disabled";
        $("#showlater").show();
        $("#sbK").fadeOut();
    }
}

$("#img_change").click(function () {
    $("#file").click();
})

/*$("#file").change(function (event) {*/
var filechange=function(event){
    var files = event.target.files, file;
    if (files && files.length > 0) {
        // 获取目前上传的文件
        file = files[0];// 文件大小校验的动作
        if(file.size > 1024 * 1024 * 2) {
            alert('图片大小不能超过 2MB!');
            return false;
        }
        if (file.height > 600 || file.width > 800) {
            alert('图片像素不超过800*600!');
            return false;
        }
        // 获取 window 的 URL 工具
        var URL = window.URL || window.webkitURL;
        // 通过 file 生成目标 url

        img.src = URL.createObjectURL(file);
        //用attr将img的src属性改成获得的url

        document.getElementById('upload').style.display = 'none'
        $("#loading").show();
    }
};

var kPoint = [];
var kPoint_pre = [];

var kColorString = [];

var kCNT = [];
var kDisSum = [];

var KclassLoc = [];

var canvas = document.getElementById("myCanvas")
var context = canvas.getContext("2d");
var repeat = 0;
var optseq = 0;
var pieOption;
var barOption;
var scatterOption;
img.onload = function () {
    setInterval(function(){ 
        $("#loading").fadeOut(); 
    });
    // document.getElementById("change_style").visibilty = "visible";
    $("#change_style").show();
    context.drawImage(img, 0, 0, img.width, img.height);
    resize(img.width, img.height);

    init();
    while (!stop(kPoint, kPoint_pre, 7)) {

        copy(kPoint_pre, kPoint);

        clear();

        kMeans(img.width, img.height, context);

        transKPoint();

        for (var i = 0; i < k; i++) {
            console.log(kPoint[i]);
        }
    }

    clearZero();

    console.log("kMeans Finish");

    var stepX = parseInt(img.width / 66);
    var stepY = parseInt(img.height / 50);
    for (var i = 0; i < img.width; i += stepX) {
        for (var j = 0; j < img.height; j += stepY) {
            classifyIntoCorrCate(i, img.height - j, context.getImageData(i, j, 1, 1).data);
        }
    }

    for (var i = 0; i < k; i++) {
        kColorString[i] = transKColorString(kPoint[i]);
        console.log(kColorString[i]);
    }
  
    var myChart = echarts.init(document.getElementById("container"));
    var app = {};

    var option;
    console.log(KclassLoc);

    var piedata = [];
    for (var i = 0; i < k; i++) {
        piedata.push({ value: kCNT[i] , name: kColorString[i]});
    }
    pieOption = {
            tooltip: {
                trigger: 'item'
            },
            legend: {
                top: '5%',
                left: 'center'
            },
            series: [{
                name: kColorString,
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 20,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '40',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: piedata,
                itemStyle: {
                    normal: {
                        color: function(params) {
                            return kColorString[params.dataIndex]
                        },
                    }
                },
            }
        ]
    };

    barOption = {
        xAxis: {
            type: 'category',
            data: kColorString,
        },
        yAxis: {},
        tooltip: {
            trigger: 'axis'
        },
        series: [
            {
                type: 'bar',
                data: kCNT,
                label: {
                    normal: {
                        show: true,
                        position: 'top',
                        textStyle: {
                            color: 'black',
                            fontSize: 26,
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        color: function(params) {
                            return kColorString[params.dataIndex]
                        },
                    }
                },
            }
        ],
    };

    var scatterSeries = [];
    for (var i = 0; i < k; i++){
        scatterSeries.push({
            symbolSize: 10,
            data: KclassLoc[i],
            type: 'scatter',
        })
    }
    scatterOption = {
        xAxis: {},
        yAxis: {},
        series: scatterSeries,
    }


    let currentOption = barOption;
    myChart.setOption(currentOption, true);

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }
}

function changestyle() {
    var myChart = echarts.init(document.getElementById("container"));

    var option;
    optseq += 1;
    var opt;
    if (optseq % 3 == 0) {
        opt = barOption;
    } else if(optseq % 3 == 1) {
        opt = pieOption;
    } else {
        opt = scatterOption;
    }
    myChart.setOption(opt, true);
    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }
}

function init() {
    for (var i = 0; i < k; i++){
        var r = parseInt(255 * Math.random());
        var g = parseInt(255 * Math.random());
        var b = parseInt(255 * Math.random());
        var initp = [r, g, b];
        kPoint.push(initp);

        console.log(kPoint[i]);

        kPoint_pre.push([0, 0, 0]);
        kCNT.push(0);
        kDisSum.push([0, 0, 0]);

        KclassLoc.push([]);
    }
}

function transKColorString(point) {
    var r = DecToHex(point[0]);
    var g = DecToHex(point[1]);
    var b = DecToHex(point[2]);

    return ('#' + r + g + b);
}

function DecToHex(num) {
    var table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    var gw = table[num % 16];
    var sw = table[parseInt(num / 16)];
    return (sw + gw);
}

function resize(w, h) {
    var nc = document.createElement("canvas");
    nc.width = canvas.width;
    nc.height = canvas.height;
    nc.getContext("2d").drawImage(canvas, 0, 0);
    canvas.width = w;
    canvas.height = h;
    context.drawImage(nc, 0, 0);
}

function copy(kPoint_pre, kPoint) {
    for (var i = 0; i < kPoint.length; i++) {
        for (var j = 0; j < kPoint.length; j++) {
            kPoint_pre[i][j] = kPoint[i][j];
        }
    }
}

function distance(color, tk) {
    // 计算某个像素的RGB三通道到某个质心RGB的距离
    return parseInt(Math.sqrt((color[0] - tk[0]) * (color[0] - tk[0])
                            + (color[1] - tk[1]) * (color[1] - tk[1])
                            + (color[2] - tk[2]) * (color[2] - tk[2])));
}

function classify(color) {
    var cls_index = 0;
    var dis = 10000;
    for (var i = 0; i < k; i++){
        var tt = distance(color, kPoint[i]);
        if (tt < dis) {
            dis = tt;
            cls_index = i;
        }
    }
    kCNT[cls_index] += 1;
    for (var i = 0; i < 3; i++) {
        kDisSum[cls_index][i] += color[i];
    }
}

function kMeans(height, width, context) {
    for (var i = 0; i < height; i++) {
        for (var j = 0; j < width; j++) {
            var color = context.getImageData(i, j, 1, 1).data;
            classify(color, kPoint);
        }
    }
}

function stop(kPoint, kPoint_pre, threshold) {
    // 当变化小于阈值的时候，视为可以离开循环
    var st = 0;
    for (var i = 0; i < k; i++) {
        for (var j = 0; j < 3; j++) {
            st += Math.abs(kPoint[i][j] - kPoint_pre[i][j]);
        }
    }
    console.log("st = " + st);
    return (st < threshold * k);
}

function clearZero() {
    var perfect = true;
    var temp = 0;
    for (var i = 0; i < k; i++){
        if (kCNT[i] == 0) {
            perfect = false;
            temp += 1;
        }
    }

    if (!perfect) {
        alert('本次结果产生' + temp + '个0分类,请重试或降低k数量');
        location.reload();
    }
}

function clear() {
    for (var i = 0; i < k; i++){
        kCNT[i] = 0;
        kDisSum[i] = [0, 0, 0];
    }
}

function transKPoint() {
    // 改变三个质心位置到目前集合的几何中心
    for (var i = 0; i < k; i++) {
        if (kCNT[i] != 0) {
            for (var j = 0; j < 3; j++) {
                kPoint[i][j] = parseInt(kDisSum[i][j] / kCNT[i]);
            }
        }
    }
}

function classifyIntoCorrCate(x, y, color) {
    var dis = 10000;
    var cls_index = 0;
    var tt;
    for (var i = 0; i < k; i++){
        tt = distance(color, kPoint[i]);
        if (tt < dis) {
            dis = tt;
            cls_index = i;
        }
    }
    KclassLoc[cls_index].push([x, y]);
}

function choosePic() {
    alert('请选择图片');
}