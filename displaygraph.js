function graphData(input) {

    if (input != "") {

        var window_width = $(window).innerWidth(),
            window_height = $(window).innerHeight()

        var color = d3.scale.category20();

        var force = d3.layout.force()
            .charge(-120)
            .linkDistance(200)
            .size([window_width, window_height]);

        $(window).resize(function () {
                width = $(window).innerWidth();
                height = $(window).innerHeight();
                force.size([width, height]);
                force.start();
        });

        var svg = d3.select("body").append("svg")
            .attr("width", $(window).innerWidth())
            .attr("height", $(window).innerHeight());

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

            node.append("text")
                .attr("class", "nodetext")
                .attr("dx", 12)
                .attr("dy", ".35em")
                .text(function(d) {return "marina"});


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
        });
    }
}


graphData(input);