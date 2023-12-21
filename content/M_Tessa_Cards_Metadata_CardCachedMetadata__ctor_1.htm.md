# CardCachedMetadata(CardMetadataCache, ICardTypeServerRepository,
ICardMetadataBuilder, ISchemeService, IDbScope, String) - конструктор
Создаёт экземпляр класса с указанием сервиса для управления типами карточек,
объекта, выполняющего построение метаинформации по типам карточек, и объекта,
используемого для доступа к метаинформации по структуре базы данных.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardCachedMetadata(
    	[NotNullAttribute] CardMetadataCache cardMetadataCache,
    	[NotNullAttribute] ICardTypeServerRepository cardTypeServerRepository,
    	[NotNullAttribute] ICardMetadataBuilder cardMetadataBuilder,
    	[NotNullAttribute] ISchemeService schemeService,
    	[NotNullAttribute] IDbScope dbScope,
    	string builderName = "Default"
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> cardMetadataCache As CardMetadataCache,
    	<NotNullAttribute> cardTypeServerRepository As ICardTypeServerRepository,
    	<NotNullAttribute> cardMetadataBuilder As ICardMetadataBuilder,
    	<NotNullAttribute> schemeService As ISchemeService,
    	<NotNullAttribute> dbScope As IDbScope,
    	Optional builderName As String = "Default"
    )
C++ __Копировать
     public:
    CardCachedMetadata(
    	[NotNullAttribute] CardMetadataCache^ cardMetadataCache, 
    	[NotNullAttribute] ICardTypeServerRepository^ cardTypeServerRepository, 
    	[NotNullAttribute] ICardMetadataBuilder^ cardMetadataBuilder, 
    	[NotNullAttribute] ISchemeService^ schemeService, 
    	[NotNullAttribute] IDbScope^ dbScope, 
    	String^ builderName = L"Default"
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] cardMetadataCache : CardMetadataCache * 
            [<NotNullAttribute>] cardTypeServerRepository : ICardTypeServerRepository * 
            [<NotNullAttribute>] cardMetadataBuilder : ICardMetadataBuilder * 
            [<NotNullAttribute>] schemeService : ISchemeService * 
            [<NotNullAttribute>] dbScope : IDbScope * 
            ?builderName : string 
    (* Defaults:
            let _builderName = defaultArg builderName "Default"
    *)
    -> CardCachedMetadata
#### Параметры
cardMetadataCache
[CardMetadataCache](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
    Глобальный кэш с метаинформацией карточек.
cardTypeServerRepository
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)
    Репозиторий для управления типами карточек на сервере.
cardMetadataBuilder
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm)
     Объект, выполняющий построение метаинформации по типам карточек [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm). 
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
     Объект, используемый для доступа к метаинформации по структуре базы данных. 
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, используемый для соединения с базой данных.
builderName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя, по которому будет резолвиться [ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm).
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[CardCachedMetadata -
перегрузка](Overload_Tessa_Cards_Metadata_CardCachedMetadata__ctor.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
