



# Transformacion 03. 
```DAX
= Table.ReplaceValue(#"Changed Type",".",",",Replacer.ReplaceText,{"sum_asks", "median"})
```

# Transformacion 04. 
```DAX
= Table.TransformColumnTypes(#"Replaced Value",{{"sum_asks", Int64.Type}, {"median", Int64.Type}})
```




