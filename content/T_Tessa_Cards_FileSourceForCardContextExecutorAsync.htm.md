# FileSourceForCardContextExecutorAsync - делегат
Выполняет действие в контексте карточки с указанием имени карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ValueTask FileSourceForCardContextExecutorAsync(
    	Func<string, CancellationToken, ValueTask> actionAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Delegate Function FileSourceForCardContextExecutorAsync ( 
    	actionAsync As Func(Of String, CancellationToken, ValueTask),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public delegate ValueTask FileSourceForCardContextExecutorAsync(
    	Func<String^, CancellationToken, ValueTask>^ actionAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     type FileSourceForCardContextExecutorAsync = 
        delegate of 
            actionAsync : Func<string, CancellationToken, ValueTask> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask
#### Параметры
actionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
     Выполняемое действие, которое получает имя карточки в качестве параметра. Действие не равно null. Передаваемое имя карточки может быть равно null или пустой строке, если имя неизвестно. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
