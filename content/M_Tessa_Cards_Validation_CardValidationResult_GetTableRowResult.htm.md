# CardValidationResult.GetTableRowResult - метод
Возвращает результат валидации для строки коллекционной или древовидной
секции. Включает в себя результаты валидации всех полей, входящих в
проверенную строку.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValidationResult GetTableRowResult(
    	string sectionName,
    	int rowIndex
    )
VB __Копировать
     Public Function GetTableRowResult ( 
    	sectionName As String,
    	rowIndex As Integer
    ) As ValidationResult
C++ __Копировать
     public:
    virtual ValidationResult^ GetTableRowResult(
    	String^ sectionName, 
    	int rowIndex
    ) sealed
F# __Копировать
     abstract GetTableRowResult : 
            sectionName : string * 
            rowIndex : int -> ValidationResult 
    override GetTableRowResult : 
            sectionName : string * 
            rowIndex : int -> ValidationResult 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя коллекционной или древовидной секции, для строки которой требуется получить результат валидации.
rowIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс строки заданной коллекционной или древовидной секции, для которой требуется получить результат валидации.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для заданной строки.
#### Реализации
[ICardValidationResult.GetTableRowResult(String,
Int32)](M_Tessa_Cards_Validation_ICardValidationResult_GetTableRowResult.htm)  
##  __См. также
#### Ссылки
[CardValidationResult - ](T_Tessa_Cards_Validation_CardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
