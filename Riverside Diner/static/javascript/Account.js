$(document).ready(() => {
  $("#accountInfoForm").show();
  $("#paymentForm").hide();
  $("#reservationInfo").hide();

  $("#accountInfo").on("click", function () {
    $("#accountInfoForm").fadeIn("700");
    $("#paymentForm").hide();
    $("#reservationInfo").hide();
  });

  $("#reservations").on("click", function () {
    $("#accountInfoForm").hide();
    $("#paymentForm").hide();
    $("#reservationInfo").fadeIn("700");
  });

  $("#payment").on("click", function () {
    $("#accountInfoForm").hide();
    $("#paymentForm").fadeIn("700");
    $("#reservationInfo").hide();
  });

  $("#resetPassword").on("click", function () {
    $("#resetWindow").fadeIn("700");
  });
});
