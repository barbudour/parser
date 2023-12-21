# PlatformCardExtensionHelper.RepairTemplateAsync - метод
Исправляет структуру карточки в шаблоне.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task RepairTemplateAsync(
    	IUIContext context,
    	ICardRepository cardRepository,
    	ICardRepairManager cardRepairManager,
    	INotificationUIManager notificationUIManager,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function RepairTemplateAsync ( 
    	context As IUIContext,
    	cardRepository As ICardRepository,
    	cardRepairManager As ICardRepairManager,
    	notificationUIManager As INotificationUIManager,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ RepairTemplateAsync(
    	IUIContext^ context, 
    	ICardRepository^ cardRepository, 
    	ICardRepairManager^ cardRepairManager, 
    	INotificationUIManager^ notificationUIManager, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member RepairTemplateAsync : 
            context : IUIContext * 
            cardRepository : ICardRepository * 
            cardRepairManager : ICardRepairManager * 
            notificationUIManager : INotificationUIManager * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [IUIContext](T_Tessa_UI_IUIContext.htm)
    Контекст с редактором, в котором открыт шаблон карточки.
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
    Репозиторий для управления карточками с расширениями.
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
    Объект, управляющий исправлением структуры карточки, например, вследствие изменения её типа карточки.
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
    Объект, управляющий отображением всплывающих уведомлений.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[PlatformCardExtensionHelper -
](T_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
