# CardValidatorHelper - методы
##  __Методы
[AddMessage](M_Tessa_Cards_Validation_CardValidatorHelper_AddMessage.htm)|
Добавляет сообщение валидации для заданного валидатора.  
---|---  
[AddNotNullTableValidationError](M_Tessa_Cards_Validation_CardValidatorHelper_AddNotNullTableValidationError.htm)|
Добавляет сообщение об ошибке валидации для заданного валидатора
[NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm), возникшее
при проверке секции section на валидность.  
[EnsureEntrySection](M_Tessa_Cards_Validation_CardValidatorHelper_EnsureEntrySection.htm)|
Подтверждает, что заданная метаинформация относится к строковой секции.  
[EnsureTableSection](M_Tessa_Cards_Validation_CardValidatorHelper_EnsureTableSection.htm)|
Подтверждает, что заданная метаинформация относится к коллекционной или
древовидной секции.  
[ExecuteValidatorsAsync](M_Tessa_Cards_Validation_CardValidatorHelper_ExecuteValidatorsAsync.htm)|
Выполняет валидаторы для заданной карточки.  
[ExistInType(CardType,
Guid)](M_Tessa_Cards_Validation_CardValidatorHelper_ExistInType.htm)|
Возвращает признак того, что секция с заданным идентификатором существует в
указанном типе карточки.  
[ExistInType(CardType, Guid,
Guid)](M_Tessa_Cards_Validation_CardValidatorHelper_ExistInType_1.htm)|
Возвращает признак того, что секция и колонка с заданными идентификаторами
существует в указанном типе карточки.  
[GetIsWarning](M_Tessa_Cards_Validation_CardValidatorHelper_GetIsWarning.htm)|
Возвращает признак того, что сообщение валидатора должно быть предупреждением,
а не ошибкой. Обычно сообщения-предупреждения не отображаются на клиенте,
кроме некоторых случаев работы с виртуальными секциями, которые на сервере не
могут быть проверены SQL-запросом.  
[GetObjectName(CardMetadataSection)](M_Tessa_Cards_Validation_CardValidatorHelper_GetObjectName.htm)|
Возвращает имя объекта валидации, полученное по секции, которую он проверяет.  
[GetObjectName(CardMetadataSection,
CardMetadataColumn)](M_Tessa_Cards_Validation_CardValidatorHelper_GetObjectName_1.htm)|
Возвращает имя объекта валидации, полученное по секции и колонке, которые он
проверяет.  
[GetParentColumnID](M_Tessa_Cards_Validation_CardValidatorHelper_GetParentColumnID.htm)|
Возвращает идентификатор родительской колонки, которая указана в настройках
валидатора, или null, если колонка не указана или указана как null.  
[GetRemoveDuplicates](M_Tessa_Cards_Validation_CardValidatorHelper_GetRemoveDuplicates.htm)|
Возвращает признак того, что неуникальные значения (дубликаты) нужно
автоматически удалять.  
[TryGetColumn](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetColumn.htm)|
Возвращает метаинформацию по одной или нескольким физическим колонкам, которая
требуется валидатору.  
[TryGetColumnID](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetColumnID.htm)|
Возвращает идентификатор колонки, которая указана в настройках валидатора.  
[TryGetErrorMessage](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetErrorMessage.htm)|
Возвращает сообщение об ошибке, которое следует выводить вместо стандартного
сообщения, или null или пустая строка, если сообщение не задано.  
[TryGetOrderColumnID](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetOrderColumnID.htm)|
Возвращает идентификатор колонки для сортировки, которая указана в настройках
валидатора.  
[TryGetParentSectionAndColumnID](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetParentSectionAndColumnID.htm)|
Возвращает идентификаторы родительской секции и колонки, которые указаны в
настройках валидатора. В случае, если какие-либо настройки не указаны или
равны null, то возвращается false.  
[TryGetSectionAsync](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetSectionAsync.htm)|
Возвращает метаинформацию по секции, которая требуется валидатору, или null,
если секция не найдена.  
[TryGetSectionID](M_Tessa_Cards_Validation_CardValidatorHelper_TryGetSectionID.htm)|
Возвращает идентификатор секции, которая указана в настройках валидатора.  
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
