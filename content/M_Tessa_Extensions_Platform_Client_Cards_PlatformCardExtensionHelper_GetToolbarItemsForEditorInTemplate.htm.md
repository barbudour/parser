# PlatformCardExtensionHelper.GetToolbarItemsForEditorInTemplate - метод
Создаёт список действий на верхней панели тулбара для карточки, редактируемой
в шаблоне.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Cards](N_Tessa_Extensions_Platform_Client_Cards.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<CardToolbarAction> GetToolbarItemsForEditorInTemplate(
    	ICardEditorModel editor,
    	ICardUIManager cardUIManager,
    	IUIHost uiHost
    )
VB __Копировать
     Public Shared Function GetToolbarItemsForEditorInTemplate ( 
    	editor As ICardEditorModel,
    	cardUIManager As ICardUIManager,
    	uiHost As IUIHost
    ) As List(Of CardToolbarAction)
C++ __Копировать
     public:
    static List<CardToolbarAction^>^ GetToolbarItemsForEditorInTemplate(
    	ICardEditorModel^ editor, 
    	ICardUIManager^ cardUIManager, 
    	IUIHost^ uiHost
    )
F# __Копировать
     static member GetToolbarItemsForEditorInTemplate : 
            editor : ICardEditorModel * 
            cardUIManager : ICardUIManager * 
            uiHost : IUIHost -> List<CardToolbarAction> 
#### Параметры
editor [ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)
    Редактор, в котором открыта карточка, редактируемая в шаблоне.
cardUIManager [ICardUIManager](T_Tessa_UI_Cards_ICardUIManager.htm)
    Объект, предоставляющий пользовательский интерфейс для операций с карточками.
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
     Объект, предоставляющий упрощённый доступ к основным функциям платформы, которые связаны с отображением информации пользователю. 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardToolbarAction](T_Tessa_UI_Cards_CardToolbarAction.htm)>  
Список действий на верхней панели тулбара.
##  __См. также
#### Ссылки
[PlatformCardExtensionHelper -
](T_Tessa_Extensions_Platform_Client_Cards_PlatformCardExtensionHelper.htm)
[Tessa.Extensions.Platform.Client.Cards - пространство
имён](N_Tessa_Extensions_Platform_Client_Cards.htm)
