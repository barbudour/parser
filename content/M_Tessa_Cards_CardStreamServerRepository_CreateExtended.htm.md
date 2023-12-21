# CardStreamServerRepository.CreateExtended - метод
Создаёт экземпляр репозитория с расширенной конфигурацией серверных
компонентов по умолчанию, с указанием контейнера с используемыми расширениями,
метаинформации по типам карточек, объекта сессии текущего пользователя, а
также области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICardStreamServerRepository CreateExtended(
    	IExtensionContainer extensionContainer,
    	string fileBasePath,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope,
    	CardCachingStrategyType cachingStrategyType,
    	IConfigurationInfoProvider configurationInfoProvider,
    	ISignatureProvider fileSignatureProvider = null,
    	CardGlobalComponentCache globalComponentCache = null,
    	bool useSimpleNamingScheme = false
    )
VB __Копировать
     Public Shared Function CreateExtended ( 
    	extensionContainer As IExtensionContainer,
    	fileBasePath As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	dbScope As IDbScope,
    	cachingStrategyType As CardCachingStrategyType,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	Optional fileSignatureProvider As ISignatureProvider = Nothing,
    	Optional globalComponentCache As CardGlobalComponentCache = Nothing,
    	Optional useSimpleNamingScheme As Boolean = false
    ) As ICardStreamServerRepository
C++ __Копировать
     public:
    static ICardStreamServerRepository^ CreateExtended(
    	IExtensionContainer^ extensionContainer, 
    	String^ fileBasePath, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope, 
    	CardCachingStrategyType cachingStrategyType, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	ISignatureProvider^ fileSignatureProvider = nullptr, 
    	CardGlobalComponentCache^ globalComponentCache = nullptr, 
    	bool useSimpleNamingScheme = false
    )
F# __Копировать
     static member CreateExtended : 
            extensionContainer : IExtensionContainer * 
            fileBasePath : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            dbScope : IDbScope * 
            cachingStrategyType : CardCachingStrategyType * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            ?fileSignatureProvider : ISignatureProvider * 
            ?globalComponentCache : CardGlobalComponentCache * 
            ?useSimpleNamingScheme : bool 
    (* Defaults:
            let _fileSignatureProvider = defaultArg fileSignatureProvider null
            let _globalComponentCache = defaultArg globalComponentCache null
            let _useSimpleNamingScheme = defaultArg useSimpleNamingScheme false
    *)
    -> ICardStreamServerRepository 
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер с используемыми расширениями.
fileBasePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Базовый путь к хранилищу файлов в файловой системе.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия, в рамках которой выполняются операции.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
cachingStrategyType
[CardCachingStrategyType](T_Tessa_Cards_ComponentModel_CardCachingStrategyType.htm)
    Тип стратегии кэширования для компонентов карточки.
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
    Поставщик информации о настройках.
fileSignatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm) (Optional)
     Объект, предоставляющий криптографические средства для вычисления хеш-суммы содержимого файла, или null, если хеш сумма будет вычислена стандартными средствами [Files](P_Tessa_Platform_HashSignatureProvider_Files.htm). Объект должен поддерживать [IHashSignatureProvider](T_Tessa_Platform_IHashSignatureProvider.htm). 
globalComponentCache
[CardGlobalComponentCache](T_Tessa_Cards_ComponentModel_CardGlobalComponentCache.htm)
(Optional)
     Глобальный кэш для компонентов API карточек или null, если при использовании стратегии глобального кэша создаётся новый глобальный кэш компонентов. 
useSimpleNamingScheme
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что следует использовать режим обратной совместимости для размещения файлов в файловом хранилище. 
#### Возвращаемое значение
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)  
Созданный экземпляр репозитория.
##  __См. также
#### Ссылки
[CardStreamServerRepository - ](T_Tessa_Cards_CardStreamServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
