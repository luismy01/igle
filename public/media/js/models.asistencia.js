$(function () {

	AsistenciaModel = Backbone.Model.extend({
		defaults: {
			fecha: '20130807',
			hermanos: 0,
			visitas: 0,
			ninos: 0,
			adolescentes: 0,
			observaciones: ''
		}
	});	

	AsistenciaCollection = Backbone.Collection.extend({
		model: AsistenciaModel,
		url: '/asistencia/list'
	});

	AsistenciaView = Backbone.View.extend({
		
		el: $("#FrmNewAsistencia"),

		defaults: {
			collection: new AsistenciaCollection()
		},

		initialize: function(){
			_.bindAll(this, 'render', 'addModel');

			this.collection.on("change", this.render, this);
			this.collection.on("add", this.render, this);
		},

		render: function() {},

		events: {
			'click button#save': "addModel",
			'click button#refresh': "loadModels"
		},

		addModel: function(){
			this.collection.create({
				fecha: $("txt-fecha").val(),
				hermanos: $("txt-hermanos").val(),
				visitas: $("txt-visitas").val(),
				ninos: $("txt-ninos").val(),
				adolescentes: $("txt-adolescentes").val()
			});
		},

		loadModels: function(){
			alert("do it refresh");
		}

	});

	ChartView = Backbone.View.extend({

		defaults: {
			chart: window.chart,
			collection: new AsistenciaCollection()
		},

		initialize: function(){
			_.bindAll(this, 'render');
		},

		render: function() {

			var categories = new Array();

			this.collection.each(function(asistencia, i) {
				window.chart.series[0].addPoint(asistencia.get("hermanos"));
				window.chart.series[1].addPoint(asistencia.get("visitas"));
				window.chart.series[2].addPoint(asistencia.get("ninos"));
				window.chart.series[3].addPoint(asistencia.get("adolescentes"));
				//categories[i] = moment(asistencia.get("fecha")).format("MMM, YYYY");
				categories[i] = asistencia.get("fecha");
			})

			window.chart.xAxis[0].setCategories(categories);
		},

		reload: function() {
			this.collection.fetch({
				success: this.render
			});
		}

	});

});