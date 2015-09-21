
$(function() {
	
	app.personas = new app.Personas();

	app.personaListView = new app.PersonaListView({
		el: $("#content"),
		collection: app.personas
	});

	app.personaListView.render();

	//app.personas.fetch();
		
	app.router = new app.PersonaRouter();
	Backbone.history.start();
	
});