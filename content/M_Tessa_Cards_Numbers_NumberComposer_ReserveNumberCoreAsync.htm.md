# NumberComposer.ReserveNumberCoreAsync - метод
Резервирует и возвращает номер заданного типа для контекста события,
происходящего с номером. Возвращает пустой номер, если действие не удалось
выполнить. Возвращённое значение не может быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<INumberObject> ReserveNumberCoreAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function ReserveNumberCoreAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of INumberObject)
C++ __Копировать
     protected:
    virtual Task<INumberObject^>^ ReserveNumberCoreAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ReserveNumberCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<INumberObject> 
    override ReserveNumberCoreAsync : 
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
    Тип номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Номер заданного типа, зарезервированный для контекста действий с номером, или
пустой номер, если действие не удалось выполнить.
## __См. также
#### Ссылки
[NumberComposer - ](T_Tessa_Cards_Numbers_NumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
