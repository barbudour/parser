# CardMetadataBuilder.AddCardTypeAsync - метод
Добавляет информацию по секциям и колонкам заданного типа карточки в контейнер
[Tessa.Cards.Metadata.CardMetadataBuilderBase.MetadataContainer].
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<bool?> AddCardTypeAsync(
    	CardMetadataBuilderBase.MetadataContainer container,
    	CardType cardType,
    	ISchemeService schemeService,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function AddCardTypeAsync ( 
    	container As CardMetadataBuilderBase.MetadataContainer,
    	cardType As CardType,
    	schemeService As ISchemeService,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean?)
C++ __Копировать
     protected:
    virtual ValueTask<Nullable<bool>> AddCardTypeAsync(
    	CardMetadataBuilderBase.MetadataContainer^ container, 
    	CardType^ cardType, 
    	ISchemeService^ schemeService, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract AddCardTypeAsync : 
            container : CardMetadataBuilderBase.MetadataContainer * 
            cardType : CardType * 
            schemeService : ISchemeService * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Nullable<bool>> 
    override AddCardTypeAsync : 
            container : CardMetadataBuilderBase.MetadataContainer * 
            cardType : CardType * 
            schemeService : ISchemeService * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Nullable<bool>> 
#### Параметры
container
[CardMetadataBuilderBase.MetadataContainer](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
    Контейнер, в который должна быть добавлена информация по секциям и колонкам заданного типа карточек.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточек, для которого должна быть добавлена информация по секциям и колонкам.
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
    Объект, используемый для доступа к метаинформации по структуре базы данных.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, содержащий сообщения валидации при создании типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>  
true, если информация по секциями и колонкам типа карточки успешно
зарегистрирована; false, если тип карточки повреждён и информация по секциям и
колонка зарегистрирована частично; null, если в типе карточки присутствуют
неизвестные секции или колонки, но для этого типа расширения запросили
отложить проверку, причём все присутствующие в схеме секции и колонки были
зарегистрированы.
## __См. также
#### Ссылки
[CardMetadataBuilder - ](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
