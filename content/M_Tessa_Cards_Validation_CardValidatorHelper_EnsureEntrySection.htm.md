# CardValidatorHelper.EnsureEntrySection - метод
Подтверждает, что заданная метаинформация относится к строковой секции.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool EnsureEntrySection(
    	CardMetadataSection section,
    	Object validator,
    	ICardValidationContext context
    )
VB __Копировать
     Public Shared Function EnsureEntrySection ( 
    	section As CardMetadataSection,
    	validator As Object,
    	context As ICardValidationContext
    ) As Boolean
C++ __Копировать
     public:
    static bool EnsureEntrySection(
    	CardMetadataSection^ section, 
    	Object^ validator, 
    	ICardValidationContext^ context
    )
F# __Копировать
     static member EnsureEntrySection : 
            section : CardMetadataSection * 
            validator : Object * 
            context : ICardValidationContext -> bool 
#### Параметры
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Метаинформация по секции, тип которой требуется проверить.
validator [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр валидатора.
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданная метаинформация относится к строковой секции; false в
противном случае.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
