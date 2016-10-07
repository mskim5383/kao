$(document).ready(function() {
  if($("div.staff").length > 0) {
    var modify = false;
    $("div#webcontent").mouseenter(function() {
      if(!modify) {
        var webcontent = $(this);
        webcontent.append("<button id='webcontent-modify'>modify</button>");
        webcontent.children("button#webcontent-modify").click(function() {
          modify = true;
          var name = webcontent.attr("name");
          webcontent.children("button#webcontent-modify").remove();
          var html = webcontent.html();
          webcontent.html("<textarea id='webcontent-textarea'></textarea><button id='webcontent-submit'>submit</button>");
          var textarea = webcontent.children("textarea#webcontent-textarea");
          textarea.val(html);
          var button = webcontent.children("button#webcontent-submit");
          button.click(function() {
            var content = textarea.val();
            $.ajax({
              url : "/webcontent/",
              type : "POST",
              data : {csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), content:content, name:name},
              dataType : "json",
              success : function(data) {
                console.log(data);
                if(data.status == "success") {
                  webcontent.html(data.content);
                  modify = false;
                }
              }
            });
          });
        });
      }
    }).mouseleave(function() {
      $(this).children("button#webcontent-modify").remove();
    });
  }
});
