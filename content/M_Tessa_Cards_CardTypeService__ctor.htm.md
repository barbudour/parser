# CardTypeService - конструктор
Инициализирует новый экземпляр класса
[CardTypeService](T_Tessa_Cards_CardTypeService.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTypeService(
    	ICardTypeServerRepository cardTypeServerRepository,
    	CardMetadataCache cardMetadataCache,
    	IConfigurationVersionProvider configurationVersionProvider,
    	IConfigurationInfoProvider configurationInfoProvider,
    	IDbScope dbScope,
    	Func<string, ICardMetadataBuilder> getCardMetadataBuilder,
    	ISchemeService schemeService,
    	ITransactionStrategy transactionStrategy,
    	[OptionalDependencyAttribute] IConfigurationLogger configurationLogger = null
    )
VB __Копировать
     Public Sub New ( 
    	cardTypeServerRepository As ICardTypeServerRepository,
    	cardMetadataCache As CardMetadataCache,
    	configurationVersionProvider As IConfigurationVersionProvider,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	dbScope As IDbScope,
    	getCardMetadataBuilder As Func(Of String, ICardMetadataBuilder),
    	schemeService As ISchemeService,
    	transactionStrategy As ITransactionStrategy,
    	<OptionalDependencyAttribute> Optional configurationLogger As IConfigurationLogger = Nothing
    )
C++ __Копировать
     public:
    CardTypeService(
    	ICardTypeServerRepository^ cardTypeServerRepository, 
    	CardMetadataCache^ cardMetadataCache, 
    	IConfigurationVersionProvider^ configurationVersionProvider, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	IDbScope^ dbScope, 
    	Func<String^, ICardMetadataBuilder^>^ getCardMetadataBuilder, 
    	ISchemeService^ schemeService, 
    	ITransactionStrategy^ transactionStrategy, 
    	[OptionalDependencyAttribute] IConfigurationLogger^ configurationLogger = nullptr
    )
F# __Копировать
     new : 
            cardTypeServerRepository : ICardTypeServerRepository * 
            cardMetadataCache : CardMetadataCache * 
            configurationVersionProvider : IConfigurationVersionProvider * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            dbScope : IDbScope * 
            getCardMetadataBuilder : Func<string, ICardMetadataBuilder> * 
            schemeService : ISchemeService * 
            transactionStrategy : ITransactionStrategy * 
            [<OptionalDependencyAttribute>] ?configurationLogger : IConfigurationLogger 
    (* Defaults:
            let _configurationLogger = defaultArg configurationLogger null
    *)
    -> CardTypeService
#### Параметры
cardTypeServerRepository
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)
    Репозиторий типов карточек.
cardMetadataCache
[CardMetadataCache](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
    Глобальный кэш метаинформации карточек.
configurationVersionProvider
[IConfigurationVersionProvider](T_Tessa_Platform_Runtime_IConfigurationVersionProvider.htm)
    Объект, обеспечивающий взаимодействие с версией конфигурации.
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Объект, предоставляющий информацию по текущей конфигурации.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
getCardMetadataBuilder
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm)>
     Функция, позволяющая получить объект, выполняющий построение метаинформации по типам карточек [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm). 
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
     Объект, используемый для доступа к метаинформации по структуре базы данных. 
transactionStrategy
[ITransactionStrategy](T_Tessa_Platform_Data_ITransactionStrategy.htm)
    Стратегия выполнения кода в SQL-транзакции.
configurationLogger
[IConfigurationLogger](T_Tessa_Platform_Configuration_IConfigurationLogger.htm)
(Optional)
     Объект, выполняющий логирование при изменении конфигурации, или null, если логирование не требуется. 
## __См. также
#### Ссылки
[CardTypeService - ](T_Tessa_Cards_CardTypeService.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
