# ICardValidationContext.GetTableFieldValidator - метод
Возвращает объект, выполняющий построение результата валидации для заданного
поля строки коллекционной или древовидной секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IValidationResultBuilder GetTableFieldValidator(
    	string sectionName,
    	int rowIndex,
    	string fieldName
    )
VB __Копировать
     Function GetTableFieldValidator ( 
    	sectionName As String,
    	rowIndex As Integer,
    	fieldName As String
    ) As IValidationResultBuilder
C++ __Копировать
    IValidationResultBuilder^ GetTableFieldValidator(
    	String^ sectionName, 
    	int rowIndex, 
    	String^ fieldName
    )
F# __Копировать
     abstract GetTableFieldValidator : 
            sectionName : string * 
            rowIndex : int * 
            fieldName : string -> IValidationResultBuilder 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя коллекционной или древовидной секции, для строки которой выполняется валидация.
rowIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс строки заданной коллекционной или древовидной секции, для поля которой выполняется валидация.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля в строке коллекционной или древовидной секции, для которого выполняется валидация.
#### Возвращаемое значение
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)  
Объект, выполняющий построение результата валидации для заданного поля.
##  __См. также
#### Ссылки
[ICardValidationContext -
](T_Tessa_Cards_Validation_ICardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
