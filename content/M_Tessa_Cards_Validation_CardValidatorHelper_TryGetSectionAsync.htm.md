# CardValidatorHelper.TryGetSectionAsync - метод
Возвращает метаинформацию по секции, которая требуется валидатору, или null,
если секция не найдена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<CardMetadataSection> TryGetSectionAsync(
    	Guid sectionID,
    	Object validator,
    	ICardValidationContext context
    )
VB __Копировать
     Public Shared Function TryGetSectionAsync ( 
    	sectionID As Guid,
    	validator As Object,
    	context As ICardValidationContext
    ) As ValueTask(Of CardMetadataSection)
C++ __Копировать
     public:
    static ValueTask<CardMetadataSection^> TryGetSectionAsync(
    	Guid sectionID, 
    	Object^ validator, 
    	ICardValidationContext^ context
    )
F# __Копировать
     static member TryGetSectionAsync : 
            sectionID : Guid * 
            validator : Object * 
            context : ICardValidationContext -> ValueTask<CardMetadataSection> 
#### Параметры
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор секции, метаинформация по которой требуется валидатору.
validator [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр валидатора.
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)>  
Метаинформация по секции, которая требуется валидатору, или null, если секция
не найдена.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
