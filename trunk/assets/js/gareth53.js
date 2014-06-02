var ap_instances = new Array();

function ap_stopAll(playerID) {
	for(var i=0 ; i<ap_instances.length ; i++) {
		try {
			if (ap_instances[i] != playerID) {
			    document.getElementById("audioplayer" + ap_instances[i].toString()).SetVariable("closePlayer", 1);
			}
			else {
			    document.getElementById("audioplayer" + ap_instances[i].toString()).SetVariable("closePlayer", 0);
		    }
		} catch( errorObject ) {
			// stop any errors
		}
	}
}


$(function() {
    
    // MP3 Audio Player
    audioPlayerOptions = {
    	bg:             "0xb1bbd0",
    	leftbg:         "0xa7b2ca",
    	lefticon:       "0x3c4963",
    	rightbg:        "0x8695b6",
    	rightbghover:   "0x596c93",
    	righticon:      "0x3c4963",
        righticonhover: "0xffffff",
    	text: 			"0x3c4963",
    	slider: 		"0x3c4963",
    	track: 			"0xFFFFFF",
    	border: 		"0x3c4963",
    	loader: 		"0x8998b8",
    	loop: 			"no",
    	autostart: 		"no"
	}
    optionStr = ""
    for (name in audioPlayerOptions) {
        optionStr = optionStr + "&" + name + "=" + eval('audioPlayerOptions.' + name);
    }
    mp3_links = 0;
    $('p.listen a').each(function() {
        mp3_links++;
        mp3_href = $(this).attr("href");
        h = '<div class="swf-player"><object type="application/x-shockwave-flash" data="/assets/swf/mp3-player.swf" id="audioplayer'+mp3_links+'" height="24" width="290">\n' +
            '<param name="movie" value="/assets/swf/mp3-player.swf">\n' +
            '<param name="FlashVars" value="playerID='+mp3_links+'&amp;soundFile='+mp3_href+optionStr+'">\n' +
            '<param name="quality" value="high">\n' +
            '<param name="menu" value="false">\n' +
            '<param name="wmode" value="transparent">\n' +
            '</object></div>'
            $(this).after(h);
            $(this).remove();
            ap_instances.push(mp3_links);
        });

    // RSS feeds
    $("a[href$='.xml']").addClass("rss");

    $('body#podcast div#keywords').hide();

    visToggler = document.createElement('a');
    visToggler.id = "keywordToggle"
    visToggler.href = "#keywords"

    initialText = document.createTextNode("Show keywords");
    visToggler.appendChild(initialText);
    visTogglerVis = false;
    $(visToggler).appendTo($('body#podcast div#keywords').prev());
    
    $('a#keywordToggle').click(function() {
        if (visTogglerVis) {
            $('div#keywords').hide('slow');
            $(visToggler).html("Show keywords");
            visTogglerVis = false;
        }
        else {
            $('div#keywords').show('slow');
            $(visToggler).html("Hide keywords");            
            visTogglerVis = true;
        }
        return false;
    })

    lastfm_APIkey = '996f8314f90aac4358c7de18e00d774a';
	lastfm_url = 'http://ws.audioscrobbler.com/2.0/';
    $('a.lastfm-profile-link').each(function(){
        if (this.href.indexOf('http://www.last.fm/user/') != -1) {
            user_id = this.href.replace('http://www.last.fm/user/','')
            user_id = user_id.replace('/','');
        	jsonUrl = lastfm_url + '?method=user.getRecentTracks&user='+user_id+'&format=json&api_key=' + lastfm_APIkey + '&limit=5&format=json&callback=?';
        $.getJSON(jsonUrl,
				// TODO - handle data failure or error response
                function(data) {
          			var list = $('<ul />');
                    data = data.recenttracks.track;
              		$.each(data, function(i, _json) { 
	          		    	if ('true' == _json.nowplaying) {
	                        	track_time = 'listening now';
	                        } else {
	                        	track_time = _json.date['#text'];
	                        	regex_year = new RegExp(" [0-9]\{4,4\}","g")
	                        	track_time = track_time.replace(regex_year,'');
	                        }
	                        list_item = $('<li />').html(_json.artist['#text'] + " - " + _json.name)
							time_span = $('<span />').attr('class','track_time').html(" (" + track_time +")").appendTo(list_item);
							list_item.appendTo(list);
	                    }
	                )
                list.insertBefore($('a.lastfm-profile-link').parent());
                }
            );
        }
        else {
            // no user id?
            // return an error message
            // this will be hidden by the CSS
            lastfm_error = $('<p />');
            lastfm_error.id = "lastfm_error";
            lastfm_error.html("Couldn't load recent tracks: unknown username");
            $('body').append(lastfm_error);
        }
    })

});