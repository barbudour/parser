# DefaultChronosPlatformDependencies - класс
Зависимости платформы по умолчанию, которые зависят от операционной системы,
исполняющей среды .NET и др. В этом классе указываются значения, не связанные
с конкретной платформой. Рекомендуется использовать наследника этого класса,
который определяет зависимости для Windows, Linux и др. платформ.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public class DefaultChronosPlatformDependencies : IChronosPlatformDependencies
VB __Копировать
     Public Class DefaultChronosPlatformDependencies
    	Implements IChronosPlatformDependencies
C++ __Копировать
     public ref class DefaultChronosPlatformDependencies : IChronosPlatformDependencies
F# __Копировать
     type DefaultChronosPlatformDependencies = 
        class
            interface IChronosPlatformDependencies
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultChronosPlatformDependencies
Derived
[Chronos.Platform.LinuxChronosPlatformDependencies](T_Chronos_Platform_LinuxChronosPlatformDependencies.htm)
Implements
    [IChronosPlatformDependencies](T_Chronos_Platform_IChronosPlatformDependencies.htm)
##  __Конструкторы
[DefaultChronosPlatformDependencies](M_Chronos_Platform_DefaultChronosPlatformDependencies__ctor.htm)|
Инициализирует новый экземпляр класса DefaultChronosPlatformDependencies  
---|---  
##  __Методы
[CreateGlobalEvent](M_Chronos_Platform_DefaultChronosPlatformDependencies_CreateGlobalEvent.htm)|
Создаёт событие по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
---|---  
[CreateGlobalMutex](M_Chronos_Platform_DefaultChronosPlatformDependencies_CreateGlobalMutex.htm)|
Создаёт мьютекс по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
[CreateProcessManagerWithJob](M_Chronos_Platform_DefaultChronosPlatformDependencies_CreateProcessManagerWithJob.htm)|
Создаёт объект [Chronos.Platform.Processes.IProcessManager] для создания
других процессов. При наличии возможности будет создан объект, объединяющий
текущий и дочерние процессы в Job. Метод может вызываться даже в том случае,
платформой не поддерживается [ChronosPlatformFeature.ProcessJob].  
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
[Initialize](M_Chronos_Platform_DefaultChronosPlatformDependencies_Initialize.htm)|
Выполняет инициализацию зависимостей платформы. Метод вызывается один раз при
запуске приложения.  
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
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
