# DRF-browsable-API-GET-support
A project containing a few pieces of code to get people the opportunity to have a GET form in DRF's browsable API pages.

DRF by default only offers 4 form in DRF admin panel - for methods POST,
PUT, PATCH and DELETE, and many developers suffer because of that, when they want to just have a ready-to-use 
page to show how they can use their API.

## Things to know
This is a very raw project, it's more like notes, so it's not really conveniently to use it, 
but I'm lazy to make it a kind of package or a ready-to-install app whatever.
Mb in the future, but idk.

## Usage
* Put somewhere the GETFormBrowsableAPIRenderer class from `renderers.py` (I suggest copying the whole file, it's already called properly)
* Put somewhere the `browsable-api-template.html` file (to a template dir, for example `<proj_root>/templates`, 
  django will find it there)
* Point DRF to use the renderer class. You can do it either:
    * globally, in settings, 
        ```python
        REST_FRAMEWORK = {
            # ...,
            'DEFAULT_RENDERER_CLASSES': [
                'rest_framework.renderers.JSONRenderer',
                '<path>.<to>.<file>.<called>.<renderers>.GETFormBrowsableAPIRenderer',
            ],
            # ...,
        }
        ```
    * or per-view like 
        ```python
        class HelloView(APIView):
            renderer_classes = [JSONRenderer, GETFormBrowsableAPIRenderer]
        ```
        or 
        ```python
        @action(detail=True, methods=['get', 'post'], renderer_classes=[JSONRenderer, GETFormBrowsableAPIRenderer])
        ```