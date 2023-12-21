# IGlobalStorage - интерфейс
Хранилище данных, обычно располагающееся в памяти, содержимое которого
разделяется между процессами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGlobalStorage : IAsyncDisposable
VB __Копировать
     Public Interface IGlobalStorage
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IGlobalStorage : IAsyncDisposable
F# __Копировать
     type IGlobalStorage = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[OpenAsync](M_Tessa_Platform_IPC_IGlobalStorage_OpenAsync.htm)|  Открывает
разделяемое хранилище для записи или чтения. При необходимости некоторое время
ожидается снятие блокировки от других процессов.  
## __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
