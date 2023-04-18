### Transformacion 01. Source
```DAX
= Csv.Document(File.Contents("C:\X_TCS_Documents\Power_BI\CAM_V_03\export_raw_sample.csv"),[Delimiter=",", Columns=7, Encoding=1252, QuoteStyle=QuoteStyle.None])
```

### Transformacion 02. Promoted headers
```DAX
= Table.PromoteHeaders(Source, [PromoteAllScalars=true])
```

### Transformacion 03. Changed Type
```DAX
= Table.TransformColumnTypes(#"Promoted Headers",{{"airline_code", type text}, {"rt", type text}, {"op_av", type text}, {"flight_date", Int64.Type}, {"snapshot_date", Int64.Type}, {"sum_asks", type text}, {"median", type text}})
```

### Transformacion 04. Replaced Value
```DAX
= Table.ReplaceValue(#"Changed Type",".",",",Replacer.ReplaceText,{"sum_asks", "median"})
```

### Transformacion 05. Changed Type
```DAX
= Table.TransformColumnTypes(#"Replaced Value",{{"sum_asks", Int64.Type}, {"median", Int64.Type}})
```
