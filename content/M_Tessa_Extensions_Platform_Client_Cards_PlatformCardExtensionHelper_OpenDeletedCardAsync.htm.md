# PlatformCardExtensionHelper.OpenDeletedCardAsync - метод
Выполняет просмотр удалённой карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task OpenDeletedCardAsync(
    	IUIContext context,
    	ICardRepairManager cardRepairManager,
    	IUIHost uiHost,
    	Func<ICardEditorModel> createEditorFunc,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function OpenDeletedCardAsync ( 
    	context As IUIContext,
    	cardRepairManager As ICardRepairManager,
    	uiHost As IUIHost,
    	createEditorFunc As Func(Of ICardEditorModel),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ OpenDeletedCardAsync(
    	IUIContext^ context, 
    	ICardRepairManager^ cardRepairManager, 
    	IUIHost^ uiHost, 
    	Func<ICardEditorModel^>^ createEditorFunc, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member OpenDeletedCardAsync : 
            context : IUIContext * 
            cardRepairManager : ICardRepairManager * 
            uiHost : IUIHost * 
            createEditorFunc : Func<ICardEditorModel> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context [IUIContext](T_Tessa_UI_IUIContext.htm)
    Контекст вкладки, в которой открыта удалённая карточка, просмотр которой необходимо выполнить.
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
     Объект, управляющий исправлением структуры карточки, например, вследствие изменения её типа карточки. 
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
     Объект, предоставляющий упрощённый доступ к основным функциям платформы, которые связаны с отображением информации пользователю. 
createEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
     Фабрика, создающая редактор для открываемой на просмотр удалённой карточки с параметрами по умолчанию. 
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
