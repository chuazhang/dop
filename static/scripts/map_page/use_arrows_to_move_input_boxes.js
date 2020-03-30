	//source: https://jonlabelle.com/snippets/view/html/navigate-html-text-input-fields-with-arrow-keys
	$(document).ready(function () {
	
	  $('input').keydown(function (e) {
	    if (e.which == 39) { // right arrow
	      $(this).closest('td').next().find('input').focus();
	
	    } else if (e.which == 37) { // left arrow
	      $(this).closest('td').prev().find('input').focus();
	
	    } else if (e.which == 40) { // down arrow
	      $(this).closest('tr').next().find('td:eq(' + $(this).closest('td').index() + ')').find('input').focus();
	
	    } else if (e.which == 38) { // up arrow
	      $(this).closest('tr').prev().find('td:eq(' + $(this).closest('td').index() + ')').find('input').focus();
	    }
	  });
	
	// un-comment to display key code
	// $("input").keydown(function (e) {
	//   console.log(e.which);
	// });
	});