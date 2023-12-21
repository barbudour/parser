# ICardValidationResult.GetTableFieldResult - метод
Возвращает результат валидации для заданного поля строки коллекционной или
древовидной секции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValidationResult GetTableFieldResult(
    	string sectionName,
    	int rowIndex,
    	string fieldName
    )
VB __Копировать
     Function GetTableFieldResult ( 
    	sectionName As String,
    	rowIndex As Integer,
    	fieldName As String
    ) As ValidationResult
C++ __Копировать
    ValidationResult^ GetTableFieldResult(
    	String^ sectionName, 
    	int rowIndex, 
    	String^ fieldName
    )
F# __Копировать
     abstract GetTableFieldResult : 
            sectionName : string * 
            rowIndex : int * 
            fieldName : string -> ValidationResult 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя коллекционной или древовидной секции, для строки которой требуется получить результат валидации.
rowIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс строки заданной коллекционной или древовидной секции, для поля которой требуется получить результат валидации.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля в строке коллекционной или древовидной секции, для которого требуется получить результат валидации.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для заданного поля.
##  __См. также
#### Ссылки
[ICardValidationResult - ](T_Tessa_Cards_Validation_ICardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
