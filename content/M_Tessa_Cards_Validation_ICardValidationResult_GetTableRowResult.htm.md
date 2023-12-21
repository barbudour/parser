# ICardValidationResult.GetTableRowResult - метод
Возвращает результат валидации для строки коллекционной или древовидной
секции. Включает в себя результаты валидации всех полей, входящих в
проверенную строку.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValidationResult GetTableRowResult(
    	string sectionName,
    	int rowIndex
    )
VB __Копировать
     Function GetTableRowResult ( 
    	sectionName As String,
    	rowIndex As Integer
    ) As ValidationResult
C++ __Копировать
    ValidationResult^ GetTableRowResult(
    	String^ sectionName, 
    	int rowIndex
    )
F# __Копировать
     abstract GetTableRowResult : 
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
##  __См. также
#### Ссылки
[ICardValidationResult - ](T_Tessa_Cards_Validation_ICardValidationResult.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
