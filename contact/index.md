---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

Our team is composed of passionate PhD students, driven M.Tech researchers, and aspiring M Tech coursework students, all united by our shared curiosity and commitment to excellence. Together, we embark on cutting-edge research projects, explore novel ideas, and tackle real-world challenges with creativity and rigor. Join us on our journey as we shape the future of Scientific computing research through collaboration, discovery, and academic excellence

{%
  include button.html
  type="email"
  text="raha@iisc.ac.in"
  link="raha@iisc.ac.in"
%}
{%
  include button.html
  type="phone"
  text="+91-80-2293-2791"
  link="+91-80-2293-2791"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://maps.app.goo.gl/jJjBMSmyBmPrJzqP7"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/contact/IISCMainBldg.jpg"
  caption="IISc Main Building"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/contact/CDS_Dept.jpg"
  caption="CDS Department Building"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}
