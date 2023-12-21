# PlatformExtensions.WaitOneAsync(WaitHandle, CancellationToken) - метод
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Ожидание выполняется без таймаута.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task WaitOneAsync(
    	this WaitHandle waitHandle,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WaitOneAsync ( 
    	waitHandle As WaitHandle,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ WaitOneAsync(
    	WaitHandle^ waitHandle, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WaitOneAsync : 
            waitHandle : WaitHandle * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
waitHandle
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
    Объект, ожидание которого выполняется.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Токен отмены для асинхронного ожидания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
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
[WaitOneAsync -
перегрузка](Overload_Chronos_Platform_PlatformExtensions_WaitOneAsync.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
