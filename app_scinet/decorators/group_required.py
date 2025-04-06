from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Sprawdzamy czy użytkownik jest zalogowany i należy do odpowiedniej grupy
            if request.user.is_authenticated and request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            # Dodajemy komunikat i przekierowujemy (np. do strony głównej)
            messages.warning(request, "Nie masz dostępu do tej sekcji!")
            return redirect("home")  # <- zmień na nazwę twojej strony
        return _wrapped_view
    return decorator
