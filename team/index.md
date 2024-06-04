---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

We are a team of dedicated and hardworking individuals, united by our passion for innovation and fueled by collaboration. Together, we form a vibrant community committed to advancing the frontiers of knowledge in the dynamic field of scientific computation. Scroll down to know more about us!!!

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}


{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: phd" %}

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role:undergrad"%}

{% include section.html background="images/background.jpg" dark=true %}

We delve into various team-building activities to foster a strong sense of camaraderie and collaboration within our group, led by our esteemed Professor Soumyendu Raha. Through engaging workshops, brainstorming sessions and collaborative projects, we cultivate an environment where every member's unique expertise and perspective are valued. Our commitment to teamwork and mutual support not only enhances our individual growth but also propels our collective efforts towards groundbreaking advancements in the diverse realm of scientific computation.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/team/Team1.jpg" %}
{% include figure.html image="images/team/Team2.jpg" %}
{% include figure.html image="images/team/Team3.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}

{% include carousel.html %}
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="images/team/Team1.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="images/team/Team2.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="images/team/Team3.jpg" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
