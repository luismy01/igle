$(function () {

	var mycollection = new AsistenciaCollection();
	
	var myview = new AsistenciaView({
		collection: mycollection
	});

	var chartView = new ChartView({
		chart: window.chart,
		collection: mycollection
	});

	mycollection.on("add", chartView.addModel, chartView);

	$("#add").click(function(){
		$("#FrmNewAsistencia").modal();
	});

	$("#refresh").click(function(){
		chartView.reload();
	});

	/* idioma por defecto para moment */
	moment.lang("es");

});