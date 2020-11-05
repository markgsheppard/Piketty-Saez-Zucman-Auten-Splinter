# Replicating Piketty, Saez, & Zucman and Auten & Splinter
This replication study recreates the results of two seminal works on income concentration, namely Piketty, Saez, & Zucman (2016), and Auten & Splinter (2019). 
<h1> Test </h1> 


<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"> <!-- begin SEO --><title>About me - Jeffrey A. Levy</title><meta property="og:locale" content="en-US"><meta property="og:site_name" content="Jeffrey A. Levy"><meta property="og:title" content="About me"><link rel="canonical" href="https://jeffreyalevy.com/"><meta property="og:url" content="https://jeffreyalevy.com/"><meta property="og:description" content="About me"> <script type="application/ld+json"> { "@context" : "http://schema.org", "@type" : "Person", "name" : "Jeffrey A. Levy", "url" : "https://jeffreyalevy.com", "sameAs" : null } </script> <!-- end SEO --><link href="https://jeffreyalevy.com/feed.xml" type="application/atom+xml" rel="alternate" title="Jeffrey A. Levy Feed"> <!-- http://t.co/dKP3o1e --><meta name="HandheldFriendly" content="True"><meta name="MobileOptimized" content="320"><meta name="viewport" content="width=device-width, initial-scale=1.0"> <script> document.documentElement.className = document.documentElement.className.replace(/\bno-js\b/g, '') + ' js '; </script> <!-- For all browsers --><link rel="stylesheet" href="https://jeffreyalevy.com/assets/css/main.css"><meta http-equiv="cleartype" content="on"> <!-- start custom head snippets --><link rel="apple-touch-icon" sizes="57x57" href="https://jeffreyalevy.com/images/apple-touch-icon-57x57.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="60x60" href="https://jeffreyalevy.com/images/apple-touch-icon-60x60.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="72x72" href="https://jeffreyalevy.com/images/apple-touch-icon-72x72.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="76x76" href="https://jeffreyalevy.com/images/apple-touch-icon-76x76.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="114x114" href="https://jeffreyalevy.com/images/apple-touch-icon-114x114.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="120x120" href="https://jeffreyalevy.com/images/apple-touch-icon-120x120.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="144x144" href="https://jeffreyalevy.com/images/apple-touch-icon-144x144.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="152x152" href="https://jeffreyalevy.com/images/apple-touch-icon-152x152.png?v=M44lzPylqQ"><link rel="apple-touch-icon" sizes="180x180" href="https://jeffreyalevy.com/images/apple-touch-icon-180x180.png?v=M44lzPylqQ"><link rel="icon" type="image/png" href="https://jeffreyalevy.com/images/favicon-32x32.png?v=M44lzPylqQ" sizes="32x32"><link rel="icon" type="image/png" href="https://jeffreyalevy.com/images/android-chrome-192x192.png?v=M44lzPylqQ" sizes="192x192"><link rel="icon" type="image/png" href="https://jeffreyalevy.com/images/favicon-96x96.png?v=M44lzPylqQ" sizes="96x96"><link rel="icon" type="image/png" href="https://jeffreyalevy.com/images/favicon-16x16.png?v=M44lzPylqQ" sizes="16x16"><link rel="manifest" href="https://jeffreyalevy.com/images/manifest.json?v=M44lzPylqQ"><link rel="mask-icon" href="https://jeffreyalevy.com/images/safari-pinned-tab.svg?v=M44lzPylqQ" color="#000000"><link rel="shortcut icon" href="/images/favicon.ico?v=M44lzPylqQ"><meta name="msapplication-TileColor" content="#000000"><meta name="msapplication-TileImage" content="https://jeffreyalevy.com/images/mstile-144x144.png?v=M44lzPylqQ"><meta name="msapplication-config" content="https://jeffreyalevy.com/images/browserconfig.xml?v=M44lzPylqQ"><meta name="theme-color" content="#ffffff"><link rel="stylesheet" href="https://jeffreyalevy.com/assets/css/academicons.css"/> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ TeX: { equationNumbers: { autoNumber: "all" } } }); </script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { inlineMath: [ ['$','$'], ["\\(","\\)"] ], processEscapes: true } }); </script> <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <!-- end custom head snippets --></head><body> <!--[if lt IE 9]><div class="notice--danger align-center" style="margin: 0;">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</div><![endif]--><div class="masthead"><div class="masthead__inner-wrap"><div class="masthead__menu"><nav id="site-nav" class="greedy-nav"> <button><div class="navicon"></div></button><ul class="visible-links"><li class="masthead__menu-item masthead__menu-item--lg"><a href="https://jeffreyalevy.com/">Jeffrey A. Levy</a></li><li class="masthead__menu-item"><a href="https://jeffreyalevy.com/talks/">Talks</a></li><li class="masthead__menu-item"><a href="https://jeffreyalevy.com/teaching/">Teaching</a></li><li class="masthead__menu-item"><a href="https://jeffreyalevy.com/projects/">Projects</a></li><li class="masthead__menu-item"><a href="https://jeffreyalevy.com/cv/">CV</a></li></ul><ul class="hidden-links hidden"></ul></nav></div></div></div><div id="main" role="main"><div class="sidebar sticky"><div itemscope itemtype="http://schema.org/Person"><div class="author__avatar"> <img src="https://jeffreyalevy.com/images/bio_photo.jpg" class="author__avatar" alt="Jeff Levy"></div><div class="author__content"><h3 class="author__name">Jeff Levy</h3><p class="author__bio">Lecturer at the <a style='color: black;' href='https://harris.uchicago.edu/'>Harris School of Public Policy</a> and PhD candidate in Economics at <a style='color: black;' href='https://www.american.edu/cas/economics/'>American University</a>.</p></div><div class="author__urls-wrapper"> <button class="btn btn--inverse">Follow</button><ul class="author__urls social-icons"><li><i class="fa fa-fw fa-map-marker" aria-hidden="true"></i> Chicago, IL</li><li><a href="mailto:levyjeff@uchicago.edu"><i class="fa fa-fw fa-envelope-square" aria-hidden="true"></i> Email</a></li><li><a href="https://www.linkedin.com/in/levyjeff"><i class="fa fa-fw fa-linkedin-square" aria-hidden="true"></i> LinkedIn</a></li><li><a href="https://github.com/levyjeff"><i class="fa fa-fw fa-github" aria-hidden="true"></i> Github</a></li><li><a href="https://www.stackoverflow.com/users/5534457/jeff"><i class="fa fa-fw fa-stack-overflow" aria-hidden="true"></i> Stackoverflow</a></li></ul></div></div></div><article class="page" itemscope itemtype="http://schema.org/CreativeWork"><meta itemprop="headline" content="About me"><meta itemprop="description" content="About me"><div class="page__inner-wrap"><header><h1 class="page__title" itemprop="headline">About me</h1></header><section class="page__content" itemprop="text"><p>Welcome, and thanks for visiting my site! I am a lecturer in public policy and PhD candidate in economics who works at the intersection data science and social science. I was able to get my hands into a wide variety of projects over my three years as a Data Scientist at the Urban Institute, where I was part of a small team that partnered with researchers whose work faced advanced technical hurdles. My joint understanding of research methods, econometrics and programming allows me to contribute in meaningful ways to nearly any research. My current role teaching at the University of Chicago allows me to pass this experience on to students hoping to enter the field of public policy research.</p><p>My PhD dissertation, which I aim to complete in summer 2019, is in the field of empirical macroeconomics. More specifically, I study the causes and impacts of economic uncertainty on the real economy, following a long line of economists from <a href="https://academic.oup.com/qje/article-abstract/51/2/209/1939387">Keynes</a>, <a href="https://mises.org/sites/default/files/Risk,%20Uncertainty,%20and%20Profit_4.pdf">Knight</a>, <a href="https://academic.oup.com/qje/article-abstract/98/1/85/1869115">Bernanke</a>, <a href="https://academic.oup.com/qje/article-abstract/105/3/597/1864581">Romer</a> and more recently, <a href="https://www.economics.utoronto.ca/public/workingPapers/tecipa-352.pdf">Alexopoulos and Cohen</a> and <a href="https://academic.oup.com/qje/article/131/4/1593/2468873">Baker, Bloom and Davis</a>. As uncertainty has been shown to be counter-cyclical, unraveling the causal relationship between uncertainty and the economy has been an active area of research, particularly since the 2007 financial crisis and ensuing Great Recession.</p><p>I have several key principles in my work:</p><ul><li>A focus on open source software, particularly Python.</li><li>Strict adherence to what I like to call “Step 0” reproducible research. As an expert in web scraping, wherever possible all of my projects begin with the programmatic retrieval of raw data from the web, and end with producing the final results. Anything less greatly hinders troubleshooting, and introduces human error into the all-important step of reproducing research results.</li><li>An emphasis on finding and using unique or hard-to-access data sources that allows for the study of straight-forward questions.</li></ul><p>In my graduate and undergraduate economics studies, and in speaking with many colleagues who have gone through similar programs, I have observed a consistent trend: a heavy focus on econometrics and theoretical models, with little-to-no focus on data. This imbalance is, I believe, a mistake, and directly at odds with performing actual research, where a large majority of a researcher’s time is spent on data. If I were to pick one single, over-arching goal of my work, it would be to help address this discrepancy with students and researchers.</p></section><footer class="page__meta"></footer></div></article></div></script><div class="page__footer"><footer> <!-- start custom footer snippets --> <a href="/sitemap/">Sitemap</a> <!-- end custom footer snippets --><div class="page__footer-follow"><ul class="social-icons"><li><strong>Follow:</strong></li><li><a href="http://github.com/levyjeff"><i class="fa fa-fw fa-github" aria-hidden="true"></i> GitHub</a></li><li><a href="https://jeffreyalevy.com/feed.xml"><i class="fa fa-fw fa-rss-square" aria-hidden="true"></i> Feed</a></li></ul></div><div class="page__footer-copyright">&copy; 2020 Jeffrey A. Levy. Powered by <a href="http://jekyllrb.com" rel="nofollow">Jekyll</a> &amp; <a href="https://github.com/academicpages/academicpages.github.io">AcademicPages</a>, a fork of <a href="https://mademistakes.com/work/minimal-mistakes-jekyll-theme/" rel="nofollow">Minimal Mistakes</a>.</div></footer></div><script src="https://jeffreyalevy.com/assets/js/main.min.js"></script> <script> (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){ (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,'script','//www.google-analytics.com/analytics.js','ga'); ga('create', '', 'auto'); ga('send', 'pageview'); </script></body></html>
