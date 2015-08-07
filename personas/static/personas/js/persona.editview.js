app.PersonaEditView = Backbone.View.extend({

	className: "container-fluid",
	template: _.template( $("#persona-edit-template").html() ),

	initialize: function (options) {
		this.router = options.router;
	},

	render: function () {

		var html = this.template(this.model.attributes);
		this.$el.html( html );
		this.$(".fecha_nacimiento").attr("placeholder", moment().format("D [de] MMMM [de] YYYY"));

		this.$(".fecha_nacimiento").datetimepicker({
	      format: "DD/MM/YYYY",
	      locale: moment.locale('es'),
	      showTodayButton: true
	    });

		if (this.model.has("fecha_nacimiento")) {
	    	var m = moment(this.model.get("fecha_nacimiento"));
	    	this.$(".fecha_nacimiento").data("DateTimePicker").date(m);
	    }

		return this;
	},

	events: {
		"click #TipoIdentificacion a": "updateTipoIdentificacion",
		"keyup .nombre": "updateNickname",
		"click .btn-guardar": "save",
		"click .chk-habilitar": "habilitar",
	},

	updateTipoIdentificacion: function(evt) {
      
		var $a = $(evt.currentTarget);
		this.$("button.identificacion_descripcion").text($a.text());
		this.$("button.identificacion_descripcion").data("tipo", $a.data("tipo"));

    },

    updateNickname: function() {

    	var nombre = this.$(".nombre").val().split(" ")[0];
    	this.$(".nickname").text(nombre);

    },

    save: function() {

    	var m = $(".fecha_nacimiento").data("DateTimePicker").date();
    	var fecha_nac = (m === null) ? null : m.format("YYYY-MM-DD");
    	var checked = this.$(".chk-habilitar").hasClass("active") ? false : true;

    	this.model.set({
    		nombre: this.$(".nombre").val(),
			identificacion_tipo: this.$(".identificacion_descripcion").data("tipo"), // CC, TI, PS
			identificacion_descripcion: this.$(".identificacion_descripcion").val(),
			identificacion_codigo: this.$(".identificacion_codigo").val(),
			congregacion: this.$(".congregacion").val(),
			fecha_nacimiento: fecha_nac,
			email: this.$(".email").val(),
			celular: this.$(".celular").val(),
			genero: this.$("input[name='options']:checked").val(),
			habilitado: checked,
    	});

		this.model.save();
    	this.collection.add(this.model);

    	this.router.navigate("listado", {trigger: true});

    },

    habilitar: function(evt) {

    	var labelCheckbox = $(evt.currentTarget);
    	var checked = labelCheckbox.hasClass("active") ? false : true;
    	var text = checked ? "Deshabilitado" : "Deshabilitar";

    	labelCheckbox.text(text);
    	this.model.set({habilitado: checked });

    },
    
});