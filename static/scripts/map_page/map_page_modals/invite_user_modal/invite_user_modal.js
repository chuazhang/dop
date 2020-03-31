$(document).ready(function () {
    $('#invite_user_email_send').on('click', function (e) {
      document.getElementById('InviteUserModal').style.display='none';
      $.ajax({
        url: '/invite_user_send_email',
        data: document.getElementById('invite_user_email_input').value,
        type: 'POST',
        success: function(response){
          console.log("Asset connections summarized successfully.")
        },
        error: function(error){
          console.log("Failed to summarize asset connections.")
        }
      });
    });
});