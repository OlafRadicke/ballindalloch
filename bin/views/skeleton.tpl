<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>{{title}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
<!--    <link href="uri_prefix/bootstrap/css/bootstrap.min.css" rel="stylesheet"> -->
    <link rel="alternate" type="application/atom+xml"  href="/atom.xml" title="Atom">
    <link rel="alternate" type="application/rss+xml"  href="/rss.xml" title="rss">
  </head>
  <body>

<!-- Menu -->
    <div>
        <ul> <!--class="nav nav-pills">-->
            <li><a href="{{uri_prefix}}/info">info</a></li>
			<li><a href="{{uri_prefix}}/containers">containers</a></li>
			<li><a href="{{uri_prefix}}/images">images</a></li>
			<li><a href="{{uri_prefix}}/version">version</a></li>
			<li><a href="{{uri_prefix}}/volumes">volumes</a></li>
			<li><a href="{{uri_prefix}}/networks">networks</a></li>
			<li><a href="{{uri_prefix}}/plugins">plugins</a></li>
			<li><a href="{{uri_prefix}}/nodes">nodes</a></li>
			<li><a href="{{uri_prefix}}/swarm">swarm</a></li>
			<li>Service
				<ul>
					<li><a href="{{uri_prefix}}/services">services</a></li>
					<li><a href="{{uri_prefix}}/services_create">create service</a></li>
				</ul>
			</li>
			<li><a href="{{uri_prefix}}/tasks">tasks</a></li>

        </ul>
    </div>
	<h1  style="text-align: center">{{title}}</h1>
    <hr
        style="width: 80%;
            height: 4px;
            margin-left: auto;
            margin-right: auto;
            background-color:#FF0066;
            color:#FF0066;
            border: 0 none;">

<!-- main area -->
    <div>
{{!main_area}}
    </div>



  </body>
</html>
