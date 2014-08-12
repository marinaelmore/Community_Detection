/* FILE: callParsefile.js
 * AUTHORS: Marina Elmore, Jennifer Hu
 * AHPCRC Summmer Institute 2014
 -------------------------------------------------
 * This file calls Delite and parses the text files based on the selection
 * of the client. Really acts as the backbone that connects the frontend
 * and backend of the application
 */

function check_valid_inputs(){
    var d_selected = $("#d_select").find('option:selected').attr('id');
    var v_selected = $("#v_select").find('option:selected').attr('id');
    var cf_txt = $("#cf_txt")[0].value;
    var thread_txt = $("#thread_txt")[0].value;
    var return_val = true;

    //FIELD ONE
    if(d_selected == "d_null"  && v_selected == "v_null"){
        console.log("Needs to select an option");
        return_val = false;    
    }
    if(!$.isNumeric(cf_txt) && cf_txt != ""){ //not numeric
        console.log("Not valid cf");
        $('#cf_txt').val(''); //clear input
        return_val = false;
    }else if(cf_txt != ""){
        console.log("cf numeric");
        cf_txt = Number(cf_txt);
        if(cf_txt <= 0){
           $('#cf_txt').val('');
           return_val = false;
       }
   }
   //FIELD TWO
  if(!$.isNumeric(thread_txt) && thread_txt != ""){  //Not a valid number
        console.log("Not valid thread");
        $('#thread_txt').val(''); //clear input
        return_val = false;
    }else if(thread_txt != ""){
        console.log("thread valid numeric");
        thread_txt = Number(thread_txt);
        if(thread_txt <= 0 || thread_txt > 4){  //Not valid number, using default
           console.log("Not valid thread");
           $('#thread_txt').val('');
           return_val = false;
       }
   }
   return return_val;
}


//Returns map from chosen graph to dataset and input file
function return_input_dict(chosen_graph){
    var dict = new Object();
    
    var dataset = "";
    var input_file = "";

   if(chosen_graph == "d_facebook" || chosen_graph == "v_facebook" ){
        dataset = "facebook";
        input_file = "facebook_combined.txt";
    }else if(chosen_graph == "d_higgs" || chosen_graph == "v_higgs"){
        dataset = "higgs";
        input_file = "higgs-social_network.txt";
    }else if(chosen_graph == "d_oregon" || chosen_graph == "v_oregon"){
        dataset = "oregon";
        input_file = "oregon1.txt"; 
    }else if(chosen_graph == "d_twitter" || chosen_graph == "v_twitter"){
        dataset = "twitter";
        input_file = "twitter_combined.txt"; 
    }else if(chosen_graph == "d_hepPh" || chosen_graph == "v_hepPh"){
        dataset = "hepPh";
        input_file = "hepPh.txt"; 
    }else if(chosen_graph == "d_hepTh" || chosen_graph == "v_hepTh"){
        dataset = "hepTh";
        input_file = "hepTh.txt"; 
    }else if(chosen_graph == "d_wiki" || chosen_graph == "v_wiki"){
        dataset = "wiki";
        input_file = "wiki-Vote.txt"; 
    }else if(chosen_graph == "d_gnutella" || chosen_graph == "v_gnutella"){
        dataset = "gnutella";
        input_file = "p2p-Gnutella04.txt"; 
    }
    dict["dataset"] = dataset;
    dict["input_file"] = input_file;
    return dict;
}


//Loads the progress bar given and intial time and a timestep
    //NOTE timestep must go evenly into width or function will not terminate
function load_progress_bar(initial_time, timestep){
    var progress = initial_time;
    while ($('#progress-inner').attr('style') != "width: 90%") {
        $('#progress-inner').attr('style', 'width: ' + progress + '%');
            progress += timestep;
    }
}

//When the "Graph Button" is clicked
    $(function() {
        $("#graph_btn").click(function() {
            if(!check_valid_inputs()){ //If inputs not valid
                alert("Please resolve errors before continuing");
            }else{
               var d_selected = $("#d_select").find('option:selected').attr('id');
               var v_selected = $("#v_select").find('option:selected').attr('id');
               var cf_txt = $("#cf_txt")[0].value;
               var thread_txt = $("#thread_txt")[0].value;
                
                //If inputs are left for the default
                if(cf_txt == ""){
                    cf_txt = "0.01";
                }
                if(thread_txt == ""){
                    thread_txt = "2";
                }

               
               //Runs program with Community Detection
               if(d_selected != "d_null" && v_selected == "v_null"){
                    console.log("Running Community Detection");
                    var input_dict = return_input_dict(d_selected);
                    var url_new = "callDelite?me=" + input_dict["input_file"] + ":" + input_dict["dataset"] + ":" + cf_txt + ":" + thread_txt;
                    console.log(url_new);

                    $("#graph_btn").attr('style', "display: none;");
                    $("#progress-bar").attr('style', "display: show;");
                    $("#progress-lbl").attr('style', "display: show;");


                    $.ajax({
                        type: 'GET',
                        url: url_new,

                        success: function(data) {   
                            console.log(data);
                            console.log("calls Delite success");
                        }
                        
                     }).done(function (){
                        load_progress_bar(0, 10);

                         setTimeout(function () { 
                            $.ajax({
                            type: 'GET',
                            url: "parsefile?me=" + input_dict["dataset"],

                            success: function(data) {
                                console.log("calls parsefile success");
                                var new_url = "displayGraph.html?me=" + input_dict["dataset"] + "_0";
                                window.location.href = new_url;
                            }
                         });
                        }, 2000);
                    });
            //Runs without Community Detection
            }else if (d_selected == "d_null" && v_selected != "v_null"){
            var input_dict = return_input_dict(v_selected);
             
             $.ajax({
                type: 'GET',
                url: "parsefile?me=" + input_dict["dataset"],

                success: function() {
                    console.log("calls parsefile success");
                    var new_url = "displayGraph.html?me=" + input_dict["dataset"] + "_0";
                    window.location.href = new_url;
                }
            });
         }else{
            alert("Please only select one option."); //alert if both select menus are selected
         }
        }
    });
});
