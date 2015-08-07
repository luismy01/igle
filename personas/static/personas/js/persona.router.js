app.PersonaRouter = Backbone.Router.extend({
	routes: {
		"listado": "listado",
		"agregar": "agregar",
		"persona/:numero/editar": "editar",
		"persona/:numero/ver": "detalle",

		"*actions": "listado",
	},

	initialize: function() {
		this.view = new Backbone.View();
	},

	listado: function() {

		this.view = new app.PersonaListView({
			el: $("#content"),
			collection: app.personas
		});

		this.view.render();
		
	},

	agregar: function() {

		var view = new app.PersonaEditView({
			model: new app.Persona,
			collection: app.personas,
			router: app.router
		});

		$("#content").html( view.render().el );

	},

	editar: function(numero) {
		var persona = app.personas.findWhere({identificacion_codigo: numero});

		var view = new app.PersonaEditView({
			model: persona,
			collection: app.personas,
			router: app.router
		});

		$("#content").html( view.render().el );
	},

	detalle: function(numero) {
		var persona = app.personas.findWhere({identificacion_codigo: numero});

		var view = new app.PersonaDetailView({
			el: $("#content"),
			model: persona,
			collection: app.personas,
			router: app.router
		});

		view.render();

	},

});