function fadeIn( elem, ms ) //Display a html item with a fade
{

    if( ! elem )
        return;
    
    elem.style.opacity = 0;
    elem.style.filter = "alpha(opacity=0)";
    elem.style.display = "inline-block";
    elem.style.visibility = "visible";
    
    if( ms )
    {
        var opacity = 0;
        var timer = setInterval( function() {
        opacity += 50 / ms;
        if( opacity >= 1 )
        {
            clearInterval(timer);
            opacity = 1;
        }
        elem.style.opacity = opacity;
        elem.style.filter = "alpha(opacity=" + opacity * 100 + ")";
        }, 50 );
    }
    else
    {
        elem.style.opacity = 1;
        elem.style.filter = "alpha(opacity=1)";
    }
}
 
function fadeOut( elem, ms ) //Hide a html item with a fade
{
  if( ! elem )
    return;
 
  if( ms )
  {
    var opacity = 1;
    var timer = setInterval( function() {
      opacity -= 50 / ms;
      if( opacity <= 0 )
      {
        clearInterval(timer);
        opacity = 0;
        elem.style.display = "none";
        elem.style.visibility = "hidden";
      }
      elem.style.opacity = opacity;
      elem.style.filter = "alpha(opacity=" + opacity * 100 + ")";
    }, 50 );
  }
  else
  {
    elem.style.opacity = 0;
    elem.style.filter = "alpha(opacity=0)";
    elem.style.display = "none";
    elem.style.visibility = "hidden";
  }
}

function show_section(section) { //Show one section and hide others.
    var section_to_show = document.getElementById(section);

    var sections = document.getElementsByClassName('central-div');
    for (var i=0; i < sections.length; i++) {
        if (sections[i].style.display != "none" && sections[i].id != section) {
            fadeOut(sections[i], 180);
        }
    }

    try {
        setTimeout(() => {fadeIn(section_to_show, 200);}, 270);
    } catch (error) {
        console.log(error);
    }
}


function form_submit(form_id, csrf_token) { //Manual submitting form (MDB is ruining django)
  var form = document.getElementById(form_id);
  var fields = form.getElementsByClassName('form-control');

  var data = new FormData();
  data.append('csrfmiddlewaretoken', csrf_token)

  for (i=0; i < fields.length; i++) {
    data.append(fields[i].id, fields[i].value);
  }

  post_url = window.location.href
  var xhr = new XMLHttpRequest();
  xhr.open('POST', post_url, true );
  xhr.onload = function () {
    if (xhr.status === 201) {
      window.location.pathname = '/thanks';
    } else {
      var node_err = document.createTextNode("Email already registered.");
      p_err = document.createElement("p");
      p_err.appendChild(node_err);
      p_err.classList.add('p_err');

      form.appendChild(p_err);
    }
  }
  xhr.send(data);
} 