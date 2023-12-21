# NumberComposer.ReserveNumberAsync - метод
Резервирует и возвращает номер заданного типа для контекста события,
происходящего с номером. Возвращает пустой номер, если действие не удалось
выполнить. Возвращённое значение не может быть равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<INumberObject> ReserveNumberAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ReserveNumberAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of INumberObject)
C++ __Копировать
     public:
    virtual Task<INumberObject^>^ ReserveNumberAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ReserveNumberAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<INumberObject> 
    override ReserveNumberAsync : 
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
#### Реализации
[INumberComposer.ReserveNumberAsync(INumberContext, NumberTypeDescriptor,
CancellationToken)](M_Tessa_Cards_Numbers_INumberComposer_ReserveNumberAsync.htm)  
##  __См. также
#### Ссылки
[NumberComposer - ](T_Tessa_Cards_Numbers_NumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
