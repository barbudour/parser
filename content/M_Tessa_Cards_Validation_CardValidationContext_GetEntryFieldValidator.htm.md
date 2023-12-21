# CardValidationContext.GetEntryFieldValidator - метод
Возвращает объект, выполняющий построение результата валидации для заданного
поля строковой секции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IValidationResultBuilder GetEntryFieldValidator(
    	string sectionName,
    	string fieldName
    )
VB __Копировать
     Public Function GetEntryFieldValidator ( 
    	sectionName As String,
    	fieldName As String
    ) As IValidationResultBuilder
C++ __Копировать
     public:
    virtual IValidationResultBuilder^ GetEntryFieldValidator(
    	String^ sectionName, 
    	String^ fieldName
    ) sealed
F# __Копировать
     abstract GetEntryFieldValidator : 
            sectionName : string * 
            fieldName : string -> IValidationResultBuilder 
    override GetEntryFieldValidator : 
            sectionName : string * 
            fieldName : string -> IValidationResultBuilder 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя строковой секции, для поля которой выполняется валидация.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Поле заданной строковой секции, для которого выполняется валидация.
#### Возвращаемое значение
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)  
Объект, выполняющий построение результата валидации для заданного поля.
#### Реализации
[ICardValidationContext.GetEntryFieldValidator(String,
String)](M_Tessa_Cards_Validation_ICardValidationContext_GetEntryFieldValidator.htm)  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
