# PlatformExtensions.ToTask - метод
Создаёт задачу, которая отмечается как завершённая, когда для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
сработает сигнал. Задача возвращает true, если ожидание handle было завершено,
или false, если ожидание завершилось таймаутом.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> ToTask(
    	this WaitHandle handle,
    	TimeSpan? timeout = null
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ToTask ( 
    	handle As WaitHandle,
    	Optional timeout As TimeSpan? = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<bool>^ ToTask(
    	WaitHandle^ handle, 
    	Nullable<TimeSpan> timeout = nullptr
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ToTask : 
            handle : WaitHandle * 
            ?timeout : Nullable<TimeSpan> 
    (* Defaults:
            let _timeout = defaultArg timeout null
    *)
    -> Task<bool> 
#### Параметры
handle
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
    Объект, ожидание которого выполняет задача.
timeout
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)>
(Optional)
    Таймаут ожидания или null, если таймаут отсутствует.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Задача, которая отмечается как завершённая, когда для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
сработает сигнал..
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Заметки
Имеется небольшая задержка между срабатыванием сигнала и отметкой задачи как
завершённой.
## __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
