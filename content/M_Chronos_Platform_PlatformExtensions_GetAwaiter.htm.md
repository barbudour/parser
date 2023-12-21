# PlatformExtensions.GetAwaiter - метод
Предоставляет функциональность await для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Задача возвращает true, если ожидание handle было завершено, или false, если
ожидание завершилось таймаутом.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static TaskAwaiter<bool> GetAwaiter(
    	this WaitHandle handle
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetAwaiter ( 
    	handle As WaitHandle
    ) As TaskAwaiter(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static TaskAwaiter<bool> GetAwaiter(
    	WaitHandle^ handle
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetAwaiter : 
            handle : WaitHandle -> TaskAwaiter<bool> 
#### Параметры
handle
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
    Объект, ожидание которого выполнятеся.
#### Возвращаемое значение
[TaskAwaiter](https://learn.microsoft.com/dotnet/api/system.runtime.compilerservices.taskawaiter-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Объект, предоставляющий функциональность await.
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
##  __См. также
#### Ссылки
[PlatformExtensions - ](T_Chronos_Platform_PlatformExtensions.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
