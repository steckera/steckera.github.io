var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'spreadsheet.py');
ourRequest.onload = function(){
	return(ourRequest.responseText);
};
//ourRequest.send();

// setup some JSON to use
var data = JSON.parse('data');
var cells;

for (var i = 0; i < data.length; i++){
	

}

window.onload = function() {
	// setup the button click
	document.getElementById("btn").onclick = function() {
		popTable()
	};
}

function popTable() {
	// iterate through the json to create table rows dynamically
	var data = JSON.parse('data');
	var cells;

	for (var i = 0; i < data.length; i++){
		if i

	}

	});
	// stop link reloading the page
 event.preventDefault();
}
</script>

