# CardMetadataBuilder.CheckCardType - метод
Проверяет информацию по секциям и колонкам заданного типа карточки после
построения метаинформации, если расширения запросили отложить проверку для
этого типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override bool CheckCardType(
    	CardMetadataBuilderBase.MetadataContainer container,
    	CardType cardType,
    	CardMetadataSectionCollection sections,
    	IValidationResultBuilder validationResult
    )
VB __Копировать
     Protected Overrides Function CheckCardType ( 
    	container As CardMetadataBuilderBase.MetadataContainer,
    	cardType As CardType,
    	sections As CardMetadataSectionCollection,
    	validationResult As IValidationResultBuilder
    ) As Boolean
C++ __Копировать
     protected:
    virtual bool CheckCardType(
    	CardMetadataBuilderBase.MetadataContainer^ container, 
    	CardType^ cardType, 
    	CardMetadataSectionCollection^ sections, 
    	IValidationResultBuilder^ validationResult
    ) override
F# __Копировать
     abstract CheckCardType : 
            container : CardMetadataBuilderBase.MetadataContainer * 
            cardType : CardType * 
            sections : CardMetadataSectionCollection * 
            validationResult : IValidationResultBuilder -> bool 
    override CheckCardType : 
            container : CardMetadataBuilderBase.MetadataContainer * 
            cardType : CardType * 
            sections : CardMetadataSectionCollection * 
            validationResult : IValidationResultBuilder -> bool 
#### Параметры
container
[CardMetadataBuilderBase.MetadataContainer](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
    Контейнер, который используется при построении метаинформации.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточек, для которого должны быть выполнены проверки по секциям и колонкам.
sections
[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
    Метаинформация по всем секциям, относительно которой требуется выполнить проверки.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, содержащий сообщения валидации при создании типа карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если информация по секциями и колонкам типа карточки успешно проверена;
false, если тип карточки повреждён, т.е. некоторые секции или колонки
отсутствуют в метаинформации.
## __См. также
#### Ссылки
[CardMetadataBuilder - ](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
