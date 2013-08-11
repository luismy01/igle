$(function () {

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


	window.ChartView = Backbone.View.extend({

		defaults: {
			collection: new Backbone.Collection()
		},

		initialize: function(){
			_.bindAll(this, 'render');
			this.collection.on("change", this.render, this);
			this.collection.on("remove", this.render, this);
		},

		render: function() {

			console.log("render chart")

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

			window.chart.xAxis[0].setCategories(categories);

			window.chart.series[0].setData(data0);
			window.chart.series[1].setData(data1);
			window.chart.series[2].setData(data2);
			window.chart.series[3].setData(data3);
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
	    	console.log("render list");
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
	    	"click .delete": "deleteAsistencia"
	    },

	    initialize: function () {
	        this.model.on("change", this.render, this);
	        this.model.on("destroy", this.close, this);
	    },

	    render: function (eventName) {
	        $(this.el).html(this.template(this.model.toJSON()));
	        return this;
	    },

	    deleteAsistencia: function () {
	        var self = this

			console.log("model is new? " + this.model.isNew());

	        this.model.destroy({
	            success: function () {
	            	app.asistList.remove(self.model)
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
	    },

	    render: function () {
	        return this;
	    },

	    events:{
	        "change input":"change",
	        "click #save":"saveAsistencia",
	    },

	    change: function (event) {
	        var target = event.target;
	        console.log('changing ' + target.id + ' from: ' + target.defaultValue + ' to: ' + target.value);
	        // You could change your model on the spot, like this:
	        // var change = {};
	        // change[target.name] = target.value;
	        // this.model.set(change);
	    },

	    saveAsistencia: function () {
	        
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
	            app.asistList.create(this.model, {
	                success: function () {
	                    console.log("new model added");
	                    $("#FrmNewAsistencia").modal("hide");
	                    $("#form-asist").reset();
	                }
	            });
	        } else {
	            this.model.save();
	        }

	        return false;
	    },

	    close: function () {
	        $(this.el).off();
	        $("#FrmNewAsistencia").modal('hide');
	    }
	});


	window.ToolBarView = Backbone.View.extend({
		
		el: $("body"),

	    initialize:function () {
	        this.render();
	    },

	    render:function (eventName) {
	        return this;
	    },

	    events: {
	        "click #add": "newAsistencia",
	        "click #refresh": "listAsistencia"
	    },

	    newAsistencia:function (event) {
	        app.navigate("!");
	        app.navigate("new", true);
	        return false;
	    },

	    listAsistencia: function(event) {
	    	app.navigate("!");
	    	app.navigate("list", true);
	        return false;	
	    }

	});

	window.AppRouter = Backbone.Router.extend({

	    routes:{
	        "":"list",
	        "list":"list",
	        "new":"newAsistencia",
	        ":id":"wineDetails"
	    },

	    initialize: function () {
	        var toolbarView = new ToolBarView();
	        this.asistList = new AsistenciaCollection()
	    },

	    list: function () {
	        this.asistList = new AsistenciaCollection();
	        var self = this;
	        this.asistList.fetch({
	            success: function () {
	                self.listView = new AsistenciaListView({collection:self.asistList});
	                self.listView.render()
	                
					self.chartView = new ChartView({collection:self.asistList});
	                self.chartView.render();

	            }
	        });
	    },

	    wineDetails: function (id) {
	        if (this.wineList) {
	            this.wine = this.wineList.get(id);
	            if (this.asistenciaView) this.asistenciaView.close();
	            this.asistenciaView = new AsistenciaView({model:this.wine});
	            $('#content').html(this.asistenciaView.render().el);
	        } else {
	            this.requestedId = id;
	            this.list();
	        }
	    },

	    newAsistencia: function () {
	        if (app.asistenciaView) app.asistenciaView.close();
	        app.asistenciaView = new AsistenciaView({model:new Asistencia()});
	        $("#FrmNewAsistencia").modal("show");
	    }

	});

	window.app = new AppRouter();
	Backbone.history.start();

});