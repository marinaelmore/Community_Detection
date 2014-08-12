/* FILE: displaygraph.js
 * AUTHORS: Marina Elmore, Jennifer Hu
 * AHPCRC Summmer Institute 2014
 -------------------------------------------------
 * This Javascript function displays a force-directed graph of the dataset
 * selected by the client. It also creates a textbox that details the statitics
 * for each graph, given a perspective to the efficacy of the Louvain Algorithm
 */

function graphData(input, textfile) {
        //Getting window size and width
        var window_width = $(window).innerWidth(),
            window_height = $(window).height()

        //Colors
        var color = d3.scale.category20();

        //Setting force
        var force = d3.layout.force()
            .charge(-120)
            .linkDistance(200)
            .size([window_width, window_height]);

        //Resize Function (for recentering the graph when the window is changed)
        $(window).resize(function () {
                width = $(window).innerWidth();
                height = $(window).height();
                force.size([width, height]);
                force.start();
        });

        var svg = d3.select("body").append("svg")
            .attr("width", $(window).innerWidth())
            .attr("height", $(window).height());

        //Created the graph from the JSON file passed into the function
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

        
        //Creating the textbox with statistics about each graph iteration
        var g = svg.append('g').attr("transform" ,"scale(0)").attr('id', "textbox_g");
        var rect = g.append('rect')
                        .attr('id', 'textbox')
                        .attr('width', 210)
                        .attr('height', 250)
                        .attr('x', 20)
                        .attr('y', 100)
                        .style('fill', 'white')
                        .style("fill-opacity", 0.6)
                        .attr('stroke', 'black')
        var text = g.append('foreignObject')
                        .attr('id','text')
                        .attr('x', 45)
                        .attr('y', 102)
                        .attr('width', 225)
                        .attr('height', 250)
                        .style("background", "transparent");

         g.transition().duration(500).attr("transform" ,"scale(1)");

         //Ajax call to get statistics from various textfiles
         $.ajax({
              type: 'GET',
              url: "getStatistics?me=" + textfile,

              success: function() {
                $.get('stats.txt', function(data){
                    var text_old = document.getElementById("text");
                    text.attr('style', 'width:200px');
                    text.html(data);
                });
              }
            })
        });
    
}
//Calling the graph data function
graphData(input, textfile);