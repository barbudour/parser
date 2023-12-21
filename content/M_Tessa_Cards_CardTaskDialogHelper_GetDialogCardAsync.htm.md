# CardTaskDialogHelper.GetDialogCardAsync - метод
Возвращает карточку диалога.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<Card> GetDialogCardAsync(
    	CardTask task,
    	Guid optionID,
    	Func<Guid, CancellationToken, ValueTask<Card>>? getter = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetDialogCardAsync ( 
    	task As CardTask,
    	optionID As Guid,
    	Optional getter As Func(Of Guid, CancellationToken, ValueTask(Of Card)) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Card)
C++ __Копировать
     public:
    static ValueTask<Card^> GetDialogCardAsync(
    	CardTask^ task, 
    	Guid optionID, 
    	Func<Guid, CancellationToken, ValueTask<Card^>>^ getter = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetDialogCardAsync : 
            task : CardTask * 
            optionID : Guid * 
            ?getter : Func<Guid, CancellationToken, ValueTask<Card>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _getter = defaultArg getter null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Card> 
#### Параметры
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Задание диалога.
optionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор варианта завершения задания диалога.
getter
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Card](T_Tessa_Cards_Card.htm)>>
(Optional)
    Метод обеспечивающий получение карточки диалога с временем жизни "Карточка" ([Card](T_Tessa_Cards_CardTaskDialogStoreMode.htm)). Если не задан, то метод возврати значение по умолчанию для типа.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Card](T_Tessa_Cards_Card.htm)>  
Карточка диалога или значение по умолчанию для типа, если её не удалось
получить.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
