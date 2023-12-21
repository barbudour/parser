# CardValidationContext.GetTableRowValidator - метод
Возвращает объект, выполняющий построение результата валидации для строки
коллекционной или древовидной секции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IValidationResultBuilder GetTableRowValidator(
    	string sectionName,
    	int rowIndex
    )
VB __Копировать
     Public Function GetTableRowValidator ( 
    	sectionName As String,
    	rowIndex As Integer
    ) As IValidationResultBuilder
C++ __Копировать
     public:
    virtual IValidationResultBuilder^ GetTableRowValidator(
    	String^ sectionName, 
    	int rowIndex
    ) sealed
F# __Копировать
     abstract GetTableRowValidator : 
            sectionName : string * 
            rowIndex : int -> IValidationResultBuilder 
    override GetTableRowValidator : 
            sectionName : string * 
            rowIndex : int -> IValidationResultBuilder 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя коллекционной или древовидной секции, для строки которой выполняется валидация.
rowIndex [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс строки заданной коллекционной или древовидной секции, для которой выполняется валидация.
#### Возвращаемое значение
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)  
Объект, выполняющий построение результата валидации для заданной строки.
#### Реализации
[ICardValidationContext.GetTableRowValidator(String,
Int32)](M_Tessa_Cards_Validation_ICardValidationContext_GetTableRowValidator.htm)  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
