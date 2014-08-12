function graphData(input) {
    if (input != "") {

        var window_width = $(window).innerWidth(),
            window_height = $(window).height()

        var color = d3.scale.category20();

        var force = d3.layout.force()
            .charge(-120)
            .linkDistance(200)
            .size([window_width, window_height]);

        $(window).resize(function () {
                width = $(window).innerWidth();
                height = $(window).height();
                force.size([width, height]);
                force.start();
        });

        var svg = d3.select("body").append("svg")
            .attr("width", $(window).innerWidth())
            .attr("height", $(window).height());

        
        

        d3.json(input, function(error, graph) {
            force
                .nodes(graph.nodes)
                .links(graph.links)
                .start();

            var link = svg.selectAll(".link")
                .data(graph.links)
                .enter().append("line")
                .attr("class", "link")
                .style("stroke-width", function(d) {
                    return 1;
                });

            var node = svg.selectAll(".node")
                .data(graph.nodes)
                .enter().append("circle")
                .attr("class", "node")
                .attr("r", function(d) {
                    if(Math.sqrt(d.weight) >= 3){
                        return Math.sqrt(d.weight);
                    }else{
                         return 5; 
                    }
                   
                })
                .style("fill", function(d) {
                    return color(d.group);
                })
                .call(force.drag);



            force.on("tick", function() {
                link.attr("x1", function(d) {
                        return d.source.x;
                    })
                    .attr("y1", function(d) {
                        return d.source.y;
                    })
                    .attr("x2", function(d) {
                        return d.target.x;
                    })
                    .attr("y2", function(d) {
                        return d.target.y;
                    });

                node.attr("cx", function(d) {
                        return d.x;
                    })
                    .attr("cy", function(d) {
                        return d.y;
                    });
            });

        

        var g = svg.append('g').attr("transform" ,"scale(0)").attr('id', "textbox_g");
        var rect = g.append('rect')
                        .attr('id', 'textbox')
                        .attr('width', 200)
                        .attr('height', 250)
                        .attr('x', 40)
                        .attr('y', 100)
                        .style('fill', 'none')
                        .attr('stroke', 'black')
        var text = g.append('foreignObject')
                        .attr('id','text')
                        .attr('x', 50)
                        .attr('y', 130)
                        .attr('width', 200)
                        .attr('height', 250)
                        .append("xhtml:body")

         g.transition().duration(500).attr("transform" ,"scale(1)");


            $.get('textfile.txt', function(data){
                    var text_old = document.getElementById("text");
                    text.attr('style', 'width:150px');
                    text.html(data);
            });
        });
    }
}


graphData(input);