# WebProxyFactoryBase - класс
Базовый класс для фабрики объектов
[IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm) для обращения к веб-
сервисам системы.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WebProxyFactoryBase : IWebProxyFactory, 
    	IAsyncDisposable
VB __Копировать
     Public MustInherit Class WebProxyFactoryBase
    	Implements IWebProxyFactory, IAsyncDisposable
C++ __Копировать
     public ref class WebProxyFactoryBase abstract : IWebProxyFactory, 
    	IAsyncDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type WebProxyFactoryBase = 
        class
            interface IWebProxyFactory
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebProxyFactoryBase
Derived
[Tessa.Platform.Runtime.WebProxyFactory](T_Tessa_Platform_Runtime_WebProxyFactory.htm)
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IWebProxyFactory](T_Tessa_Platform_Runtime_IWebProxyFactory.htm)
##  __Конструкторы
[WebProxyFactoryBase](M_Tessa_Platform_Runtime_WebProxyFactoryBase__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[HttpClientPool](P_Tessa_Platform_Runtime_WebProxyFactoryBase_HttpClientPool.htm)|
Пул объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
---|---  
[IsDisposed](P_Tessa_Platform_Runtime_WebProxyFactoryBase_IsDisposed.htm)|
Признак того, что ресурсы объекта были освобождены.  
[UnityContainer](P_Tessa_Platform_Runtime_WebProxyFactoryBase_UnityContainer.htm)|
Контейнер Unity для создания прокси-объектов или null, если объекты создаются
конструктором по умолчанию. Для создания объектов используйте метод
[Resolve<T>()](M_Tessa_Platform_Runtime_WebProxyFactoryBase_Resolve__1.htm).  
## __Методы
[DisposeAsync()](M_Tessa_Platform_Runtime_WebProxyFactoryBase_DisposeAsync.htm)|
Освобождает ресурсы, занимаемые объектом.  
---|---  
[DisposeAsync(Boolean)](M_Tessa_Platform_Runtime_WebProxyFactoryBase_DisposeAsync_1.htm)|
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
[InitializeProxyParametersAsync](M_Tessa_Platform_Runtime_WebProxyFactoryBase_InitializeProxyParametersAsync.htm)|
Инициализирует параметры заданного прокси-объекта в соответствие с настройками
текущей фабрики. При этом могут устанавливаться такие свойства, как
[BaseUri](P_Tessa_Platform_Runtime_IWebProxy_BaseUri.htm),
[InstanceName](P_Tessa_Platform_Runtime_IWebProxy_InstanceName.htm),
[SessionTokenHolder](P_Tessa_Platform_Runtime_IWebProxy_SessionTokenHolder.htm),
[SessionVersionHolder](P_Tessa_Platform_Runtime_IWebProxy_SessionVersionHolder.htm).  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Resolve<T>](M_Tessa_Platform_Runtime_WebProxyFactoryBase_Resolve__1.htm)|
Получает или создаёт экземпляр класса прокси-объекта
[IWebProxy](T_Tessa_Platform_Runtime_IWebProxy.htm).  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UseProxyAsync<T>](M_Tessa_Platform_Runtime_WebProxyFactoryBase_UseProxyAsync__1.htm)|
Получает или создаёт потокобезопасный экземпляр прокси-объекта заданного типа
T, который инициализирован для использования.  
## __Методы расширения
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
