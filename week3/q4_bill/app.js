function produceBill() {
    prices = {'HP': 10, 'Nokia': 20, 'Samsung': 30, 'Motorola': 40, 'Apple': 50};
    var total = 0;
    var quantity = 0;
    var brand = document.getElementById('brand').value;
    var quantity = document.getElementById('number').value;

    // check if mobile checkbox is selected
    if (document.getElementById('mobile').checked) {
        total += prices[brand] * quantity * 100;
    }

    // check if laptop checkbox is selected
    if (document.getElementById('laptop').checked) {
        total += prices[brand] * quantity * 1000;
    }
    
    alert('Total amount is ' + total);
}