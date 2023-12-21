# ApplicationLaunchingStrategy - класс
Стратегия запуска приложения.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationLaunchingStrategy : IApplicationLaunchingStrategy
VB __Копировать
     Public NotInheritable Class ApplicationLaunchingStrategy
    	Implements IApplicationLaunchingStrategy
C++ __Копировать
     public ref class ApplicationLaunchingStrategy sealed : IApplicationLaunchingStrategy
F# __Копировать
     [<SealedAttribute>]
    type ApplicationLaunchingStrategy = 
        class
            interface IApplicationLaunchingStrategy
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationLaunchingStrategy
Implements
    [IApplicationLaunchingStrategy](T_Tessa_Applications_IApplicationLaunchingStrategy.htm)
##  __Конструкторы
[ApplicationLaunchingStrategy](M_Tessa_Applications_ApplicationLaunchingStrategy__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationLaunchingStrategy  
---|---  
##  __Методы
[CreateProcess](M_Tessa_Applications_ApplicationLaunchingStrategy_CreateProcess.htm)|
Осуществляет создание процесса приложения  
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
[UpdateApplicationAsync](M_Tessa_Applications_ApplicationLaunchingStrategy_UpdateApplicationAsync.htm)|
Осуществляет обновление приложения  
[UpdateAvailableAsync](M_Tessa_Applications_ApplicationLaunchingStrategy_UpdateAvailableAsync.htm)|
Проверяет необходимость обновления приложения. Возвращает признак наличия
обновления приложения и действительную разрядность приложения на момент
проверки, если обновление доступно (иначе нельзя опираться на возвращённое
значение).  
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
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
