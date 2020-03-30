
// Get the modals
var EmulsionLineModal = document.getElementById("EmulsionLineModal");
var PadModal = document.getElementById("PadModal");
var CPFModal = document.getElementById("CPFModal");
var AssetSummaryModal=document.getElementById("AssetSummaryModal");
var AssignTypeCurvesModal=document.getElementById("AssignTypeCurvesModal");
var SaveScenarioModal = document.getElementById("SaveScenarioModal");
var LogOutModal = document.getElementById("LogOutModal");
var ChangeHistoryModal = document.getElementById("ChangeHistoryModal");
var InviteUserModal = document.getElementById("InviteUserModal");
var BaseCaseModal = document.getElementById("BaseCaseModal");

// Get the <span> element that closes the modal
var EmulsionLineModalCloseSpan = document.getElementById("EmulsionLineModalClose");
var PadModalCloseSpan = document.getElementById("PadModalClose");
var CPFModalCloseSpan = document.getElementById("CPFModalClose");
var AssetSummaryCloseSpan=document.getElementById("AssetSummaryModalClose");
var AssignTypeCurvesModalCloseSpan=document.getElementById("AssignTypeCurvesModalClose");
var SaveScenarioModalCloseSpan = document.getElementById("SaveScenarioModalClose");
var LogOutModalCloseSpan = document.getElementById("LogOutModalClose");
var ChangeHistoryModalCloseSpan = document.getElementById("ChangeHistoryModalClose");
var InviteUserModalCloseSpan = document.getElementById("InviteUserModalClose");
var BaseCaseModalCloseSpan = document.getElementById("BaseCaseModalClose");

// When the user clicks on <span> (x), close the modal
EmulsionLineModalCloseSpan.onclick = function() {
  	EmulsionLineModal.style.display="none";
}
PadModalCloseSpan.onclick = function() {
  	PadModal.style.display = "none";
}
CPFModalCloseSpan.onclick = function() {
  CPFModal.style.display = "none";
}
AssetSummaryCloseSpan.onclick = function() {
  AssetSummaryModal.style.display = "none";
}
AssignTypeCurvesModalCloseSpan.onclick = function() {
  AssignTypeCurvesModal.style.display = "none";
}
SaveScenarioModalCloseSpan.onclick = function() {
  SaveScenarioModal.style.display = "none";
}
LogOutModalCloseSpan.onclick = function() {
  LogOutModal.style.display = "none";
}
ChangeHistoryModalCloseSpan.onclick = function() {
  ChangeHistoryModal.style.display = "none";
}
InviteUserModalCloseSpan.onclick = function() {
  InviteUserModal.style.display = "none";
}
BaseCaseModalCloseSpan.onclick = function() {
  BaseCaseModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == PadModal) {
    PadModal.style.display = "none";
  } else if (event.target == CPFModal) { 
    CPFModal.style.display = "none";
  } else if (event.target == EmulsionLineModal) {
  	EmulsionLineModal.style.display="none";
  } else if (event.target == AssetSummaryModal) {
  	AssetSummaryModal.style.display="none";
  } else if (event.target == AssignTypeCurvesModal) {
    AssignTypeCurvesModal.style.display="none";
  } else if (event.target == SaveScenarioModal) {
  	SaveScenarioModal.style.display="none";
  } else if (event.target == LogOutModal) {
  	LogOutModal.style.display="none";
  } else if (event.target == ChangeHistoryModal) {
  	ChangeHistoryModal.style.display="none";
  } else if (event.target == InviteUserModal) {
  	InviteUserModal.style.display="none";
  } else if (event.target == BaseCaseModal) {
  	BaseCaseModal.style.display="none";
  }
}

