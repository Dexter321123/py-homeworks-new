def check_file(file):
    def_result = dict()
    file_result = dict()

    file_data = file.read()
    file_info = chardet.detect(file_data)
    file_encoding = file_info['encoding']

    def_result['data'] = file_data
    def_result['info'] = file_info
    def_result['encoding'] = file_encoding
    file_result['data'] = file_data
    file_result['info'] = file_info
    file_result['encoding'] = file_encoding

    return def_result
    return file_result


def read_xml_and_convert(file_path, file_name):
    def_result = dict()
    xml_result = dict()
    xml_result[file_name] = list()

    with open(file_path + file_name, 'rb') as f:
        file = check_file(f)
@@ -29,13 +30,14 @@ def read_xml_and_convert(file_path, file_name):
            result_dict['title'] = item.find('title').text
            result_dict['description'] = item.find('description').text

            def_result[file_name] = result_dict
            xml_result[file_name] += [result_dict]

    return def_result
    return xml_result


def read_json_and_convert(file_path, file_name):
    def_result = dict()
    json_result = dict()
    json_result[file_name] = list()

    with open(file_path + file_name, 'rb') as f:
        file = check_file(f)
@@ -47,6 +49,6 @@ def read_json_and_convert(file_path, file_name):
            result_dict['title'] = item['title']
            result_dict['description'] = item['description']

            def_result[file_name] = result_dict
            json_result[file_name] += [result_dict]

    return def_result
    return json_result
