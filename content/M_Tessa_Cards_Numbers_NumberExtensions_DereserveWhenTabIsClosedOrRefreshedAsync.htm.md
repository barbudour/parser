# NumberExtensions.DereserveWhenTabIsClosedOrRefreshedAsync - метод
Добавляет запись в очередь действий с номерами, которая вызовет
дерезервирование заданного номера number при закрытии вкладки карточки или при
её переоткрытии (например, в процессе сохранения).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> DereserveWhenTabIsClosedOrRefreshedAsync(
    	this INumberQueueContainer queueContainer,
    	INumberContext context,
    	INumberObject number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function DereserveWhenTabIsClosedOrRefreshedAsync ( 
    	queueContainer As INumberQueueContainer,
    	context As INumberContext,
    	number As INumberObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<bool> DereserveWhenTabIsClosedOrRefreshedAsync(
    	INumberQueueContainer^ queueContainer, 
    	INumberContext^ context, 
    	INumberObject^ number, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member DereserveWhenTabIsClosedOrRefreshedAsync : 
            queueContainer : INumberQueueContainer * 
            context : INumberContext * 
            number : INumberObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
queueContainer
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm)
     Объект, посредством которого осуществляется доступ к очереди действий с номерами. 
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
     Дерезервируемый номер. Не может быть равен null. Если указан номер, не являющийся номером из последовательности, то метод не выполняет действий и возвращает false. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если обработка события успешно выполнена; false, если обработка события
была отменена или при выполнении обработки возникли ошибки.
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
