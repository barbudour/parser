# ViewTileExtension - конструктор
Initializes a new instance of the
[ViewTileExtension](T_Tessa_Extensions_Platform_Client_Tiles_ViewTileExtension.htm)
class.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ViewTileExtension(
    	[NotNullAttribute] Func<SearchQueryManageDialog> searchQueriesDialogFactory,
    	[NotNullAttribute] ICardRepository cardRepository,
    	[NotNullAttribute] ICardMetadata cardMetadata,
    	[NotNullAttribute] ICardManager cardManager,
    	[NotNullAttribute] ICardRepairManager cardRepairManager,
    	[NotNullAttribute] INotificationUIManager notificationUIManager,
    	[NotNullAttribute] ISessionClient sessionClient,
    	[NotNullAttribute] IOperationRepository operationRepository,
    	[NotNullAttribute] ISession session,
    	[NotNullAttribute] IDialogService dialogService,
    	[NotNullAttribute] IViewDataExporter[] exporters,
    	[NotNullAttribute] IForumProvider forumProviders,
    	[NotNullAttribute] IForumDialogManager forumDialogManager,
    	[NotNullAttribute] IForumPermissionsProvider permissionsProvider
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> searchQueriesDialogFactory As Func(Of SearchQueryManageDialog),
    	<NotNullAttribute> cardRepository As ICardRepository,
    	<NotNullAttribute> cardMetadata As ICardMetadata,
    	<NotNullAttribute> cardManager As ICardManager,
    	<NotNullAttribute> cardRepairManager As ICardRepairManager,
    	<NotNullAttribute> notificationUIManager As INotificationUIManager,
    	<NotNullAttribute> sessionClient As ISessionClient,
    	<NotNullAttribute> operationRepository As IOperationRepository,
    	<NotNullAttribute> session As ISession,
    	<NotNullAttribute> dialogService As IDialogService,
    	<NotNullAttribute> exporters As IViewDataExporter(),
    	<NotNullAttribute> forumProviders As IForumProvider,
    	<NotNullAttribute> forumDialogManager As IForumDialogManager,
    	<NotNullAttribute> permissionsProvider As IForumPermissionsProvider
    )
C++ __Копировать
     public:
    ViewTileExtension(
    	[NotNullAttribute] Func<SearchQueryManageDialog^>^ searchQueriesDialogFactory, 
    	[NotNullAttribute] ICardRepository^ cardRepository, 
    	[NotNullAttribute] ICardMetadata^ cardMetadata, 
    	[NotNullAttribute] ICardManager^ cardManager, 
    	[NotNullAttribute] ICardRepairManager^ cardRepairManager, 
    	[NotNullAttribute] INotificationUIManager^ notificationUIManager, 
    	[NotNullAttribute] ISessionClient^ sessionClient, 
    	[NotNullAttribute] IOperationRepository^ operationRepository, 
    	[NotNullAttribute] ISession^ session, 
    	[NotNullAttribute] IDialogService^ dialogService, 
    	[NotNullAttribute] array<IViewDataExporter^>^ exporters, 
    	[NotNullAttribute] IForumProvider^ forumProviders, 
    	[NotNullAttribute] IForumDialogManager^ forumDialogManager, 
    	[NotNullAttribute] IForumPermissionsProvider^ permissionsProvider
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] searchQueriesDialogFactory : Func<SearchQueryManageDialog> * 
            [<NotNullAttribute>] cardRepository : ICardRepository * 
            [<NotNullAttribute>] cardMetadata : ICardMetadata * 
            [<NotNullAttribute>] cardManager : ICardManager * 
            [<NotNullAttribute>] cardRepairManager : ICardRepairManager * 
            [<NotNullAttribute>] notificationUIManager : INotificationUIManager * 
            [<NotNullAttribute>] sessionClient : ISessionClient * 
            [<NotNullAttribute>] operationRepository : IOperationRepository * 
            [<NotNullAttribute>] session : ISession * 
            [<NotNullAttribute>] dialogService : IDialogService * 
            [<NotNullAttribute>] exporters : IViewDataExporter[] * 
            [<NotNullAttribute>] forumProviders : IForumProvider * 
            [<NotNullAttribute>] forumDialogManager : IForumDialogManager * 
            [<NotNullAttribute>] permissionsProvider : IForumPermissionsProvider -> ViewTileExtension
#### Параметры
searchQueriesDialogFactory
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[SearchQueryManageDialog](T_Tessa_UI_Views_SearchQueryManageDialog.htm)>
     Фабрика создания диалога поисковых запросов 
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий карточек 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
     Метаданные карточек 
cardManager [ICardManager](T_Tessa_Cards_ICardManager.htm)
     Диспетчер карточек 
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
     Объект управляющий восстановлением структуры карточек 
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
     Объект, управляющий отображением всплывающих уведомлений 
sessionClient [ISessionClient](T_Tessa_Platform_Runtime_ISessionClient.htm)
     Объект, обеспечивающий взаимодействие с сессиями на клиенте. 
operationRepository
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm)
     Репозиторий, управляющий операциями. 
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
     Текущая сессия 
dialogService [IDialogService](T_Tessa_UI_Controls_IDialogService.htm)
     Сервис диалогов 
exporters [IViewDataExporter](T_Tessa_UI_Views_Export_IViewDataExporter.htm)[]
     Список экспортеров данных 
forumProviders [IForumProvider](T_Tessa_Forums_IForumProvider.htm)
     Провайдер для работы с форумами 
forumDialogManager
[IForumDialogManager](T_Tessa_UI_Controls_Forums_IForumDialogManager.htm)
     Менеджер для работы с диалоговыми окнами для форума 
permissionsProvider
[IForumPermissionsProvider](T_Tessa_Forums_IForumPermissionsProvider.htm)
     Провайдер для работы с правами досутупа в системе форумов 
## __См. также
#### Ссылки
[ViewTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_ViewTileExtension.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
