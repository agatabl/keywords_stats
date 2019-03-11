# Keywords stats

Prosta aplikacja webowa analizująca liczbę wystąpnień słowa kluczowego w treści strony. 

Aplikacja Keyword stats przyjmuje od użytkownika adres URL i wyświetla informację ile razy każde 
słowo kluczowe zdefiniowane w headzie strony występuje w 
jej treści. 

W przypadku braku słów kluczowych aplikackacja informuje o tym użytkownika.
Jeśli podany adres nie istnieje aplikackacja informuje o tym użytkownika (błąd 404).
W przypadku wystąpnienia innego błędu użytkownik otrzymuje ogólny komunikat o nieprawidłowościach oraz możliwość powrotu do strony głównej.

Aplikacja napisana została w języku Python 3.6.5 z wykorzystaniem frameworka Flask 1.0.2. 


__________________________________________________________________________________________________
ENG

Simple Flask app for counting keywords on websites.

Interface asks user for an URL and analyze the wbsite in terms of occurence of keywords defined in website's head.

If there are no keywords defined, user gets a proper response.
If given website doesn't exist, user gets a proper response - error 404.
In case of any other problem (ex. invalid url, lacking schema) user gets a general error message and 'Go home' button.

Technology: 
- Python 3.6.5
- Flask 1.0.2
 
 
