-- Pandoc Lua filter for removing sourcepos filter attributes from spans to read pure "include line"
--
-- Take AST from …+sourcepos, and remove all "data-pos" spans 

function ClearDataPos(elem)
    elem.attributes['data-pos'] = nil
    return elem
end

return {
    {
    },
    {
        Span = ClearDataPos,
        Div = ClearDataPos,
    }
}
