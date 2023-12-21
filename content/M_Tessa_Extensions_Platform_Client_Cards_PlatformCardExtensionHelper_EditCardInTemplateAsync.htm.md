# PlatformCardExtensionHelper.EditCardInTemplateAsync - метод
Запускает редактирование карточки в шаблоне для текущего объекта редактора
editor, в котором должен быть открыт шаблон карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task EditCardInTemplateAsync(
    	ICardEditorModel editor,
    	ICardUIManager cardUIManager,
    	IUIHost uiHost,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function EditCardInTemplateAsync ( 
    	editor As ICardEditorModel,
    	cardUIManager As ICardUIManager,
    	uiHost As IUIHost,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ EditCardInTemplateAsync(
    	ICardEditorModel^ editor, 
    	ICardUIManager^ cardUIManager, 
    	IUIHost^ uiHost, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member EditCardInTemplateAsync : 
            editor : ICardEditorModel * 
            cardUIManager : ICardUIManager * 
            uiHost : IUIHost * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
editor [ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)
     Редактор, в котором открыт шаблон карточки. Может быть равен null, в этом случае действий не выполняется. 
cardUIManager [ICardUIManager](T_Tessa_UI_Cards_ICardUIManager.htm)
    Объект, предоставляющий пользовательский интерфейс для операций с карточками.
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
     Объект, предоставляющий упрощённый доступ к основным функциям платформы, которые связаны с отображением информации пользователю. 
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
