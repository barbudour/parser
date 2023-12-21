# PlatformCardExtensionHelper.CreateFromTemplateAsync - метод
Создаёт карточку по шаблону на основании шаблона карточки и открывает её в
отдельной вкладке.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task CreateFromTemplateAsync(
    	ICardEditorModel editor,
    	ICardManager cardManager,
    	ICardUIManager cardUIManager,
    	ICardMetadata cardMetadata,
    	IUIHost uiHost,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CreateFromTemplateAsync ( 
    	editor As ICardEditorModel,
    	cardManager As ICardManager,
    	cardUIManager As ICardUIManager,
    	cardMetadata As ICardMetadata,
    	uiHost As IUIHost,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ CreateFromTemplateAsync(
    	ICardEditorModel^ editor, 
    	ICardManager^ cardManager, 
    	ICardUIManager^ cardUIManager, 
    	ICardMetadata^ cardMetadata, 
    	IUIHost^ uiHost, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CreateFromTemplateAsync : 
            editor : ICardEditorModel * 
            cardManager : ICardManager * 
            cardUIManager : ICardUIManager * 
            cardMetadata : ICardMetadata * 
            uiHost : IUIHost * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
editor [ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)
     Редактор, в котором открыт шаблон карточки. Может быть равен null, в этом случае действий не выполняется. 
cardManager [ICardManager](T_Tessa_Cards_ICardManager.htm)
    Объект, управляющий операциями с карточками.
cardUIManager [ICardUIManager](T_Tessa_UI_Cards_ICardUIManager.htm)
    Объект, предоставляющий пользовательский интерфейс для операций с карточками.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по всем типам карточек.
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
     Объект, предоставляющий упрощённый доступ к основным функциям платформы, которые связаны с отображением информации пользователю. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Метод показывает сплэш в процессе создания карточки.
## __См. также
#### Ссылки
[PlatformCardExtensionHelper -
](T_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
