# ShowCardEditorFuncAsync - делегат
Делегат для переопределения действия на открытие карточки по представлению
карточки [ShowCardAsync(ICardEditorModel, Func<ICardEditorModel,
CancellationToken, ValueTask<Boolean>>, ShowCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_ShowCardAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task<IUIContextObject> ShowCardEditorFuncAsync(
    	ICardEditorModel editor,
    	Func<ICardEditorModel, CancellationToken, ValueTask<bool>> prepareEditorActionAsync = null,
    	ShowCardOptions options = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function ShowCardEditorFuncAsync ( 
    	editor As ICardEditorModel,
    	Optional prepareEditorActionAsync As Func(Of ICardEditorModel, CancellationToken, ValueTask(Of Boolean)) = Nothing,
    	Optional options As ShowCardOptions = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IUIContextObject)
C++ __Копировать
     public delegate Task<IUIContextObject^>^ ShowCardEditorFuncAsync(
    	ICardEditorModel^ editor, 
    	Func<ICardEditorModel^, CancellationToken, ValueTask<bool>>^ prepareEditorActionAsync = nullptr, 
    	ShowCardOptions^ options = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type ShowCardEditorFuncAsync = 
        delegate of 
            editor : ICardEditorModel * 
            ?prepareEditorActionAsync : Func<ICardEditorModel, CancellationToken, ValueTask<bool>> * 
            ?options : ShowCardOptions * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _prepareEditorActionAsync = defaultArg prepareEditorActionAsync null
            let _options = defaultArg options null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IUIContextObject>
#### Параметры
editor [ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)
    Редактируемое представление карточки на клиенте.
prepareEditorActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>
(Optional)
     Метод, который подготавливает редактор карточки непосредственно перед отображением, или null, если подготовительные действия не требуется.
С помощью возврата значения false можно отменить создание UI.
Рекомендуется использовать этот метод, чтобы установить свойство редактора
[WorkspaceName](P_Tessa_UI_Cards_ICardEditorModel_WorkspaceName.htm).
options [ShowCardOptions](T_Tessa_UI_ShowCardOptions.htm) (Optional)
    Настройки отображения карточки ил значение null, если используются настройки по умолчанию.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IUIContextObject](T_Tessa_UI_IUIContextObject.htm)>  
Объект, содержащий информацию об открытой карточке или значение null, если
создание UI было отменено.
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
