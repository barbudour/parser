# ClientInitializationCacheProvider - класс
Объект, предоставляющий средства для сохранения информации по инициализации в
локальном кэше приложения и для загрузки этой информации из кэша.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ClientInitializationCacheProvider : IClientInitializationCacheProvider
VB __Копировать
     Public Class ClientInitializationCacheProvider
    	Implements IClientInitializationCacheProvider
C++ __Копировать
     public ref class ClientInitializationCacheProvider : IClientInitializationCacheProvider
F# __Копировать
     type ClientInitializationCacheProvider = 
        class
            interface IClientInitializationCacheProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientInitializationCacheProvider
Implements
    [IClientInitializationCacheProvider](T_Tessa_Platform_Initialization_IClientInitializationCacheProvider.htm)
##  __Конструкторы
[ClientInitializationCacheProvider](M_Tessa_Platform_Initialization_ClientInitializationCacheProvider__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[Application](P_Tessa_Platform_Initialization_ClientInitializationCacheProvider_Application.htm)|
Объект приложения, содержащий параметры запуска приложения, или null, если
приложение с параметрами недоступно.  
---|---  
[ApplicationDescriptor](P_Tessa_Platform_Initialization_ClientInitializationCacheProvider_ApplicationDescriptor.htm)|
Объект, описывающий текущее приложение.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetMetadataRootedPath](M_Tessa_Platform_Initialization_ClientInitializationCacheProvider_GetMetadataRootedPath.htm)|
Возвращает полный путь к файлу с кэшом метаинформации.  
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
[SaveResponseAsync](M_Tessa_Platform_Initialization_ClientInitializationCacheProvider_SaveResponseAsync.htm)|
Сохраняет ответ на запрос по инициализации в локальном кэше приложения.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryLoadResponseAsync](M_Tessa_Platform_Initialization_ClientInitializationCacheProvider_TryLoadResponseAsync.htm)|
Загружает ответ на запрос по инициализации из локального кэша приложения.
Возвращает null, если ответ на запрос отсутствует в кэше.  
## __Поля
[MetadataFileName](F_Tessa_Platform_Initialization_ClientInitializationCacheProvider_MetadataFileName.htm)|
Имя файла по умолчанию с метаинформацией приложения, которое располагается в
папке кэша приложения. Может быть переопределено параметром
[MetadataCacheFilePath](P_Tessa_Platform_Runtime_IApplicationParameters_MetadataCacheFilePath.htm).  
---|---  
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
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
