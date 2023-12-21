# CardValidationResult.GetSectionResult - метод
Возвращает результат валидации для строковой, коллекционной или древовидной
секции карточки. Включает в себя результаты валидации всех строк и полей,
входящих в проверенную секцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValidationResult GetSectionResult(
    	string sectionName,
    	bool ownResultsOnly = false
    )
VB __Копировать
     Public Function GetSectionResult ( 
    	sectionName As String,
    	Optional ownResultsOnly As Boolean = false
    ) As ValidationResult
C++ __Копировать
     public:
    virtual ValidationResult^ GetSectionResult(
    	String^ sectionName, 
    	bool ownResultsOnly = false
    ) sealed
F# __Копировать
     abstract GetSectionResult : 
            sectionName : string * 
            ?ownResultsOnly : bool 
    (* Defaults:
            let _ownResultsOnly = defaultArg ownResultsOnly false
    *)
    -> ValidationResult 
    override GetSectionResult : 
            sectionName : string * 
            ?ownResultsOnly : bool 
    (* Defaults:
            let _ownResultsOnly = defaultArg ownResultsOnly false
    *)
    -> ValidationResult 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя секции, для которой требуется получить результат валидации.
ownResultsOnly
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что возвращаются только результаты, связанные с секцией как таковой, но не с её дочерними объектами: строками и полями. 
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для заданной секции.
#### Реализации
[ICardValidationResult.GetSectionResult(String,
Boolean)](M_Tessa_Cards_Validation_ICardValidationResult_GetSectionResult.htm)  
##  __См. также
#### Ссылки
[CardValidationResult - ](T_Tessa_Cards_Validation_CardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
