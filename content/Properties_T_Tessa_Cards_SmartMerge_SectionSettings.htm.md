# SectionSettings - свойства
##  __Свойства
[ExcludedColumns](P_Tessa_Cards_SmartMerge_SectionSettings_ExcludedColumns.htm)|
Исключенные колонки. Если заполнены, то значения узлов слияния, относящихся к
данной секции, будут сравниваться исключая эти колонки. Имеют приоритет перед
IncludedColumns. Если ExcludedColumns и IncludedColumns заполнены
одновременно, выдается Warning в ValidationResult.  
---|---  
[Ignored](P_Tessa_Cards_SmartMerge_SectionSettings_Ignored.htm)|  Указывает на
то что секция игнорируется при слиянии  
[IgnoredColumns](P_Tessa_Cards_SmartMerge_SectionSettings_IgnoredColumns.htm)|
Игнорируемые колонки. Поведение такое же как и у параметра ExcludedColumns
(дополняют друг друга), но в дополнение к логике параметра ExcludedColumns,
колонки, указанные в этом параметре, будут проигнорированы при апдейте узлов.  
[IgnoreDuplicateRows](P_Tessa_Cards_SmartMerge_SectionSettings_IgnoreDuplicateRows.htm)|
Отвечает за логику в случае более одного совпадения по ключевым полям на одном
"тир-уровне", имеет приоритет над общим одноименным флагом, установленным для
опций.  
[IncludedColumns](P_Tessa_Cards_SmartMerge_SectionSettings_IncludedColumns.htm)|
Включенные колонки. Если заполнены, то значения узлов слияния, относящихся к
данной секции, будут сравниваться только с учетом этих колонок.  
[KeyColumns](P_Tessa_Cards_SmartMerge_SectionSettings_KeyColumns.htm)|
Ключевые колонки. Если заполнены, то помимо RowID на первом уровне
сопоставления, на втором уровне объекты будут сопоставляться по этим ключевым
колонкам.  
[Name](P_Tessa_Cards_SmartMerge_SectionSettings_Name.htm)|  Наименование
секции  
## __См. также
#### Ссылки
[SectionSettings - ](T_Tessa_Cards_SmartMerge_SectionSettings.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
