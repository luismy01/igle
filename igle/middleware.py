from django.utils import translation
from django.conf import settings

LANGUAGE_PARAM = "lang"

class ChangeLaguageMiddleware(object):

	current_language = translation.get_language()
	user_language = ""

	def process_request(self, request):

		if LANGUAGE_PARAM in request.GET:

			self.user_language = request.GET[LANGUAGE_PARAM]

			if self.user_language:

				for lang in settings.LANGUAGES:

					if lang[0] == self.user_language:
						translation.activate(self.user_language)
						request.session[translation.LANGUAGE_SESSION_KEY] = self.user_language

		return None

	def process_response(self, request, response):
		
		response.set_cookie(settings.LANGUAGE_COOKIE_NAME, self.user_language)

		return response


