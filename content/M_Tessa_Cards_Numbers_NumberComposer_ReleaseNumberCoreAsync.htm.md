# NumberComposer.ReleaseNumberCoreAsync - метод
Освобождает заданный выделенный или зарезервированный номер для контекста
события, происходящего с номером. Возвращает признак того, что освобождение
номера успешно выполнено.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<bool> ReleaseNumberCoreAsync(
    	INumberContext context,
    	INumberObject number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function ReleaseNumberCoreAsync ( 
    	context As INumberContext,
    	number As INumberObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     protected:
    virtual Task<bool>^ ReleaseNumberCoreAsync(
    	INumberContext^ context, 
    	INumberObject^ number, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReleaseNumberCoreAsync : 
            context : INumberContext * 
            number : INumberObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
    override ReleaseNumberCoreAsync : 
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
    Номер, который требуется освободить. Номер может быть зарезервирован или выделен.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если номер успешно освобождён; false в противном случае.
## __См. также
#### Ссылки
[NumberComposer - ](T_Tessa_Cards_Numbers_NumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
