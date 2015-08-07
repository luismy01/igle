app.Personas = Backbone.Collection.extend({
	model: app.Persona,
	localStorage: new Backbone.LocalStorage("personas")
});