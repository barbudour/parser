# IGlobalMutex - интерфейс
Мьютекс с глобально уникальным именем, используемый для синхронизации между
процессами.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGlobalMutex : IAsyncDisposable
VB __Копировать
     Public Interface IGlobalMutex
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IGlobalMutex : IAsyncDisposable
F# __Копировать
     type IGlobalMutex = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Методы
[CleanAsync](M_Tessa_Platform_IPC_IGlobalMutex_CleanAsync.htm)|  Освобождает
ресурсы мьютекса, делая невозможным его дальнейшее использование, и удаляет
связанный с ним файл при его наличии. В реализации по умолчанию выполняет
работу по очистке на Linux и игнорируется на Windows.  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[ReleaseAsync](M_Tessa_Platform_IPC_IGlobalMutex_ReleaseAsync.htm)|
Освобождает блокировку на текущий мьютекс. Не выполняет действий, если
блокировка не была взята.  
[WaitAsync](M_Tessa_Platform_IPC_IGlobalMutex_WaitAsync.htm)|  Ожидает и
получает блокировку на текущий мьютекс. После взятия блокировки её необходимо
освободить методом Release.  
## __См. также
#### Ссылки
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
