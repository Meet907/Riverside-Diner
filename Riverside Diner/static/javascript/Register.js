jQuery("#registerForm").validate({
  rules: {
    password: {
      minlength: 5,
    },
    confirm_password: {
      minlength: 5,
      equalTo: "#password",
    },
  },
});
