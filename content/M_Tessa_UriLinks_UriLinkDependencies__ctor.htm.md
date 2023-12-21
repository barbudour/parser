# UriLinkDependencies - конструктор
Создает экземпляр объекта
[UriLinkDependencies](T_Tessa_UriLinks_UriLinkDependencies.htm).
## __Definition
 **Пространство имён:** [Tessa.UriLinks](N_Tessa_UriLinks.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public UriLinkDependencies(
    	IUriLinkHandler uriLinkHandler,
    	UIContextExecutorAsync? uiContextExecutor = null
    )
VB __Копировать
     Public Sub New ( 
    	uriLinkHandler As IUriLinkHandler,
    	Optional uiContextExecutor As UIContextExecutorAsync = Nothing
    )
C++ __Копировать
     public:
    UriLinkDependencies(
    	IUriLinkHandler^ uriLinkHandler, 
    	UIContextExecutorAsync^ uiContextExecutor = nullptr
    )
F# __Копировать
     new : 
            uriLinkHandler : IUriLinkHandler * 
            ?uiContextExecutor : UIContextExecutorAsync 
    (* Defaults:
            let _uiContextExecutor = defaultArg uiContextExecutor null
    *)
    -> UriLinkDependencies
#### Параметры
uriLinkHandler [IUriLinkHandler](T_Tessa_UriLinks_IUriLinkHandler.htm)
    [IUriLinkHandler](T_Tessa_UriLinks_IUriLinkHandler.htm).
uiContextExecutor
[UIContextExecutorAsync](T_Tessa_UI_UIContextExecutorAsync.htm) (Optional)
    [UIContextExecutorAsync](T_Tessa_UI_UIContextExecutorAsync.htm), может быть равен null, в этом случае будет использован [UnknownContextExecutorAsync(Func<IUIContext, CancellationToken, ValueTask>, CancellationToken)](M_Tessa_UI_UIHelper_UnknownContextExecutorAsync.htm). 
## __См. также
#### Ссылки
[UriLinkDependencies - ](T_Tessa_UriLinks_UriLinkDependencies.htm)
[Tessa.UriLinks - пространство имён](N_Tessa_UriLinks.htm)
