class MyAdaptorEditInline(object):
    @classmethod
    def can_edit(cls, adaptor_field):
       return True # All user can edit