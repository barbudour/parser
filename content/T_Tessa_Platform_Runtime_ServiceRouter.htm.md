# ServiceRouter - класс
Объект, выполняющий получение экземпляров сервисов, актуальных для текущего
или заданного маршрута. Используется на клиенте для некоторых сервисов, для
которых требуется обеспечить обратную совместимость.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ServiceRouter : IServiceRouter
VB __Копировать
     Public Class ServiceRouter
    	Implements IServiceRouter
C++ __Копировать
     public ref class ServiceRouter : IServiceRouter
F# __Копировать
     type ServiceRouter = 
        class
            interface IServiceRouter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServiceRouter
Implements
    [IServiceRouter](T_Tessa_Platform_Runtime_IServiceRouter.htm)
##  __Заметки
Классы-наследники могут переопределять поведение методов для изменения
алгоритмов резолва сервисов. Алгоритм кэширования экземпляров нельзя изменить,
для этого определите другую реализацию интерфейса
[IServiceRouter](T_Tessa_Platform_Runtime_IServiceRouter.htm).
## __Конструкторы
[ServiceRouter](M_Tessa_Platform_Runtime_ServiceRouter__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[RouteSettings](P_Tessa_Platform_Runtime_ServiceRouter_RouteSettings.htm)|
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.  
---|---  
[UnityContainer](P_Tessa_Platform_Runtime_ServiceRouter_UnityContainer.htm)|
Контейнер Unity, в котором зарегистрированы сервисы для разных маршрутов.  
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
[GetActiveService<T>](M_Tessa_Platform_Runtime_ServiceRouter_GetActiveService__1.htm)|
Возвращает экземпляр сервиса для текущего активного маршрута. Если экземпляр
не удалось получить (т.к. он не зарегистрирован), то выбрасывается исключение
[Tessa.Platform.Runtime.ServiceNotFoundException].  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetService<T>](M_Tessa_Platform_Runtime_ServiceRouter_GetService__1.htm)|
Возвращает экземпляр сервиса для заданного маршрута route. Если экземпляр не
удалось получить (т.к. он не зарегистрирован), то выбрасывается исключение
[Tessa.Platform.Runtime.ServiceNotFoundException].  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Invalidate](M_Tessa_Platform_Runtime_ServiceRouter_Invalidate.htm)|  Очищает
кэш со всеми созданными экземплярами маршрутизируемых сервисов, чтобы они
могли быть инициализированы повторно.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryResolveServiceCore<T>](M_Tessa_Platform_Runtime_ServiceRouter_TryResolveServiceCore__1.htm)|
Возвращает новый экземпляр сервиса (без учёта кэширования) для заданного
маршрута route или null, если экземпляр не удалось получить (т.к. он не
зарегистрирован).  
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
