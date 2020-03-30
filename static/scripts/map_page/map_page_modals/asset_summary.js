document.getElementById('Summarize_Asset_Connections').addEventListener('click',function ()
{
    Summarize_Asset_Connections();
});

//alert('test');
function Summarize_Asset_Connections() {
    //alert('hola');   
    document.getElementById('AssetSummaryModal').style.display='block';
    $.ajax({
		url: '/asynchronously_summarize_asset_connections_and_save_to_svg',
		type: 'POST',
		success: function(response){
			var ary = response.split('|');
			$('#asset_summary_emulsion_svg').html(ary[0]);
			$('#asset_summary_steam_svg').html(ary[1]);
			// assume 160 is the starting position of map and each row is 19 pixels high, 19 pixel is according to plot size
			if ((160 + ary[2] * 19) <= (window.innerHeight * 0.80)) {
				document.getElementById('AssetSummaryModal').getElementsByClassName('modal-content')[0].style.height = (160 + ary[2] * 19) + 'px';
				document.getElementById('asset_summary_scroll').style.overflowY = 'hidden';
				document.getElementById('asset_summary_scroll').style.height = ary[2] * 19 + 'px';
			} else {
				document.getElementById('AssetSummaryModal').getElementsByClassName('modal-content')[0].style.height = '95%';
				document.getElementById('asset_summary_scroll').style.height = '70%'; // This is consider scroll bar height will take 10% of entire space
				document.getElementById('asset_summary_scroll').style.overflowY = 'scroll';
			}
			console.log("Asset connections summarized successfully.")
		},
		error: function(error){
			console.log("Failed to summarize asset connections.")
		}
    });
  }

