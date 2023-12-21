# NumberComposer.AcquireUnreservedNumberAsync - метод
Выделяет заданный номер без предварительного резервирования для контекста
события, происходящего с номером. Возвращает признак того, что выделение
номера успешно выполнено.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> AcquireUnreservedNumberAsync(
    	INumberContext context,
    	INumberObject number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function AcquireUnreservedNumberAsync ( 
    	context As INumberContext,
    	number As INumberObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    virtual Task<bool>^ AcquireUnreservedNumberAsync(
    	INumberContext^ context, 
    	INumberObject^ number, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract AcquireUnreservedNumberAsync : 
            context : INumberContext * 
            number : INumberObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override AcquireUnreservedNumberAsync : 
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
    Номер, который требуется выделить. Номер не должен быть зарезервирован.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если номер успешно выделен; false в противном случае.
#### Реализации
[INumberComposer.AcquireUnreservedNumberAsync(INumberContext, INumberObject,
CancellationToken)](M_Tessa_Cards_Numbers_INumberComposer_AcquireUnreservedNumberAsync.htm)  
##  __См. также
#### Ссылки
[NumberComposer - ](T_Tessa_Cards_Numbers_NumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
