-- Pandoc Lua filter for adding filename of currently processed file back to 
-- "data-pos" attributes (compatible with "sourcepos" extension)

function Meta (meta)
    CURFILE = meta.current_markdown_file
    return meta
end

function AddFileNameToElem(elem)
    if elem.attributes ~= nil and elem.attributes['data-pos'] ~= nil then
	if not string.find(elem.attributes['data-pos'], '@') then
	   elem.attributes['data-pos'] = CURFILE .. "@" .. elem.attributes['data-pos']
        end
    end
    return elem
end

return {
    {
        Meta = Meta,
    },
    {
        Inlines = AddFileNameToElem,
        Span = AddFileNameToElem,
        Div = AddFileNameToElem,
        Headers = AddFileNameToElem,
        Block = AddFileNameToElem,
        Code = AddFileNameToElem,
        Span = AddFileNameToElem,
        Inlines = AddFileNameToElem,
        CodeBlock = AddFileNameToElem,
    }
}
