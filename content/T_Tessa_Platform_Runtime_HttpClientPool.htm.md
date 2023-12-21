# HttpClientPool - класс
Пул объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class HttpClientPool : LimitedPool<HttpClient>, 
    	IHttpClientPool, ILimitedPool<HttpClient>, IAsyncDisposable
VB __Копировать
     Public Class HttpClientPool
    	Inherits LimitedPool(Of HttpClient)
    	Implements IHttpClientPool, ILimitedPool(Of HttpClient), 
    	IAsyncDisposable
C++ __Копировать
     public ref class HttpClientPool : public LimitedPool<HttpClient^>, 
    	IHttpClientPool, ILimitedPool<HttpClient^>, IAsyncDisposable
F# __Копировать
     type HttpClientPool = 
        class
            inherit LimitedPool<HttpClient>
            interface IHttpClientPool
            interface ILimitedPool<HttpClient>
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LimitedPool](T_Tessa_Platform_Collections_LimitedPool_1.htm)<[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)> __ HttpClientPool
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ILimitedPool](T_Tessa_Platform_Collections_ILimitedPool_1.htm)<[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)>, [IHttpClientPool](T_Tessa_Platform_Runtime_IHttpClientPool.htm)
##  __Конструкторы
[HttpClientPool(Nullable<TimeSpan>)](M_Tessa_Platform_Runtime_HttpClientPool__ctor.htm)|
Создаёт экземпляр класса с указанием времени жизни объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
---|---  
[HttpClientPool(IConnectionSettings,
Nullable<TimeSpan>)](M_Tessa_Platform_Runtime_HttpClientPool__ctor_1.htm)|
Создаёт экземпляр класса с указанием настроек соединения и времени жизни
объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
[HttpClientPool(IConnectionSettings, IHttpClientFactory,
Nullable<TimeSpan>)](M_Tessa_Platform_Runtime_HttpClientPool__ctor_2.htm)|
Создаёт экземпляр класса с указанием настроек соединения и времени жизни
объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
## __Свойства
[ExpirationTokenSource](P_Tessa_Platform_Collections_LimitedPool_1_ExpirationTokenSource.htm)|
Объект, по которому токены определяют признак того, что время жизни объектов в
пуле истекло, которые были созданы по этому же источнику
[LimitedPoolExpirationTokenSource](T_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource.htm).  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
---|---  
[IdleCount](P_Tessa_Platform_Collections_LimitedPool_1_IdleCount.htm)|
Количество объектов в пуле, ожидающих повторного использования. Срок жизни
некоторых из этих объектов может быть уже завершён, т.е. при попытке
переиспользовать их будет выполнено повторное создание.  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
[IsDisposed](P_Tessa_Platform_Collections_LimitedPool_1_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
##  __Методы
[DisposeAsync()](M_Tessa_Platform_Collections_LimitedPool_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
---|---  
[DisposeAsync(Boolean)](M_Tessa_Platform_Collections_LimitedPool_1_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetAsync](M_Tessa_Platform_Collections_LimitedPool_1_GetAsync.htm)|  Получает
объект из пула. Вызовите метод [!:ILimitedPoolItem<T>.DisposeAsync] на этом
объекте, чтобы вернуть его в пул.  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetAllExpiredAsync](M_Tessa_Platform_Collections_LimitedPool_1_SetAllExpiredAsync.htm)|
Определяет срок всех объектов, созданных к настоящему моменту, как истёкший.
Это относится как к объектам, находящимся в пуле к текущему моменту, так и к
используемым объектам, которые не будут возвращены в пул в этом случае.  
(Унаследован от
[LimitedPool<T>](T_Tessa_Platform_Collections_LimitedPool_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
