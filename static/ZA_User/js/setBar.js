function setSrollBar() {
    var barHeight = $("body").height() / $("body")[0].scrollHeight;
    if (barHeight >= 1) {
        $("#scrollBar").css("display", "none")
    } else {
        $("#scrollBar").css("display", "block");
        $("#scrollBar").css("height", barHeight * 100 + "%");
        $("body").on("scroll", function () {
            $("#scrollBar").css("top", (barHeight * $("body").scrollTop()) + "px")
        });
        $("#scrollBar").on("mousedown", function (e) {
            e.stopPropagation();
            var start = e.pageY;
            var orginPostion = $("#scrollBar").css("top");
            $(document).mousemove(function (event) {
                var end = event.pageY;
                var move = end - start;
                var currPostion = parseFloat(orginPostion) + (end - start);
                if (currPostion <= 0) {
                    $("#scrollBar").css("top", "0px")
                } else {
                    if (currPostion + parseFloat($("#scrollBar").css("height")) >= parseFloat($("#warp").css("height"))) {
                        $("#scrollBar").css("top", (parseFloat($("#warp").css("height")) - parseFloat($("#scrollBar").css("height"))) + "px")
                    } else {
                        $("#scrollBar").css("top", currPostion + "px");
                        $("body").scrollTop(currPostion / barHeight)
                    }
                }
            });
            $(document).mouseup(function (event) {
                $(document).off("mousemove")
            })
        })
    }
};