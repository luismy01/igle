$(function () {

	window.asistenciaChart = new Highcharts.Chart({
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

	window.Asistencia = Backbone.Model.extend({
		defaults: {
			fecha: '20130807',
			hermanos: 0,
			visitas: 0,
			ninos: 0,
			adolescentes: 0,
			ofrenda: 0,
			observaciones: ''
		},

		initialize: function() {}

	});	

	window.AsistenciaCollection = Backbone.Collection.extend({
		model: Asistencia,
		url: '/asistencia/',

		initialize: function() {},

		comparator: function (model) {
			return model.get("fecha");
		}

	});


	window.AsistenciaChartView = Backbone.View.extend({

		defaults: {
			collection: new Backbone.Collection(),
			chart: window.asistenciaChart
		},

		initialize: function(){
			_.bindAll(this, 'render');
			this.collection.on("change", this.render, this);
			this.collection.on("remove", this.render, this);
		},

		render: function() {

			var categories = new Array();
			var data0 = new Array();
			var data1 = new Array();
			var data2 = new Array();
			var data3 = new Array();

			this.collection.each(function(asistencia, i) {

				categories[i] = asistencia.get("fecha");

				data0[i] = asistencia.get("hermanos");
				data1[i] = asistencia.get("visitas");
				data2[i] = asistencia.get("ninos");
				data3[i] = asistencia.get("adolescentes");

			})

			asistenciaChart.xAxis[0].setCategories(categories);

			asistenciaChart.series[0].setData(data0);
			asistenciaChart.series[1].setData(data1);
			asistenciaChart.series[2].setData(data2);
			asistenciaChart.series[3].setData(data3);

			return this;
		},

		reload: function() {
			this.collection.fetch({
				success: this.render
			});
		}

	});

	window.AsistenciaListView = Backbone.View.extend({

	    el: $("#tabla-body"),

	    initialize: function () {
	    	var self = this;
	        this.collection.on("change", this.render, this);
	        this.collection.on("remove", this.render, this);
	    },

	    render: function () {	    	
	    	
	    	$(this.el).html("");
	        _.each(this.collection.models, function (asist) {
	            $(this.el).append(new AsistenciaListItemView({model:asist}).render().el);
	        }, this);
	        
	        return this;
	    }

	});

	window.AsistenciaListItemView = Backbone.View.extend({

	    tagName: "tr",

	    template: _.template($('#tpl-asist-list-item').html()),

	    events: {
	    	"click .btn-edit": "edit",
	    	"click .btn-delete": "delete"
	    },

	    initialize: function () {
	        this.model.on("change", this.render, this);
	        this.model.on("destroy", this.close, this);
	    },

	    render: function (eventName) {
	        $(this.el).html(this.template(this.model.toJSON()));
	        return this;
	    },

	    delete: function () {
	        var self = this

	        this.model.destroy({
	            success: function () {
	            	app.asistencias.remove(self.model)
	            	console.log("model deleted")
	            },

	            error: function() {
	            	alert('Error Borrar');
	            }

	        }, {wait: true});
	        return false;
	    },

	    close: function () {
	        $(this.el).off();
	        $(this.el).remove();
	    }

	});

	window.AsistenciaView = Backbone.View.extend({

		el: $("#FrmNewAsistencia"),

		defaults: {
			model: new Backbone.Model()
		},

	    initialize: function () {
	        this.model.on("change", this.render, this);

	        this.$el.on("hide.bs.modal", function() {
				app.navigate("#");
			});

	    },

	    render: function () {
	        return this;
	    },

	    events:{
	    	"click #save": "save",
	    },

	    add: function() {

			$("#txt-fecha").val("");
			$("#txt-hermanos").val("");
			$("#txt-visitas").val("");
			$("#txt-ninos").val("");
			$("#txt-adolescentes").val("");
			$("#txt-ofrenda").val("");
			$("#txt-obs").val("");

	    	this.$el.modal("show");
	    },

	    edit: function() {

			$("#txt-fecha").val(this.model.get("fecha"));
			$("#txt-hermanos").val(this.model.get("hermanos"));
			$("#txt-visitas").val(this.model.get("visitas"));
			$("#txt-ninos").val(this.model.get("ninos"));
			$("#txt-adolescentes").val(this.model.get("adolescentes"));
			$("#txt-ofrenda").val(this.model.get("ofrenda"));
			$("#txt-obs").val(this.model.get("observaciones"));

	    	this.$el.modal("show");
	    },

	    save: function () {
	        
	        this.model.set({
				fecha: $("#txt-fecha").val(),
				hermanos: parseInt($("#txt-hermanos").val()),
				visitas: parseInt($("#txt-visitas").val()),
				ninos: parseInt($("#txt-ninos").val()),
				adolescentes: parseInt($("#txt-adolescentes").val()),
				ofrenda: parseInt($("#txt-ofrenda").val()),
				observaciones: $("#txt-obs").val()
			});

	        if (this.model.isNew()) {
	            var self = this;
	            app.asistencias.create(this.model, {
	                success: function () {
	                    self.close();
	                }
	            });
	        } else {
	        	var self = this;
	            this.model.save({},{
	            	success: function() {
	            		self.close();
	            	}
	            });
	        }

	        return false;
	    },

	    close: function () {
	        this.$el.off();
	        this.$el.modal('hide');
	    }
	});

	window.AsistenciaDeleteView = Backbone.View.extend({

		el: $("#AsistenciaDeleteView"),

		template: _.template($('#tpl-delete-asist').html()),

		defaults: {
			model: new Backbone.Model()
		},

	    initialize: function () {
	        this.model.on("change", this.render, this);

	        this.$el.on("hide.bs.modal", function() {
				app.navigate("#");
			});

	    },

	    render: function () {
	    	$(".modal-body", this.el).html(this.template(this.model.toJSON()));
	    	$("#AsistenciaDeleteView").modal('show');
	        return this;
	    },

	    events:{
	    	"click #btn-delete":"delete",
	    },

	    delete: function() {

	    	var self = this;
	        this.model.destroy({
	            success: function () {
	            	app.asistencias.remove(self.model);
	            	self.close();
	            },

	            error: function() {
	            	alert('Error Borrar');
	            }

	        }, {wait: true});

	    },

	    close: function () {
	        this.$el.off();
	        this.$el.modal('hide');
	    }
	});


	window.AppRouter = Backbone.Router.extend({

	    routes: {
	        "":"refresh",
	        "list":"refresh",
	        "refresh":"refresh",
	        "new":"addAsistencia",
	        "add":"addAsistencia",
	        "edit/:date": "editAsistencia",
	        "delete/:date": "deleteAsistencia"
	    },

	    initialize: function () {
	        this.asistencias = new AsistenciaCollection()
	    },

	    refresh: function (evt) {
	        this.asistencias = new AsistenciaCollection();
	        var self = this;
	        this.asistencias.fetch({
	            success: function () {
	                self.listView = new AsistenciaListView({collection:self.asistencias});
	                self.listView.render()
	                
					self.chartView = new AsistenciaChartView({collection:self.asistencias, chart: window.asistenciaChart});
	                self.chartView.render();

	                if (evt) {

	                	if (evt.edit) self.editAsistencia(evt.fecha);
	                	else if (evt.delete) self.deleteAsistencia(evt.fecha);

	                }

	                self.navigate("");
	            }
	        });
	    },

	    addAsistencia: function () {
	        if (app.asistenciaView) app.asistenciaView.close();
	        app.asistenciaView = new AsistenciaView({model:new Asistencia()});
	        app.asistenciaView.add();
	    },

	    editAsistencia: function (fecha) {
	    	
	    	if (this.asistencias.length == 0) {
		    	this.refresh({fecha: fecha, edit:true});
		    }

	    	_.each(this.asistencias.models, function (asist) {
	            
	    		if (asist.get("fecha") == fecha) {

					if (app.asistenciaView) app.asistenciaView.close();
				    app.asistenciaView = new AsistenciaView({model:asist});
				    app.asistenciaView.edit();
				    return;
	    		}

	        }, this);

		},

	    deleteAsistencia: function (fecha) {

	    	if (this.asistencias.length == 0) {
		    	this.refresh({fecha: fecha, delete:true});
		    }

	    	_.each(this.asistencias.models, function (asist) {
	            
	    		if (asist.get("fecha") == fecha) {
					if (app.asistenciaDeleteView) app.asistenciaDeleteView.close();
				    app.asistenciaDeleteView = new AsistenciaDeleteView({model:asist});
				    app.asistenciaDeleteView.render();
				    return;
	    		}

	        }, this);

	    }

	});

	var oldFunction = Backbone.sync;
	Backbone.sync = function (method, model, options) {
		if (method == "update") method = "create";
		return oldFunction(method, model, options);
	};

	/* idioma por defecto para moment */
	moment.lang("es");

	window.app = new AppRouter();
	Backbone.history.start();

});