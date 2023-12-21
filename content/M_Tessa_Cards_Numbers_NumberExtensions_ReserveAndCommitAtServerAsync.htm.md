# NumberExtensions.ReserveAndCommitAtServerAsync - метод
Резервирует номер заданного типа и добавляет запись в очередь действий с
номерами, которая вызовет выделение номера при сохранении карточки. Возвращает
зарезервированный номер или пустой номер, если зарезервировать номер не
удалось или в процессе выполнения произошли ошибки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<INumberObject> ReserveAndCommitAtServerAsync(
    	this INumberQueueContainer queueContainer,
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	SessionType? sessionType = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ReserveAndCommitAtServerAsync ( 
    	queueContainer As INumberQueueContainer,
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional sessionType As SessionType? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of INumberObject)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<INumberObject^>^ ReserveAndCommitAtServerAsync(
    	INumberQueueContainer^ queueContainer, 
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	Nullable<SessionType> sessionType = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ReserveAndCommitAtServerAsync : 
            queueContainer : INumberQueueContainer * 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?sessionType : Nullable<SessionType> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _sessionType = defaultArg sessionType null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<INumberObject> 
#### Параметры
queueContainer
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm)
     Объект, посредством которого осуществляется доступ к очереди действий с номерами. 
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
     Тип номера, который будет зарезервирован. Не может быть равен null. 
sessionType
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[SessionType](T_Tessa_Platform_Runtime_SessionType.htm)>
(Optional)
     Тип сессии, который используется вместо актуального из объекта сессии, или null, если используется тип сессии из context.Session. Рекомендуется указывать только в таких ситуациях, когда на сервере необходимо зарезервировать номер для отправки его на клиент. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Непустой зарезервированный номер, если обработка события успешно выполнена;
пустой номер, если обработка события была отменена или при выполнении
обработки возникли ошибки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
