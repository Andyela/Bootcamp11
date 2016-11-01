<!DOCTYPE html>
<html>
<body>

<p>Type a password and click Enter:</p>

<input id="id1" type="number" max="100">
<button onclick="myFunction()">Enter</button>

<p>If the number is too long an  error message will be dispalyed.</p>

<p id="demo"></p>

<script>
function myFunction() {
    var txt = "";
    if (document.getElementById("id1").validity.rangeOverflow) {
        txt = "Number out of range";
    } else {
        txt = "Successful";
    }
    document.getElementById("demo").innerHTML = txt;
}
</script>

</body>
</html>