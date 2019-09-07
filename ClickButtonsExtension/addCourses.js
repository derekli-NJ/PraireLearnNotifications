function DOMtoString(document_root) {
    var courseTable = document.getElementsByClassName("table table-sm table-hover table-striped")[0].childNodes[1];
    var table = courseTable.getElementsByTagName("tr");
    var ret = "";
    // for (var i = 0; i < courseTable.length; i++) {
        // var item = courseTable[i];
	// ret += item.innerHTML;
    // }
    for (var i = 0; i < 6; i++) {
        var row = table[i];
        var buttonToClick = row.querySelectorAll('[data-target="#removeModal' + i + '"]');
        // var buttonToClick = row.querySelectorAll('[data-target="#addModal' + i + '"]');
	
        if (buttonToClick.length > 0) {
            // buttonToClick[0].click();
	    // var row = table[i];
	    // ret += row.outerHTML;
            buttonToClick2 = row.querySelectorAll('[type="submit"]')[0];
	    buttonToClick2.click();
	    ret += buttonToClick2.outerHTML;
	    for (var j = 1; j < 100000000; j++) {
                
	    }
        }
    }
    return ret;
}

chrome.runtime.sendMessage({
    action: "addCourses",
    source: DOMtoString(document)
});
