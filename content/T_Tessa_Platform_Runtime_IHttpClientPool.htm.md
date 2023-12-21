# IHttpClientPool - интерфейс
Пул объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IHttpClientPool : ILimitedPool<HttpClient>, 
    	IAsyncDisposable
VB __Копировать
     Public Interface IHttpClientPool
    	Inherits ILimitedPool(Of HttpClient), IAsyncDisposable
C++ __Копировать
     public interface class IHttpClientPool : ILimitedPool<HttpClient^>, 
    	IAsyncDisposable
F# __Копировать
     type IHttpClientPool = 
        interface
            interface ILimitedPool<HttpClient>
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ILimitedPool](T_Tessa_Platform_Collections_ILimitedPool_1.htm)<[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)>
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
(Унаследован от
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm))  
[SetAllExpiredAsync](M_Tessa_Platform_Collections_ILimitedPool_1_SetAllExpiredAsync.htm)|
Определяет срок всех объектов, созданных к настоящему моменту, как истёкший.
Это относится как к объектам, находящимся в пуле к текущему моменту, так и к
используемым объектам, которые не будут возвращены в пул в этом случае.  
(Унаследован от
[ILimitedPool<T>](T_Tessa_Platform_Collections_ILimitedPool_1.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
