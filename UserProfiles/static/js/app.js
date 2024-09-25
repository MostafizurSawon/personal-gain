console.log("working")
document.addEventListener('DOMContentLoaded', function() {
  // Locate the element by id
  var positionDiv = document.getElementById('div_id_position');
  
  // Create the new anchor element
  var newLink = document.createElement('a');
  newLink.href = '/profile/add-position/';
  newLink.target = '_blank';
  newLink.className = 'btn btn-link text-decoration-none';  // Add your CSS class
  newLink.textContent = 'Not here? Add New Position';

  // Append the link to the position div
  positionDiv.appendChild(newLink);
});

// hover text in social link in profile
console.log("inside tooltip trigger 1")
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  console.log("inside tooltip trigger")
  return new bootstrap.Tooltip(tooltipTriggerEl)
})
