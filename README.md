# Introduction

This is a unified authoring platform that makes it easy (for reasonably computer-savvy users) to make academic content in all its forms available on the web in a coherent and easily maintained way, increasing both presence and reach of the work going on in an AI research group or CDT.

This platform was built using Quarto, a scientific and technical authoring system (https://quarto.org). it is highly recommended to install (https://quarto.org/docs/get-started/) Quarto.org to render the application locally. 

## Submiting 

The application is tracked by git hub actions. The automatic delivery occurs after a sucessfull push.

### Creating content

First, inside the content directory, create a new directory with your title. Inside this newly created dir create a index.qmd file, according to the model below. 

```
---
title: "<Your Title>"

categories: ["category_1", "category_2", "category_3"]
format: 
  html:
    df-print: paged
    toc: true
---


## Tldr 
<TLDR>
    
## Author 
<author>

## Image  

![hero-image](<link-to-the-image>)

## Paper-authors
<paper-authors>

## Venue
- [<venue-name>](<venue-link>)

## Video   

{{< video <link-to-the-video> >}}

## Slides
<link-to-the-slides>

## Code
<code-repository>

## More Resources

[PDF](<link-to-pdf>)

[Poster](<link-to-poster>)

[Supplement](<link-for-suplement>)

[Scholar](<google-scholar-link>)

[Blog Post](../../posts/<name-for-your-blogpost>/)*

```

*You can create a blog post related to your content and link it.

### Creating a Blog post 

The blog post creation is similar to content creation. First create a new directory into the posts directory. 
Inside the new created directory add a index.qmd file that will include your blogpost.