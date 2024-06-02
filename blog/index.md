---
title: Blog
nav:
  order: 4
  tooltip: Musings and miscellany
---

# {% include icon.html icon="fa-solid fa-feather-pointed" %}Blog

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}

<!-- Example image and download button -->
<div class="image-download">
  <img id="image-to-download" src="images/logo.png" alt="Description of Image">
  <button id="download-btn">Download Logo</button>
</div>
<script>
  document.getElementById('download-btn').addEventListener('click', function() {
    var imgPath = document.getElementById('image-to-download').src;
    var fileName = imgPath.substring(imgPath.lastIndexOf('/') + 1);
    var a = document.createElement('a');
    a.href = imgPath;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  });
</script>
<style>
  .image-download {
    text-align: center;
    margin: 20px 0;
  }
  #download-btn {
    display: inline-block;
    padding: 10px 20px;
    margin-top: 10px;
    font-size: 16px;
    color: white;
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
  }
  #download-btn:hover {
    background-color: #0056b3;
  }
</style>