# UniqueValidatorHelper - методы
##  __Методы
[CheckUniqueAsync(CardValidationUniqueInfo, IDbScope,
CancellationToken)](M_Tessa_Cards_Validation_UniqueValidatorHelper_CheckUniqueAsync_1.htm)|
Проверяет на наличие дубликатов строки секции, заданной в параметрах
валидатора уникальности info.  
---|---  
[CheckUniqueAsync(List<CardValidationUniqueInfo>, IDbScope,
IValidationResultBuilder, Object, Boolean,
CancellationToken)](M_Tessa_Cards_Validation_UniqueValidatorHelper_CheckUniqueAsync.htm)|
Проверяет на наличие дубликатов для строк секций, заданных в параметрах
валидаторов уникальности infoList. Возвращает признак того, что все проверки
успешно выполнены и дубликатов нет.  
[CheckUniqueOrRemoveDuplicatesOnClientAsync](M_Tessa_Cards_Validation_UniqueValidatorHelper_CheckUniqueOrRemoveDuplicatesOnClientAsync.htm)|
Проверяет на уникальность или удаляет дубликаты для секции при выполнении на
клиенте.  
[RemoveDuplicatesAsync(CardValidationUniqueInfo, IDbScope,
Func<IList<CardRow>, CardRow, CancellationToken, ValueTask>,
CancellationToken)](M_Tessa_Cards_Validation_UniqueValidatorHelper_RemoveDuplicatesAsync_1.htm)|
Удаляет дубликаты для строк секции, заданной в параметрах валидатора
уникальности info.  
[RemoveDuplicatesAsync(List<CardValidationUniqueInfo>, IDbScope,
Func<CardValidationUniqueInfo, IList<CardRow>, CardRow, CancellationToken,
ValueTask>,
CancellationToken)](M_Tessa_Cards_Validation_UniqueValidatorHelper_RemoveDuplicatesAsync.htm)|
Удаляет дубликаты для строк секций, заданных в параметрах валидаторов
уникальности infoList.  
## __См. также
#### Ссылки
[UniqueValidatorHelper - ](T_Tessa_Cards_Validation_UniqueValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
