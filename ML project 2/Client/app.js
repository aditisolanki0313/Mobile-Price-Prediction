function onPageLoad() {
    console.log("document loaded");

    var url = "http://127.0.0.1:5000/get_mobile_name";

    $.get(url, function (data, status) {
        console.log("got response for get_mobile_name request");
        if (data, status) {
            var Name = data.Name;
            $('#uiName').empty();
            for (var i in Name) {
                var opt = new Option(Name[i]);
                $('#uiName').append(opt);
            }
        }
    });
}
function onClickedEstimatePrice() {
    console.log('Estimaate price button clicked');
    var Name = document.getElementById('uiName');
    var Battery_mAh = document.getElementById('uiBattery');
    var Camera_MP = document.getElementById('uiCamera');
    var Storage_GB_RAM = document.getElementById('uiRAM');
    var Storage_GB_ROM = document.getElementById('uiROM');
    var Display_cm = document.getElementById('uiDisplay');

    var url = "http://127.0.0.1:5000/predict_Price";

    
    $.post(url, {
        Name: Name.value,
        Battery_mAh: Battery_mAh,
        Camera_MP: Camera_MP,
        Storage_GB_RAM: Storage_GB_RAM,
        Storage_GB_ROM: Storage_GB_ROM,
        Display_cm : Display_cm
    }, function (data, status) {

        console.log(data.estimated_Price);
        estprice.innerHTML = data.estimated_Price;
        console.log(status);
    });
}
window.onload = onPageLoad;