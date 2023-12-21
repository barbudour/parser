# CardMetadataBuilderBase.BuildInternalAsync - метод
Выполняет построение метаинформации
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) по заданным типам
карточек cardTypes и возвращает созданный объект.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<CardMetadata> BuildInternalAsync(
    	CardTypeCollection cardTypes,
    	ISchemeService schemeService,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function BuildInternalAsync ( 
    	cardTypes As CardTypeCollection,
    	schemeService As ISchemeService,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardMetadata)
C++ __Копировать
     protected:
    virtual Task<CardMetadata^>^ BuildInternalAsync(
    	CardTypeCollection^ cardTypes, 
    	ISchemeService^ schemeService, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract BuildInternalAsync : 
            cardTypes : CardTypeCollection * 
            schemeService : ISchemeService * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardMetadata> 
    override BuildInternalAsync : 
            cardTypes : CardTypeCollection * 
            schemeService : ISchemeService * 
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
[CardMetadataBuilderBase -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
