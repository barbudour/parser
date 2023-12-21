# CardValidationUniqueInfo - свойства
##  __Свойства
[CardType](P_Tessa_Cards_Validation_CardValidationUniqueInfo_CardType.htm)|
Тип карточки, файла или задания, к которому принадлежит секция.  
---|---  
[Instance](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Instance.htm)|
Проверяемый объект, по которому могут быть получены секции и идентификатор.
Может быть объектом карточки, файла или задания.  
[MainColumn](P_Tessa_Cards_Validation_CardValidationUniqueInfo_MainColumn.htm)|
Колонка в родительской секции или null, если родительская секция не задана.  
[OrderColumn](P_Tessa_Cards_Validation_CardValidationUniqueInfo_OrderColumn.htm)|
Физическая колонка для сортировки в секции
[Section](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Section.htm) или
null, если колонка для сортировки не задана.  
[ParentMainColumn](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ParentMainColumn.htm)|
Комплексная или физическая колонка, в которой требуется проверить уникальность
значения.  
[ParentPhysicalColumns](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ParentPhysicalColumns.htm)|
Физические колонки в родительской секции или пустая коллекция, если
родительская секция не задана. Если валидатор был связан с комплексной
колонкой, то свойство содержит все ключевые колонки внутри комплексной. В
противном случае свойство содержит единственную физическую колонку, с которой
был связан валидатор.  
[ParentSection](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ParentSection.htm)|
Родительская секция или null, если родительская секция не задана.  
[PhysicalColumns](P_Tessa_Cards_Validation_CardValidationUniqueInfo_PhysicalColumns.htm)|
Физические колонки, в которых требуется проверить уникальность значения. Если
валидатор был связан с комплексной колонкой, то свойство содержит все ключевые
колонки внутри комплексной. В противном случае свойство содержит единственную
физическую колонку, с которой был связан валидатор.  
[RemoveDuplicates](P_Tessa_Cards_Validation_CardValidationUniqueInfo_RemoveDuplicates.htm)|
Признак того, что дубликаты, найденные в коллекционной секции, должны быть
автоматически удалены.  
[Section](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Section.htm)|
Секция, в которой требуется проверить уникальность значения.  
[StoreMode](P_Tessa_Cards_Validation_CardValidationUniqueInfo_StoreMode.htm)|
Режим сохранения карточки. Поскольку
[Instance](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Instance.htm)
может быть заданием, то режим сохранения определяем отдельным свойством.  
[ValidationMode](P_Tessa_Cards_Validation_CardValidationUniqueInfo_ValidationMode.htm)|
Способ выполнения валидации.  
[Validator](P_Tessa_Cards_Validation_CardValidationUniqueInfo_Validator.htm)|
Валидатор, инициировавший проверку секции.  
## __См. также
#### Ссылки
[CardValidationUniqueInfo -
](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
