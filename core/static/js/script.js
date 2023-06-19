function chose(value, bord, i){
    if (value.classList.contains("he")){
        bord.classList.remove('duvborder')
        value.classList.remove('he')
        i.classList.remove('fa-caret-down')
        i.classList.add("fa-caret-up");
    }
    else{
        bord.classList.add("duvborder");
        value.classList.add("he");
        i.classList.remove('fa-caret-up')
        i.classList.add("fa-caret-down"); 
    }
}

const a = document.getElementById("duvi-a");
const b = document.getElementById("duvi-b");
const ia = document.getElementById("i-a");

a.addEventListener("click", function() {
    chose(b, a, ia)
});

const c = document.getElementById("duvi-c");
const d = document.getElementById("duvi-d");
const ic = document.getElementById("i-c");


c.addEventListener("click", function() {
    chose(d, c, ic)
});

const e = document.getElementById("duvi-e");
const f = document.getElementById("duvi-f");
const ie = document.getElementById("i-e");

e.addEventListener("click", function() {
    chose(f, e, ie)
});

const g = document.getElementById("duvi-g");
const h = document.getElementById("duvi-h");
const ig = document.getElementById("i-g");

g.addEventListener("click", function() {
    chose(h, g, ig)
});

const i = document.getElementById("duvi-i");
const j = document.getElementById("duvi-j");
const ii = document.getElementById("i-i");

i.addEventListener("click", function() {
    chose(j, i, ii)
});
