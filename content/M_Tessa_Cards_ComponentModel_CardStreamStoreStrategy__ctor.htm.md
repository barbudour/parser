# CardStreamStoreStrategy - конструктор
Создаёт экземпляр класса с указанием области видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm), репозитория для работы с
файлами и компонента для сохранения карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStreamStoreStrategy(
    	IDbScope dbScope,
    	ICardStoreComponent storeComponent,
    	ICardRequestComponent requestComponent,
    	ICardContentStrategy contentStrategy,
    	ICardFileVersionStrategy versionStrategy,
    	ICardMetadata cardMetadata,
    	ISession session,
    	[OptionalDependencyAttribute("Files")] ISignatureProvider fileSignatureProvider = null
    )
VB __Копировать
     Public Sub New ( 
    	dbScope As IDbScope,
    	storeComponent As ICardStoreComponent,
    	requestComponent As ICardRequestComponent,
    	contentStrategy As ICardContentStrategy,
    	versionStrategy As ICardFileVersionStrategy,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	<OptionalDependencyAttribute("Files")> Optional fileSignatureProvider As ISignatureProvider = Nothing
    )
C++ __Копировать
     public:
    CardStreamStoreStrategy(
    	IDbScope^ dbScope, 
    	ICardStoreComponent^ storeComponent, 
    	ICardRequestComponent^ requestComponent, 
    	ICardContentStrategy^ contentStrategy, 
    	ICardFileVersionStrategy^ versionStrategy, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	[OptionalDependencyAttribute(L"Files")] ISignatureProvider^ fileSignatureProvider = nullptr
    )
F# __Копировать
     new : 
            dbScope : IDbScope * 
            storeComponent : ICardStoreComponent * 
            requestComponent : ICardRequestComponent * 
            contentStrategy : ICardContentStrategy * 
            versionStrategy : ICardFileVersionStrategy * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            [<OptionalDependencyAttribute("Files")>] ?fileSignatureProvider : ISignatureProvider 
    (* Defaults:
            let _fileSignatureProvider = defaultArg fileSignatureProvider null
    *)
    -> CardStreamStoreStrategy
#### Параметры
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Область видимости объекта [DbManager](T_Tessa_Platform_Data_DbManager.htm).
storeComponent
[ICardStoreComponent](T_Tessa_Cards_ComponentModel_ICardStoreComponent.htm)
    Компонент для сохранения карточки.
requestComponent
[ICardRequestComponent](T_Tessa_Cards_ComponentModel_ICardRequestComponent.htm)
    Компонент для выполнения универсальных запросов к сервису карточек.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файла.
versionStrategy
[ICardFileVersionStrategy](T_Tessa_Cards_ComponentModel_ICardFileVersionStrategy.htm)
    Стратегия, определяющая состояние версии файла.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя.
fileSignatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm) (Optional)
     Объект, предоставляющий криптографические средства для вычисления хеш-суммы содержимого файла, или null, если хеш сумма будет вычислена стандартными средствами [Files](P_Tessa_Platform_HashSignatureProvider_Files.htm). Объект должен поддерживать [IHashSignatureProvider](T_Tessa_Platform_IHashSignatureProvider.htm). 
## __См. также
#### Ссылки
[CardStreamStoreStrategy -
](T_Tessa_Cards_ComponentModel_CardStreamStoreStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
