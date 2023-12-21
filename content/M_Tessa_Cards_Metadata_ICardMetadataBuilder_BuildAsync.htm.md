# ICardMetadataBuilder.BuildAsync - метод
Выполняет построение метаинформации
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) по заданным типам
карточек cardTypes и возвращает созданный объект.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<CardMetadata> BuildAsync(
    	[CanBeNullAttribute] CardTypeCollection cardTypes,
    	[NotNullAttribute] ISchemeService schemeService,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function BuildAsync ( 
    	<CanBeNullAttribute> cardTypes As CardTypeCollection,
    	<NotNullAttribute> schemeService As ISchemeService,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardMetadata)
C++ __Копировать
    Task<CardMetadata^>^ BuildAsync(
    	[CanBeNullAttribute] CardTypeCollection^ cardTypes, 
    	[NotNullAttribute] ISchemeService^ schemeService, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract BuildAsync : 
            [<CanBeNullAttribute>] cardTypes : CardTypeCollection * 
            [<NotNullAttribute>] schemeService : ISchemeService * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardMetadata> 
#### Параметры
cardTypes [CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)
     Типы карточек, для которых требуется построить метаинформацию [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm). Значение может быть равно null. При передаче защищённой от изменений коллекции создаётся защищённый от изменений объект [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm). 
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
     Объект, используемый для доступа к метаинформации по структуре базы данных. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Созданный объект, содержащий построенную метаинформацию по типам карточек.
Изменение созданного объекта допустимо в том случае, если допустимо изменение
заданной коллекции cardTypes.
## __См. также
#### Ссылки
[ICardMetadataBuilder - ](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
