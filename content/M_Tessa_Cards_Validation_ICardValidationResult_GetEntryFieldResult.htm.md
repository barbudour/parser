# ICardValidationResult.GetEntryFieldResult - метод
Возвращает результат валидации для заданного поля строковой секции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValidationResult GetEntryFieldResult(
    	string sectionName,
    	string fieldName
    )
VB __Копировать
     Function GetEntryFieldResult ( 
    	sectionName As String,
    	fieldName As String
    ) As ValidationResult
C++ __Копировать
    ValidationResult^ GetEntryFieldResult(
    	String^ sectionName, 
    	String^ fieldName
    )
F# __Копировать
     abstract GetEntryFieldResult : 
            sectionName : string * 
            fieldName : string -> ValidationResult 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя строковой секции, для поля которой требуется получить результат валидации.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Поле заданной строковой секции, для которого требуется получить результат валидации.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для заданного поля.
##  __См. также
#### Ссылки
[ICardValidationResult - ](T_Tessa_Cards_Validation_ICardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
