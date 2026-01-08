import django
from django.template.context import Context

def patch_jazzmin_context():
    """
    Patch to fix Jazzmin compatibility with Django 5.0+ / 6.0
    The error "AttributeError: 'super' object has no attribute 'dicts'" occurs
    because Jazzmin tries to access .dicts which was removed or changed in recent Django versions.
    """
    if django.VERSION >= (5, 0):
        def _get_dicts(self):
            # For Django 5.0+, the context stack is managed differently.
            # We try to expose the data in a way Jazzmin expects, vaguely.
            # Context is a list of dicts effectively.
            return [d for d in self] 
        
        # We can't easily monkeypatch 'dicts' property if it doesn't exist on parent.
        # But the error happens in __copy__ of Context where it calls self.dicts[:]
        # Wait, the traceback says: `duplicate.dicts = self.dicts[:]` in `django.template.context.py`.
        # This means Django's OWN code is trying to access .dicts?
        # NO, the traceback showed the error IN Django's code.
        # Exception Location: ...django\template\context.py, line 39, in __copy__
        # This implies 'super()' (BaseContext) issue.
        pass

# Actually, the traceback indicated the error is INSIDE django.template.context.py
# line 39, in __copy__: duplicate.dicts = self.dicts[:]
# And the error is 'super' object has no attribute 'dicts'.
# This suggests that Context.__copy__ is calling super() (which returns a BaseContext)
# AND trying to access .dicts on it, OR self.dicts doesn't exist?

# The traceback says:
# File "django\template\context.py", line 158, in __copy__
#    duplicate = super().__copy__()
# File "django\template\context.py", line 39, in __copy__
#    duplicate.dicts = self.dicts[:]
# Exception Value: 'super' object has no attribute 'dicts' ...

# This typically happens if `Context` usage is mixed with something that breaks the MRO or initialization.
# Given the complexity, downgrading to Django 4.2 LTS is safer and faster.
