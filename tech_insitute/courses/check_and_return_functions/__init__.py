from django.db import transaction

@transaction.atomic
def check_field_data_same(check_obj, save_obj, fieldnames, values):
    if type(fieldnames) == list:
        for field, value in zip(fieldnames, values):
            field_data = getattr(check_obj, field)
            if field_data != value:
                setattr(save_obj, field, value)
                save_obj.save()
        return True
    else:
        field_data = getattr(check_obj, fieldnames)
        if field_data != values:
            setattr(save_obj, fieldnames, values)
            save_obj.save()
        return True