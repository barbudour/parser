# PlatformExtensions.WaitOneAsync(WaitHandle, TimeSpan, CancellationToken) -
метод
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Возвращает признак того, что ожидание завершилось при переходе объекта
waitHandle в сигнальное состояние, а не при наступлении таймаута.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> WaitOneAsync(
    	this WaitHandle waitHandle,
    	TimeSpan timeout,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WaitOneAsync ( 
    	waitHandle As WaitHandle,
    	timeout As TimeSpan,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task<bool>^ WaitOneAsync(
    	WaitHandle^ waitHandle, 
    	TimeSpan timeout, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WaitOneAsync : 
            waitHandle : WaitHandle * 
            timeout : TimeSpan * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
waitHandle
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
    Объект, ожидание которого выполняется.
timeout [TimeSpan](https://learn.microsoft.com/dotnet/api/system.timespan)
     Таймаут, в течение которого выполняется ожидание до того, как ожидание будет прервано несмотря на то, что объект waitHandle всё ещё не перешёл в сигнальное состояние. Если указано значение [InfiniteTimeSpan](https://learn.microsoft.com/dotnet/api/system.threading.timeout.infinitetimespan), то таймаут не наступает, т.е. ожидание завершится только при объекте waitHandle. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Токен отмены для асинхронного ожидания.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если ожидание завершилось при переходе объекта waitHandle в сигнальное
состояние; false, если ожидание завершилось при наступлении таймаута.
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
