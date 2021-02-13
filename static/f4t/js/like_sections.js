$(function () {
  
  // blog like button
  $(document).on("click", "#like_blog_button", (event) => {
    event.preventDefault();
    var formData = $("#like_blog_form").serialize();
    var slug = $("#like_blog_button").attr("value");

    $.ajax({
      type: "POST",
      url: `/like_blog/${slug}/`,
      data: formData,
      dataType: "json",
      success: (response) => {
        $("#like_section").html(response["like"]);
      },
      error: (rs, e) => {
        console.log(rs.responseText);
      },
    });
  });
});
