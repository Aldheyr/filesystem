

def validate_nomenclatura(name_instance):
    instance = name_instance.lower()

    # ambiente
    ambiente = 'Indefinido'

    if 'desa' in instance:
        ambiente = 'desa'
    elif 'test' in instance:
        ambiente = 'test'
    elif 'prod' in instance:
        ambiente = 'prod'


    # proyecto
    proyecto = ''
    service = 'rds'
    type_service = 'dba'


    abrev_region = ""
    regionsplit = region.split('-')
    for item in regionsplit:
        abrev_region += item[0]

    nomenclatura_region = False
    nomenclatura_type_service = False
    nomenclatura_ambiente = False
    nomenclatura_service = False
    nomenclatura_correlativo = False

    if not proyecto:

        if instance[:3] in abreviatura_region:
            nomenclatura_region = True

            if type_service == instance[3:6]:
                nomenclatura_type_service = True

                if ambiente == instance[6:10]:
                    nomenclatura_ambiente = True

                    if service == instance[10:13]:
                        nomenclatura_service = True

                        correlativo = ''
                        name_proyecto = ''
                        for number in instance[13:]:
                            if number.isdigit():
                                correlativo += number
                            else:
                                if not correlativo:
                                    name_proyecto += number

    if nomenclatura_region and nomenclatura_type_service and nomenclatura_ambiente and nomenclatura_service:
        proyecto = name_proyecto

    return proyecto


def validate_tags(tagList):

    the_tags = []
    response = False
    tags_obligatorias = ["AMBIENTE", "ENTORNO", "NAME", "PROYECTO", "RESPONSABLE"]

    for tag in tagList:

        if tag.get('key') == 'AMBIENTE':
            tags_obligatorias.remove('AMBIENTE')
            the_tags.append({
                'AMBIENTE': tag.get('value')
            })

        if tag.get('key') == 'ENTORNO':
            tags_obligatorias.remove('ENTORNO')
            the_tags.append({
                'ENTORNO': tag.get('value')
            })

        if tag.get('key') == 'NAME':
            tags_obligatorias.remove('NAME')
            the_tags.append({
                'NAME': tag.get('value')
            })

        if tag.get('key') == 'PROYECTO':
            tags_obligatorias.remove('PROYECTO')
            the_tags.append({
                'PROYECTO': tag.get('value')
            })

        if tag.get('key') == 'RESPONSABLE':
            tags_obligatorias.remove('RESPONSABLE')
            the_tags.append({
                'RESPONSABLE': tag.get('value')
            })

    for tag in tags_obligatorias:
        response = True
        the_tags.append({
            tag: ""
        })

    return response
