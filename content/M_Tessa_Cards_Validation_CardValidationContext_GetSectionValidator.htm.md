# CardValidationContext.GetSectionValidator - метод
Возвращает объект, выполняющий построение результата валидации для строковой,
коллекционной или древовидной секции карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IValidationResultBuilder GetSectionValidator(
    	string sectionName
    )
VB __Копировать
     Public Function GetSectionValidator ( 
    	sectionName As String
    ) As IValidationResultBuilder
C++ __Копировать
     public:
    virtual IValidationResultBuilder^ GetSectionValidator(
    	String^ sectionName
    ) sealed
F# __Копировать
     abstract GetSectionValidator : 
            sectionName : string -> IValidationResultBuilder 
    override GetSectionValidator : 
            sectionName : string -> IValidationResultBuilder 
#### Параметры
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя проверяемой секции.
#### Возвращаемое значение
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)  
Объект, выполняющий построение результата валидации для заданной секции.
#### Реализации
[ICardValidationContext.GetSectionValidator(String)](M_Tessa_Cards_Validation_ICardValidationContext_GetSectionValidator.htm)  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
