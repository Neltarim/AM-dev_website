function fadeIn( elem, ms )
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
 
function fadeOut( elem, ms )
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


function show_section(section) {
    var welcome = document.getElementById("welcome");
    var section_to_show = document.getElementById(section);


    if(section == "welcome" && welcome.style.display == "none") { /* if the user want to show the welcome section */
        fadeIn(welcome, 200);
        setTimeout(() => {welcome.style.display = "inline";}, 199);
        return 0; /* stop here to cancel the next instruction (important) */
    }

    if (welcome.style.display != "none" && section != "welcome") { /* Turn off welcome display */
        fadeOut(welcome, 200);
        setTimeout(() => {welcome.style.display = "none";}, 199);
    } else {    /* if another section is already open */
        var sections = document.getElementsByClassName("central-div");

        for(var i=0; i < sections.length; i++) {
            if (sections[i].style.display == "inline") {
                fadeOut(sections[i], 200)
                setTimeout(() => {sections[i].style.display = "none";}, 199);
            }
        }
    }

    try { /* now try to display the section to open */
        section_to_show.style.display = "inline";
    } catch (error) {
        console.log(error);
    }
}


function collapse() {

    var nav = document.getElementById('PrimaryNav');
    var is_collapsed = false;

    els =  nav.classList;
    for(var i=0; i < els.length; i++) {
        if (els[i] == "show") {
            is_collapsed = true;
        }
    }

    if (!is_collapsed) {
        fadeIn(nav, 200);
        setTimeout(() => {nav.classList.add("show");}, 199);
    } else {
        fadeOut(nav, 200);
        setTimeout(() => {nav.classList.remove("show");}, 199);
    }
}