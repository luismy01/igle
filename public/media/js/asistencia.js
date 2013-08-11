
$(function () {

	/* idioma por defecto para moment */
	moment.lang("es");
/*
	var mycollection = new AsistenciaCollection();
	
	var myview = new AsistenciaVieww({
		collection: mycollection
	});

	var chartView = new ChartView({
		chart: window.chart,
		collection: mycollection
	});

	mycollection.on("add", chartView.addModel, chartView);

	$("#refresh").click(function(){
		chartView.reload();
	});
*/

	$('#tabs a').click(function (e) {
	  e.preventDefault();
	  $(this).tab('show');
	});

});