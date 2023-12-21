# INumberComposer.DereserveNumberAsync - метод
Дерезервирует заданный номер для контекста события, происходящего с номером.
Возвращает признак того, что дерезервирование номера успешно выполнено.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> DereserveNumberAsync(
    	INumberContext context,
    	INumberObject number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function DereserveNumberAsync ( 
    	context As INumberContext,
    	number As INumberObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ DereserveNumberAsync(
    	INumberContext^ context, 
    	INumberObject^ number, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract DereserveNumberAsync : 
            context : INumberContext * 
            number : INumberObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Номер, который требуется дерезервировать. Номер должен быть зарезервирован.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если номер успешно дерезервирован; false в противном случае.
## __См. также
#### Ссылки
[INumberComposer - ](T_Tessa_Cards_Numbers_INumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
