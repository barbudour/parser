# CardValidationResult.GetEntryFieldResult - метод
Возвращает результат валидации для заданного поля строковой секции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValidationResult GetEntryFieldResult(
    	string sectionName,
    	string fieldName
    )
VB __Копировать
     Public Function GetEntryFieldResult ( 
    	sectionName As String,
    	fieldName As String
    ) As ValidationResult
C++ __Копировать
     public:
    virtual ValidationResult^ GetEntryFieldResult(
    	String^ sectionName, 
    	String^ fieldName
    ) sealed
F# __Копировать
     abstract GetEntryFieldResult : 
            sectionName : string * 
            fieldName : string -> ValidationResult 
    override GetEntryFieldResult : 
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
#### Реализации
[ICardValidationResult.GetEntryFieldResult(String,
String)](M_Tessa_Cards_Validation_ICardValidationResult_GetEntryFieldResult.htm)  
##  __См. также
#### Ссылки
[CardValidationResult - ](T_Tessa_Cards_Validation_CardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
