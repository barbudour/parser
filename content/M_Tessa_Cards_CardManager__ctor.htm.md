# CardManager - конструктор
Создаёт экземпляр класса с указанием репозитория карточек, используемого для
выполнения операций с карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardManager(
    	ISession session,
    	ICardMetadata cardMetadata,
    	ICardRepairManager cardRepairManager,
    	ICardRepository cardRepository,
    	Func<IGuidReplacer> createGuidReplacerFunc,
    	ICardStreamClientRepository cardStreamClientRepository,
    	ISmartMerger<Card> cardMerger,
    	Func<IStorageValuesKeeper> createStorageValuesKeeperFunc,
    	ICardExternalSourceLogic cardExternalSourceLogic,
    	Func<string, ISourceProviderLinker> getProviderLinker,
    	ICardStreamServerRepository cardStreamServerRepository = null,
    	ICardNewStrategy newStrategy = null
    )
VB __Копировать
     Public Sub New ( 
    	session As ISession,
    	cardMetadata As ICardMetadata,
    	cardRepairManager As ICardRepairManager,
    	cardRepository As ICardRepository,
    	createGuidReplacerFunc As Func(Of IGuidReplacer),
    	cardStreamClientRepository As ICardStreamClientRepository,
    	cardMerger As ISmartMerger(Of Card),
    	createStorageValuesKeeperFunc As Func(Of IStorageValuesKeeper),
    	cardExternalSourceLogic As ICardExternalSourceLogic,
    	getProviderLinker As Func(Of String, ISourceProviderLinker),
    	Optional cardStreamServerRepository As ICardStreamServerRepository = Nothing,
    	Optional newStrategy As ICardNewStrategy = Nothing
    )
C++ __Копировать
     public:
    CardManager(
    	ISession^ session, 
    	ICardMetadata^ cardMetadata, 
    	ICardRepairManager^ cardRepairManager, 
    	ICardRepository^ cardRepository, 
    	Func<IGuidReplacer^>^ createGuidReplacerFunc, 
    	ICardStreamClientRepository^ cardStreamClientRepository, 
    	ISmartMerger<Card^>^ cardMerger, 
    	Func<IStorageValuesKeeper^>^ createStorageValuesKeeperFunc, 
    	ICardExternalSourceLogic^ cardExternalSourceLogic, 
    	Func<String^, ISourceProviderLinker^>^ getProviderLinker, 
    	ICardStreamServerRepository^ cardStreamServerRepository = nullptr, 
    	ICardNewStrategy^ newStrategy = nullptr
    )
F# __Копировать
     new : 
            session : ISession * 
            cardMetadata : ICardMetadata * 
            cardRepairManager : ICardRepairManager * 
            cardRepository : ICardRepository * 
            createGuidReplacerFunc : Func<IGuidReplacer> * 
            cardStreamClientRepository : ICardStreamClientRepository * 
            cardMerger : ISmartMerger<Card> * 
            createStorageValuesKeeperFunc : Func<IStorageValuesKeeper> * 
            cardExternalSourceLogic : ICardExternalSourceLogic * 
            getProviderLinker : Func<string, ISourceProviderLinker> * 
            ?cardStreamServerRepository : ICardStreamServerRepository * 
            ?newStrategy : ICardNewStrategy 
    (* Defaults:
            let _cardStreamServerRepository = defaultArg cardStreamServerRepository null
            let _newStrategy = defaultArg newStrategy null
    *)
    -> CardManager
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
     Сессия для текущего пользователя. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
     Метаданные по типам карточек. 
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
     Объект, управляющий исправлением структуры карточки, например, вследствие изменения её типа карточки. 
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий карточек, используемый для выполнения операций с карточками. 
createGuidReplacerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IGuidReplacer](T_Tessa_Platform_IGuidReplacer.htm)>
     Функция, выполняющая создание объекта [IGuidReplacer](T_Tessa_Platform_IGuidReplacer.htm) для замены идентификаторов, например, при создании по шаблону. 
cardStreamClientRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
     Потоковый репозиторий карточек на клиенте, используемый для выполнения операций с карточками. 
cardMerger
[ISmartMerger](T_Tessa_SmartMerge_ISmartMerger_1.htm)<[Card](T_Tessa_Cards_Card.htm)>
     Объект, содержащий логику слияния карточек при импорте. 
createStorageValuesKeeperFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IStorageValuesKeeper](T_Tessa_Platform_Storage_IStorageValuesKeeper.htm)>
    Получает объект, который позволяет запоминать и восстанавливать значения из хранилища (storage) по заданным путям.
cardExternalSourceLogic
[ICardExternalSourceLogic](T_Tessa_Cards_ICardExternalSourceLogic.htm)
     Объект, обеспечивающий выполнение логики по непосредственному чтению/записи карточек. Например с/на диск(а) (зависит от реализации [ISourceContentProvider](T_Tessa_Platform_SourceProviders_ISourceContentProvider.htm) передаваемого в его методы). 
getProviderLinker
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[ISourceProviderLinker](T_Tessa_Platform_SourceProviders_ISourceProviderLinker.htm)>
     Получает объект, который связывает провайдеры ресурсов между собой [ISourceProviderLinker](T_Tessa_Platform_SourceProviders_ISourceProviderLinker.htm). 
cardStreamServerRepository
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)
(Optional)
     Потоковый репозиторий карточек на сервере, используемый для выполнения операций с карточками, или null, если операции выполняются на клиенте. 
newStrategy
[ICardNewStrategy](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
(Optional)
     Стратегия создания карточки, используемая для получения объектов SectionRows без расширений, или null, если операции выполняются на клиенте. 
## __См. также
#### Ссылки
[CardManager - ](T_Tessa_Cards_CardManager.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
