# ILimitedPool<T> \- интерфейс
Пул объектов, имеющих ограниченное время жизни.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILimitedPool<T> : IAsyncDisposable
VB __Копировать
     Public Interface ILimitedPool(Of T)
    	Inherits IAsyncDisposable
C++ __Копировать
    generic<typename T>
    public interface class ILimitedPool : IAsyncDisposable
F# __Копировать
     type ILimitedPool<'T> = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
#### Параметры типа
T
    Тип объектов в пуле.
##  __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[GetAsync](M_Tessa_Platform_Collections_ILimitedPool_1_GetAsync.htm)|
Получает объект из пула. Вызовите метод [!:ILimitedPoolItem<T>.DisposeAsync]
на этом объекте, чтобы вернуть его в пул.  
[SetAllExpiredAsync](M_Tessa_Platform_Collections_ILimitedPool_1_SetAllExpiredAsync.htm)|
Определяет срок всех объектов, созданных к настоящему моменту, как истёкший.
Это относится как к объектам, находящимся в пуле к текущему моменту, так и к
используемым объектам, которые не будут возвращены в пул в этом случае.  
## __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
