# IAsyncReaderWriterLock - интерфейс
Объект, обеспечивающий блокировки на чтение и запись. Объект можно получить из
Unity как PerResolve зависимость.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAsyncReaderWriterLock
VB __Копировать
     Public Interface IAsyncReaderWriterLock
C++ __Копировать
     public interface class IAsyncReaderWriterLock
F# __Копировать
     type IAsyncReaderWriterLock = interface end
##  __Методы
[ReaderLockAsync](M_Tessa_Platform_IAsyncReaderWriterLock_ReaderLockAsync.htm)|
Выполняет взятие блокировки на чтение. Ожидает освобождения блокировки на
запись, если она была взята. Внимание! Не вызывайте метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) у возвращённого объекта более одного раза. Рекомендуется
использовать конструкцию using и не обращаться к возвращаемому объекту
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
другим образом.  
---|---  
[WriterLockAsync](M_Tessa_Platform_IAsyncReaderWriterLock_WriterLockAsync.htm)|
Выполняет взятие эксклюзивной блокировки на запись. Ожидает освобождения всех
блокировок на чтение или параллельной блокировки на запись, если они были
взяты. Внимание! Не вызывайте метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) у возвращённого объекта более одного раза. Рекомендуется
использовать конструкцию using и не обращаться к возвращаемому объекту
[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
другим образом.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
