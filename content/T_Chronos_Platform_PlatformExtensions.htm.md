# PlatformExtensions - класс
Методы-расширения для пространства имён Chronos.Platform.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PlatformExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class PlatformExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class PlatformExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type PlatformExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PlatformExtensions
##  __Методы
[ComputeHash](M_Chronos_Platform_PlatformExtensions_ComputeHash.htm)|
Возвращает массив байт с криптостойким хеш-значением для заданного массива
байт с данными.  
---|---  
[Get<T>](M_Chronos_Platform_PlatformExtensions_Get__1.htm)|  Возвращает
значение из хранилища IDictionary<string, object>, полученное по ключу key и
приведённое к типу T.  
[GetActualLocationFileName](M_Chronos_Platform_PlatformExtensions_GetActualLocationFileName.htm)|
Возвращает действительное местоположение сборки (обычно это местоположение до
того, как сборка была скопирована механизмом shadow copy). При этом
используется делегат
[AssemblyResolveActualLocationFunc](P_Chronos_Platform_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)
или метод
[GetLocationFileNameFromCodeBase(Assembly)](M_Chronos_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm),
если делегат не был определён.  
[GetActualLocationFolder](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm)|
Возвращает действительное местоположение сборки (обычно это местоположение до
того, как сборка была скопирована механизмом shadow copy). При этом
используется делегат
[AssemblyResolveActualLocationFunc](P_Chronos_Platform_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)
или метод
[GetLocationFolderFromCodeBase(Assembly)](M_Chronos_Platform_PlatformExtensions_GetLocationFolderFromCodeBase.htm),
если делегат не был определён.  
[GetAwaiter](M_Chronos_Platform_PlatformExtensions_GetAwaiter.htm)|
Предоставляет функциональность await для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Задача возвращает true, если ожидание handle было завершено, или false, если
ожидание завершилось таймаутом.  
[GetConstantHashCode](M_Chronos_Platform_PlatformExtensions_GetConstantHashCode.htm)|
Возвращает постоянный хеш-код для строки, значение которого не зависит от
текущего процесса.  
[GetFullText](M_Chronos_Platform_PlatformExtensions_GetFullText.htm)|
Возвращает полную информацию по заданному исключению, включая текст нескольких
исключений для
[AggregateException](https://learn.microsoft.com/dotnet/api/system.aggregateexception).
Для обычных исключений результат аналогичен вызову метода
[ToString()](https://learn.microsoft.com/dotnet/api/system.exception.tostring#system-
exception-tostring).  
[GetHashedString](M_Chronos_Platform_PlatformExtensions_GetHashedString.htm)|
Возвращает строку, содержащую криптостойкое хеш-значение от текущей строки.  
[GetLocationFileNameFromCodeBase](M_Chronos_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm)|
Возвращает полный путь к файлу сборки.  
[GetLocationFolderFromCodeBase](M_Chronos_Platform_PlatformExtensions_GetLocationFolderFromCodeBase.htm)|
Возвращает путь к папке со сборкой. Используйте метод
[GetActualLocationFolder(Assembly)](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm),
если может потребоваться глобально переопределить местоположение сборки.  
[Implements<T>](M_Chronos_Platform_PlatformExtensions_Implements__1.htm)|
Возвращает признак того, что тип реализует заданный интерфейс.  
[IsAssignableFrom<T>](M_Chronos_Platform_PlatformExtensions_IsAssignableFrom__1.htm)|
Возвращает признак того, что тип реализует заданный интерфейс.  
[LogException(ILogger, Exception,
LogLevel)](M_Chronos_Platform_PlatformExtensions_LogException.htm)|
Записывает сообщение об исключении в лог с указанием необходимых деталей.  
[LogException(ILogger, String, Exception,
LogLevel)](M_Chronos_Platform_PlatformExtensions_LogException_1.htm)|
Записывает сообщение об исключении в лог с указанием необходимых деталей.  
[ToTask](M_Chronos_Platform_PlatformExtensions_ToTask.htm)|  Создаёт задачу,
которая отмечается как завершённая, когда для
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)
сработает сигнал. Задача возвращает true, если ожидание handle было завершено,
или false, если ожидание завершилось таймаутом.  
[TryGet<T>](M_Chronos_Platform_PlatformExtensions_TryGet__1.htm)|
Возвращает либо значение из хранилища IDictionary<string, object>, полученное
по ключу key и приведённое к типу T при его наличии, либо возвращает значение
по умолчанию defaultValue, если запрошенное значение отсутствовало в
хранилище.
Внимание! Если требуется получить значение, которое может присутствовать со
значением null, но тип данных не допускает null, например, для типа int, то
пишите следующим образом: storage.TryGet<int?>("key") ?? 0  
[WaitOneAsync(WaitHandle,
CancellationToken)](M_Chronos_Platform_PlatformExtensions_WaitOneAsync_1.htm)|
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Ожидание выполняется без таймаута.  
[WaitOneAsync(WaitHandle, Int32,
CancellationToken)](M_Chronos_Platform_PlatformExtensions_WaitOneAsync.htm)|
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Возвращает признак того, что ожидание завершилось при переходе объекта
waitHandle в сигнальное состояние, а не при наступлении таймаута.  
[WaitOneAsync(WaitHandle, TimeSpan,
CancellationToken)](M_Chronos_Platform_PlatformExtensions_WaitOneAsync_2.htm)|
Асинхронно ожидает заданный объект
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
Возвращает признак того, что ожидание завершилось при переходе объекта
waitHandle в сигнальное состояние, а не при наступлении таймаута.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
