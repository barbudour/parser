# FileSourceForCard - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSourceForCard(
    	FileSourceForCardContext sourceContext,
    	Card card,
    	CardType cardType,
    	ICardMetadata cardMetadata,
    	ICardRepository cardRepository,
    	ICardStreamClientRepository cardStreamClientRepository,
    	ICardStreamServerRepository cardStreamServerRepository,
    	ICardFileSourceSettings cardFileSourceSettings,
    	IFileCache cache,
    	ISession session,
    	[OptionalDependencyAttribute] IFileManager manager = null,
    	[OptionalDependencyAttribute] IApplicationDescriptor applicationDescriptor = null
    )
VB __Копировать
     Public Sub New ( 
    	sourceContext As FileSourceForCardContext,
    	card As Card,
    	cardType As CardType,
    	cardMetadata As ICardMetadata,
    	cardRepository As ICardRepository,
    	cardStreamClientRepository As ICardStreamClientRepository,
    	cardStreamServerRepository As ICardStreamServerRepository,
    	cardFileSourceSettings As ICardFileSourceSettings,
    	cache As IFileCache,
    	session As ISession,
    	<OptionalDependencyAttribute> Optional manager As IFileManager = Nothing,
    	<OptionalDependencyAttribute> Optional applicationDescriptor As IApplicationDescriptor = Nothing
    )
C++ __Копировать
     public:
    FileSourceForCard(
    	FileSourceForCardContext^ sourceContext, 
    	Card^ card, 
    	CardType^ cardType, 
    	ICardMetadata^ cardMetadata, 
    	ICardRepository^ cardRepository, 
    	ICardStreamClientRepository^ cardStreamClientRepository, 
    	ICardStreamServerRepository^ cardStreamServerRepository, 
    	ICardFileSourceSettings^ cardFileSourceSettings, 
    	IFileCache^ cache, 
    	ISession^ session, 
    	[OptionalDependencyAttribute] IFileManager^ manager = nullptr, 
    	[OptionalDependencyAttribute] IApplicationDescriptor^ applicationDescriptor = nullptr
    )
F# __Копировать
     new : 
            sourceContext : FileSourceForCardContext * 
            card : Card * 
            cardType : CardType * 
            cardMetadata : ICardMetadata * 
            cardRepository : ICardRepository * 
            cardStreamClientRepository : ICardStreamClientRepository * 
            cardStreamServerRepository : ICardStreamServerRepository * 
            cardFileSourceSettings : ICardFileSourceSettings * 
            cache : IFileCache * 
            session : ISession * 
            [<OptionalDependencyAttribute>] ?manager : IFileManager * 
            [<OptionalDependencyAttribute>] ?applicationDescriptor : IApplicationDescriptor 
    (* Defaults:
            let _manager = defaultArg manager null
            let _applicationDescriptor = defaultArg applicationDescriptor null
    *)
    -> FileSourceForCard
#### Параметры
sourceContext
[FileSourceForCardContext](T_Tessa_Cards_FileSourceForCardContext.htm)
    Контекст использования источника файлов.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой создаётся источник файлов.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки card.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками.
cardStreamClientRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
    Репозиторий для потокового управления карточками на клиенте.
cardStreamServerRepository
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)
    Репозиторий для потокового управления карточками на сервере.
cardFileSourceSettings
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm)
    Настройки по местоположениям контента файлов.
cache [IFileCache](T_Tessa_Files_IFileCache.htm)
    Кэш для контента файлов.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
     Сессия пользователя, который используется для автоматического заполнения свойств в создаваемых токенах для файлов и версий файлов. 
manager [IFileManager](T_Tessa_Files_IFileManager.htm) (Optional)
     Объект, управляющий взаимодействием с файлами по умолчанию, или null, если используется стандартный [FileManager](T_Tessa_Files_FileManager.htm). 
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
(Optional)
     Дескриптор приложения или null, если используется дескриптор по умолчанию для конфигурации. 
## __См. также
#### Ссылки
[FileSourceForCard - ](T_Tessa_Cards_FileSourceForCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
