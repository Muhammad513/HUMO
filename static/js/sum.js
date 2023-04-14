var tds = document.getElementsByTagName('td');
var psum1 = 0;
var psum2 = 0;
var psum3 = 0;
var psum4 = 0;
var psum5 = 0;
var psum6 = 0;
var psum7 = 0;
var psum8 = 0;
var psum9 = 0;
var psum10 = 0;
var psum11 = 0;
var psum12 = 0;
var psum13 = 0;
var psum14 = 0;
var psum15 = 0;
var psum16 = 0;
var psum17 = 0;
var psum18 = 0;


for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'gektar_1') {
        psum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'reja_1') {
        psum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda_1') {
        psum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumda_1') {
        psum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentner_1') {
        psum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilish_1') {
        psum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    
    if(tds[i].className == 'gektar_2') {
        psum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'reja_2') {
        psum8 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda_2') {
        psum9 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumda_2') {
        psum10 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentner_2') {
        psum11 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilish_2') {
        psum12 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }

    if(tds[i].className == 'gektar_3') {
        psum13 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'reja_3') {
        psum14 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda_3') {
        psum15 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumda_3') {
        psum16 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentner_3') {
        psum17 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilish_3') {
        psum18 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    

}

document.getElementById('psumg1').innerHTML=psum1.toFixed(2)                                   
document.getElementById('psumg2').innerHTML=psum2.toFixed(2)                                              
document.getElementById('psumg3').innerHTML=psum3.toFixed(2)
document.getElementById('psumg4').innerHTML=psum4.toFixed(2)
document.getElementById('psumg5').innerHTML=((psum4/psum1)*10).toFixed(2)
document.getElementById('psumg6').innerHTML=(psum4*100/psum2).toFixed(2)
document.getElementById('psumg7').innerHTML=psum7.toFixed(2)                                   
document.getElementById('psumg8').innerHTML=psum8.toFixed(2)                                              
document.getElementById('psumg9').innerHTML=psum9.toFixed(2)
document.getElementById('psumg10').innerHTML=psum10.toFixed(2)
document.getElementById('psumg11').innerHTML=((psum10/psum7)*10).toFixed(2)
document.getElementById('psumg12').innerHTML=(psum10*100/psum8).toFixed(2)
document.getElementById('psumg13').innerHTML=psum13.toFixed(2)                                   
document.getElementById('psumg14').innerHTML=psum14.toFixed(2)                                              
document.getElementById('psumg15').innerHTML=psum15.toFixed(2)
document.getElementById('psumg16').innerHTML=psum16.toFixed(2)
document.getElementById('psumg17').innerHTML=((psum16/psum13)*10).toFixed(2)
document.getElementById('psumg18').innerHTML=(psum16*100/psum14).toFixed(2)

document.getElementById('psumg19').innerHTML=(psum1+psum7+psum13).toLocaleString()
document.getElementById('psumg20').innerHTML=(psum2+psum8+psum14).toLocaleString()
document.getElementById('psumg21').innerHTML=(psum3+psum9+psum15).toLocaleString()
document.getElementById('psumg22').innerHTML=(psum4+psum10+psum16).toLocaleString()
document.getElementById('psumg23').innerHTML=((psum4+psum10+psum16)/(psum1+psum7+psum13)*10).toLocaleString()
document.getElementById('psumg24').innerHTML=((psum4+psum10+psum16)/(psum2+psum8+psum14)*100).toLocaleString()
