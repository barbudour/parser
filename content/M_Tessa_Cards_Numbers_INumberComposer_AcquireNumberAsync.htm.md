# INumberComposer.AcquireNumberAsync - метод
Выделяет и возвращает очередной номер заданного типа без предварительного
резервирования для контекста события, происходящего с номером. Возвращает
пустой номер, если действие не удалось выполнить. Возвращённое значение не
может быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<INumberObject> AcquireNumberAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function AcquireNumberAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of INumberObject)
C++ __Копировать
    Task<INumberObject^>^ AcquireNumberAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract AcquireNumberAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<INumberObject> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера, для которого требуется выделить очередной номер.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Выделенный номер заданного типа для контекста события, происходящего с
номером, или пустой номер, если действие не удалось выполнить.
## __См. также
#### Ссылки
[INumberComposer - ](T_Tessa_Cards_Numbers_INumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
