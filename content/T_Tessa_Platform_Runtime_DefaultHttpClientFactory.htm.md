# DefaultHttpClientFactory - класс
Фабрика объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient),
которая использует настройки платформы по умолчанию
[ITessaPlatformDependencies](T_Tessa_Platform_ITessaPlatformDependencies.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DefaultHttpClientFactory : IHttpClientFactory
VB __Копировать
     Public Class DefaultHttpClientFactory
    	Implements IHttpClientFactory
C++ __Копировать
     public ref class DefaultHttpClientFactory : IHttpClientFactory
F# __Копировать
     type DefaultHttpClientFactory = 
        class
            interface IHttpClientFactory
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultHttpClientFactory
Implements
    [IHttpClientFactory](T_Tessa_Platform_Runtime_IHttpClientFactory.htm)
##  __Конструкторы
[DefaultHttpClientFactory()](M_Tessa_Platform_Runtime_DefaultHttpClientFactory__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию. Используются зависимости
[Dependencies](P_Tessa_Platform_TessaPlatform_Dependencies.htm).  
---|---  
[DefaultHttpClientFactory(Func<ITessaPlatformDependencies>)](M_Tessa_Platform_Runtime_DefaultHttpClientFactory__ctor_1.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
## __Свойства
[GetDependenciesFunc](P_Tessa_Platform_Runtime_DefaultHttpClientFactory_GetDependenciesFunc.htm)|
Настройки платформы по умолчанию, используемые для создания объектов
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient).  
---|---  
## __Методы
[CreateHttpClient](M_Tessa_Platform_Runtime_DefaultHttpClientFactory_CreateHttpClient.htm)|
Создаёт объект
[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)
для взаимодействия с веб-сервисами на основании объекта с настройками.  
---|---  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
