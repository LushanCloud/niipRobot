def process_search_ocr(result):
    # 移除包含关键字 "search" 的元素的前缀 "search "
    search_ocr = [element.replace("search ", "") for element in result if "search" in element]
    # 将结果中的英文文本全部转换为小写
    search_ocr = [item.lower() for item in search_ocr]

    # 返回包含关键字 "search" 的元素列表
    return search_ocr