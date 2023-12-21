# CardValidatorHelper.TryGetColumn - метод
Возвращает метаинформацию по одной или нескольким физическим колонкам, которая
требуется валидатору.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetColumn(
    	CardMetadataSection section,
    	Guid columnID,
    	Object validator,
    	ICardValidationContext context,
    	out CardMetadataColumn mainColumn,
    	out CardMetadataColumn[] physicalColumns
    )
VB __Копировать
     Public Shared Function TryGetColumn ( 
    	section As CardMetadataSection,
    	columnID As Guid,
    	validator As Object,
    	context As ICardValidationContext,
    	<OutAttribute> ByRef mainColumn As CardMetadataColumn,
    	<OutAttribute> ByRef physicalColumns As CardMetadataColumn()
    ) As Boolean
C++ __Копировать
     public:
    static bool TryGetColumn(
    	CardMetadataSection^ section, 
    	Guid columnID, 
    	Object^ validator, 
    	ICardValidationContext^ context, 
    	[OutAttribute] CardMetadataColumn^% mainColumn, 
    	[OutAttribute] array<CardMetadataColumn^>^% physicalColumns
    )
F# __Копировать
     static member TryGetColumn : 
            section : CardMetadataSection * 
            columnID : Guid * 
            validator : Object * 
            context : ICardValidationContext * 
            mainColumn : CardMetadataColumn byref * 
            physicalColumns : CardMetadataColumn[] byref -> bool 
#### Параметры
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Метаинформация по секции, в которой расположена требуемая колонка.
columnID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор колонки, метаинформация по которой требуется валидатору.
validator [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр валидатора.
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации.
mainColumn [CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
    Основная колонка, проверка которой выполняется. Может быть физической или комплексной.
physicalColumns
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)[]
    Возвращённая метаинформация по одной или нескольким физическим колонкам.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если параметр physicalColumns содержит запрошенные значения; false, если
при получении значения произошла ошибка.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
