# CardModelSettings.SetFilePreviewIsHiddenAsync - метод
Признак того, что область предпросмотра файлов скрыта.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SetFilePreviewIsHiddenAsync(
    	bool value,
    	Func<Action, CancellationToken, Task> executePropertyChangedAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetFilePreviewIsHiddenAsync ( 
    	value As Boolean,
    	Optional executePropertyChangedAsync As Func(Of Action, CancellationToken, Task) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SetFilePreviewIsHiddenAsync(
    	bool value, 
    	Func<Action^, CancellationToken, Task^>^ executePropertyChangedAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetFilePreviewIsHiddenAsync : 
            value : bool * 
            ?executePropertyChangedAsync : Func<Action, CancellationToken, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _executePropertyChangedAsync = defaultArg executePropertyChangedAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SetFilePreviewIsHiddenAsync : 
            value : bool * 
            ?executePropertyChangedAsync : Func<Action, CancellationToken, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _executePropertyChangedAsync = defaultArg executePropertyChangedAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Устанавливаемое значение.
executePropertyChangedAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Action](https://learn.microsoft.com/dotnet/api/system.action),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
     Метод, выполняющий изменение свойства (текущий метод может быть вызван из другого потока, тогда этот метод "пробросит" выполнение в поток UI). Если параметр равен null, то изменение свойства выполняется в текущем потоке. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardModelSettings.SetFilePreviewIsHiddenAsync(Boolean, Func<Action,
CancellationToken, Task>,
CancellationToken)](M_Tessa_Cards_ICardModelSettings_SetFilePreviewIsHiddenAsync.htm)  
##  __См. также
#### Ссылки
[CardModelSettings - ](T_Tessa_Cards_CardModelSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
