$(function () {

    window.chart = new Highcharts.Chart({
            chart: {
                renderTo: 'lineChart',
                type: 'line'
            },
            title: {
                text: 'Asistencia a la Escuela Dominical'
            },
            subtitle: {
                text: 'IPUC - Veinte de Julio'
            },
            xAxis: {
                type: "datetime"
            },
            yAxis: {
                title: {
                    text: 'Asistencia'
                }
            },
            tooltip: {
                enabled: true,
                useHTML: true,
                formatter: function() {
                    var txt = '<div class="container">' +
                        '<div class="row">' +
                          '<div class="span10">' +
                            moment(this.x).format("dddd, DD [de] MMMM [de] YYYY") + '<br/>'

                    var total = 0;
                    $.each(this.points, function(i, point) {
                        txt += '<br/> <b>' + point.series.name + '</b>: ' + point.y + ' personas'
                        total += point.y
                    });
                    
                    txt += '<br/><br/> <b>Total</b>: ' + total + ' personas'
                        + '</div>' + '</div>';

                    return txt;
                },
                shared: true
            },
            plotOptions: {
                line: {
                    dataLabels: {
                        enabled: true
                    },
                    enableMouseTracking: true
                }
            },
            series: [{
                name: 'Hermanos',
                data: []
            }, {
                name: 'Visitas',
                data: []
            }, {
                name: 'Ninos',
                data: []
            }, {
                name: 'Adolescentes',
                data: []
            }]
    });

});