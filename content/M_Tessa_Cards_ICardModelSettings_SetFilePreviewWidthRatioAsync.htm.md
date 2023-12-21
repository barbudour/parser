# ICardModelSettings.SetFilePreviewWidthRatioAsync - метод
Отношение ширины области предпросмотра к суммарной ширине области карточки и
области предпросмотра.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SetFilePreviewWidthRatioAsync(
    	double value,
    	Func<Action, CancellationToken, Task> executePropertyChangedAsync = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetFilePreviewWidthRatioAsync ( 
    	value As Double,
    	Optional executePropertyChangedAsync As Func(Of Action, CancellationToken, Task) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SetFilePreviewWidthRatioAsync(
    	double value, 
    	Func<Action^, CancellationToken, Task^>^ executePropertyChangedAsync = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetFilePreviewWidthRatioAsync : 
            value : float * 
            ?executePropertyChangedAsync : Func<Action, CancellationToken, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _executePropertyChangedAsync = defaultArg executePropertyChangedAsync null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
value [Double](https://learn.microsoft.com/dotnet/api/system.double)
     Устанавливаемое значение. Значение должно располагаться на отрезке [0;1]. Значение 0.5 означает, что области распределены в равных долях, а значение 0.25 определяет, что ширина области предпросмотра в три раза меньше, чем область карточки. 
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
##  __См. также
#### Ссылки
[ICardModelSettings - ](T_Tessa_Cards_ICardModelSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)