from pydantic import ValidationError


def validate(model, data):
    try:
        model.parse_obj(data)
        return True
    except ValidationError as e:
        raise ValueError(str(e))