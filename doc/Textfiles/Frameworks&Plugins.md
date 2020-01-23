### Bootstrap
 - Bootstrap is een gratis open source CSS framework oorspronkelijk ontwikkeld voor intern gebruik door de ontwikkelaars van Twitter. Het framework heeft standaard al een boel standaard functies waardoor het ontwikkelen van een responsive website zeer snel gaat.
 - In layout.html (uit Finance)
 - http://getbootstrap.com/docs/4.1/
 - https://bootswatch.com/
 - https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css
 
### Flask

[Flask](https://flask.palletsprojects.com/) is een webraamwerk dat tools, bibliotheken en technologieën biedt die geschikt zijn om een webapplicatie te bouwen. Deze webapplicatie kan komen in de vorm van webpagina's, blogs, of zelfs een uitgebreide webgebaseerde agenda-app of een commerciële site.
Flask is een van de beste [micro-frameworks](https://en.wikipedia.org/wiki/Microframework), omdat het weinig tot geen afhankelijkheden heeft van externe bibliotheken.

- Uit application.py (in Finance)
	>from flask import Flask, flash, jsonify, redirect, 
	render_template, request, session
	from flask_session import Session
	
### Socket.io

Socket.IO is een JavaScript-bibliotheek voor realtime webapplicaties. Het maakt realtime bidirectionele communicatie tussen webclients en servers mogelijk.

- Kan misschien pop-ups genereren, push meldingen versturen naar de gebruikers.
- A.s. vrijdag 17 januari meer over vragen aan begeleiders.

### tempfile

This module creates temporary files and directories.
It works on all supported platforms.
TemporaryFile, NamedTemporaryFile, TemporaryDirectory, and SpooledTemporaryFile are
high-level interfaces which provide automatic cleanup and can be used as context managers.
mkstemp() and mkdtemp() are lower-level functions which require manual cleanup.
We used mkdtemp().

### Datetime.now
- Genereert de datum van het moment van spelen van de trivia game
- Voor de datum in de leaderboards
- In application.py (uit Finance)

### Chart.js
Chart.js is een gratis open-source JavaScript-bibliotheek voor gegevensvisualisatie, die 8 grafiektypen ondersteunt: balk, lijn, gebied, taart (donut), bubbel, radar, polair en spreiding. Gecreëerd door de Londense webontwikkelaar Nick Downie in 2013, wordt het nu onderhouden door de gemeenschap en is het de tweede meest populaire JS-kaartbibliotheek op GitHub op basis van het aantal sterren na D3.js, dat als aanzienlijk gemakkelijker te gebruiken wordt beschouwd, maar minder aanpasbaar is dan de laatste. Chart.js wordt weergegeven in HTML5 canvas en wordt algemeen behandeld als een van de beste datavisualisatiebibliotheken. Het is beschikbaar onder de MIT-licentie.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEyODA4NjIxM119
-->