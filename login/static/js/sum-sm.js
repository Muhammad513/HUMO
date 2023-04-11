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
    if(tds[i].className == 'gektarsm_1') {
        psum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'rejasm_1') {
        psum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkundasm_1') {
        psum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumdasm_1') {
        psum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentnersm_1') {
        psum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilishsm_1') {
        psum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    
    if(tds[i].className == 'gektarsm_2') {
        psum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'rejasm_2') {
        psum8 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkundasm_2') {
        psum9 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumdasm_2') {
        psum10 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentnersm_2') {
        psum11 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilishsm_2') {
        psum12 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }

    if(tds[i].className == 'gektarsm_3') {
        psum13 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'rejasm_3') {
        psum14 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkundasm_3') {
        psum15 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumdasm_3') {
        psum16 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentnersm_3') {
        psum17 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilishsm_3') {
        psum18 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    

}

document.getElementById('psumg1sm').innerHTML=psum1.toFixed(2)                                   
document.getElementById('psumg2sm').innerHTML=psum2.toFixed(2)                                              
document.getElementById('psumg3sm').innerHTML=psum3.toFixed(2)
document.getElementById('psumg4sm').innerHTML=psum4.toFixed(2)
document.getElementById('psumg5sm').innerHTML=((psum4/psum1)*10).toFixed(2)
document.getElementById('psumg6sm').innerHTML=(psum4*100/psum2).toFixed(2)
document.getElementById('psumg7sm').innerHTML=psum7.toFixed(2)                                   
document.getElementById('psumg8sm').innerHTML=psum8.toFixed(2)                                              
document.getElementById('psumg9sm').innerHTML=psum9.toFixed(2)
document.getElementById('psumg10sm').innerHTML=psum10.toFixed(2)
document.getElementById('psumg11sm').innerHTML=((psum10/psum7)*10).toFixed(2)
document.getElementById('psumg12sm').innerHTML=(psum10*100/psum8).toFixed(2)
document.getElementById('psumg13sm').innerHTML=psum13.toFixed(2)                                   
document.getElementById('psumg14sm').innerHTML=psum14.toFixed(2)                                              
document.getElementById('psumg15sm').innerHTML=psum15.toFixed(2)
document.getElementById('psumg16sm').innerHTML=psum16.toFixed(2)
document.getElementById('psumg17sm').innerHTML=((psum16/psum13)*10).toFixed(2)
document.getElementById('psumg18sm').innerHTML=(psum16*100/psum14).toFixed(2)

document.getElementById('psumg19sm').innerHTML=(psum1+psum7+psum13).toLocaleString()
document.getElementById('psumg20sm').innerHTML=(psum2+psum8+psum14).toLocaleString()
document.getElementById('psumg21sm').innerHTML=(psum3+psum9+psum15).toLocaleString()
document.getElementById('psumg22sm').innerHTML=(psum4+psum10+psum16).toLocaleString()
document.getElementById('psumg23sm').innerHTML=((psum4+psum11+psum18)/(psum1+psum8+psum15)*10).toLocaleString()
document.getElementById('psumg24sm').innerHTML=((psum4+psum11+psum18)/(psum2+psum9+psum16)*100).toLocaleString()
