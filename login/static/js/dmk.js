var tds = document.getElementsByTagName('td');
console.log(tds)
var dmkreja = 0;
var dmkxak = 0;
var zavodreja = 0;
var zavodxak = 0;

for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'dreja') {
        dmkreja += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'dxak') {
        dmkxak += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'zavodreja') {
        zavodreja += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'zavodxak') {
        zavodxak += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}

document.getElementById('sumreja').innerHTML=dmkreja.toFixed(2)                                   
document.getElementById('sumxak').innerHTML=dmkxak.toFixed(2)                                              
document.getElementById('jamireja').innerHTML=(dmkreja+zavodreja).toFixed(2)
document.getElementById('jamixak').innerHTML=(dmkxak+zavodxak).toFixed(2)
