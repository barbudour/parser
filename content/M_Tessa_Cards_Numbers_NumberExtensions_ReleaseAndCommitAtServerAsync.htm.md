# NumberExtensions.ReleaseAndCommitAtServerAsync - метод
Добавляет запись в очередь действий с номерами, которая вызовет освобождение
заданного номера number при сохранении карточки. Вторым параметром возвращает
действие, выполняемое для отмены операции по освобождению номера, или null,
если отсутствуют действия для отмены.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<(bool result, Action cancelAction)> ReleaseAndCommitAtServerAsync(
    	this INumberQueueContainer queueContainer,
    	INumberContext context,
    	INumberObject number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ReleaseAndCommitAtServerAsync ( 
    	queueContainer As INumberQueueContainer,
    	context As INumberContext,
    	number As INumberObject,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (result As Boolean, cancelAction As Action))
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValueTask<ValueTuple<bool, Action^>> ReleaseAndCommitAtServerAsync(
    	INumberQueueContainer^ queueContainer, 
    	INumberContext^ context, 
    	INumberObject^ number, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ReleaseAndCommitAtServerAsync : 
            queueContainer : INumberQueueContainer * 
            context : INumberContext * 
            number : INumberObject * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<bool, Action>> 
#### Параметры
queueContainer
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm)
     Объект, посредством которого осуществляется доступ к очереди действий с номерами. 
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
     Освобождаемый номер. Не может быть равен null. Если указан номер, не являющийся номером из последовательности, то метод не выполняет действий и возвращает false. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Action](https://learn.microsoft.com/dotnet/api/system.action)>>  
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
