# CardMetadataHelper.CreateCardMetadataAsync - метод
Создаёт метаинформацию по типам карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<CardMetadata> CreateCardMetadataAsync(
    	ICardTypeServerRepository cardTypeServerRepository,
    	ICardMetadataBuilder cardMetadataBuilder,
    	ISchemeService schemeService,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateCardMetadataAsync ( 
    	cardTypeServerRepository As ICardTypeServerRepository,
    	cardMetadataBuilder As ICardMetadataBuilder,
    	schemeService As ISchemeService,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardMetadata)
C++ __Копировать
     public:
    static Task<CardMetadata^>^ CreateCardMetadataAsync(
    	ICardTypeServerRepository^ cardTypeServerRepository, 
    	ICardMetadataBuilder^ cardMetadataBuilder, 
    	ISchemeService^ schemeService, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateCardMetadataAsync : 
            cardTypeServerRepository : ICardTypeServerRepository * 
            cardMetadataBuilder : ICardMetadataBuilder * 
            schemeService : ISchemeService * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardMetadata> 
#### Параметры
cardTypeServerRepository
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)
    Репозиторий для управления типами карточек на сервере.
cardMetadataBuilder
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm)
     Объект, выполняющий построение метаинформации по типам карточек [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm). 
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
     Объект, используемый для доступа к метаинформации по структуре базы данных. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Возвращает созданную метаинформацию.
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
