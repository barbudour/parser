# LimitedPool<T> \- класс
Пул объектов, имеющих ограниченное время жизни.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class LimitedPool<T> : ILimitedPool<T>, 
    	IAsyncDisposable
    where T : class
VB __Копировать
     Public Class LimitedPool(Of T As Class)
    	Implements ILimitedPool(Of T), IAsyncDisposable
C++ __Копировать
    generic<typename T>
    where T : ref class
    public ref class LimitedPool : ILimitedPool<T>, 
    	IAsyncDisposable
F# __Копировать
     type LimitedPool<'T when 'T : not struct> = 
        class
            interface ILimitedPool<'T>
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LimitedPool<T>
Derived
[Tessa.Platform.Runtime.HttpClientPool](T_Tessa_Platform_Runtime_HttpClientPool.htm)
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ILimitedPool](T_Tessa_Platform_Collections_ILimitedPool_1.htm)<T>
#### Параметры типа
T
    Тип объектов в пуле.
##  __Конструкторы
[LimitedPool<T>](M_Tessa_Platform_Collections_LimitedPool_1__ctor.htm)|
Создаёт экземпляр класса с указанием параметров по жизненному циклу.  
---|---  
## __Свойства
[ExpirationTokenSource](P_Tessa_Platform_Collections_LimitedPool_1_ExpirationTokenSource.htm)|
Объект, по которому токены определяют признак того, что время жизни объектов в
пуле истекло, которые были созданы по этому же источнику
[LimitedPoolExpirationTokenSource](T_Tessa_Platform_Collections_LimitedPoolExpirationTokenSource.htm).  
---|---  
[IdleCount](P_Tessa_Platform_Collections_LimitedPool_1_IdleCount.htm)|
Количество объектов в пуле, ожидающих повторного использования. Срок жизни
некоторых из этих объектов может быть уже завершён, т.е. при попытке
переиспользовать их будет выполнено повторное создание.  
[IsDisposed](P_Tessa_Platform_Collections_LimitedPool_1_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
##  __Методы
[DisposeAsync()](M_Tessa_Platform_Collections_LimitedPool_1_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync(Boolean)](M_Tessa_Platform_Collections_LimitedPool_1_DisposeAsync_1.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
