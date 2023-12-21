# TessaApplicationAddressGenerator - класс
Объект
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
для определения адреса клиентского приложения с указанием идентификатора
процесса. Например: Syntellect/Tessa/App_4422 (где 4422 \- идентификатор
процесса для приложения)
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaApplicationAddressGenerator : HostServiceAddressGenerator
VB __Копировать
     Public Class TessaApplicationAddressGenerator
    	Inherits HostServiceAddressGenerator
C++ __Копировать
     public ref class TessaApplicationAddressGenerator : public HostServiceAddressGenerator
F# __Копировать
     type TessaApplicationAddressGenerator = 
        class
            inherit HostServiceAddressGenerator
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[HostServiceAddressGenerator](T_Tessa_Host_HostServiceAddressGenerator.htm) __ TessaApplicationAddressGenerator
Derived
[Tessa.Applications.Services.PlatformApplication.TessaApplicationClientAddressGenerator](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationClientAddressGenerator.htm)
##  __Конструкторы
[TessaApplicationAddressGenerator](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationAddressGenerator__ctor.htm)|
Инициализирует новый экземпляр класса TessaApplicationAddressGenerator  
---|---  
##  __Свойства
[AppendUniqueCounter](P_Tessa_Host_HostServiceAddressGenerator_AppendUniqueCounter.htm)|  
(Унаследован от
[HostServiceAddressGenerator](T_Tessa_Host_HostServiceAddressGenerator.htm))  
---|---  
[Instance](P_Tessa_Applications_Services_PlatformApplication_TessaApplicationAddressGenerator_Instance.htm)|  
[ProcessId](P_Tessa_Host_HostServiceAddressGenerator_ProcessId.htm)|  
(Унаследован от
[HostServiceAddressGenerator](T_Tessa_Host_HostServiceAddressGenerator.htm))  
##  __Методы
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
[GetActualHandlerType](M_Tessa_Applications_Services_PlatformApplication_TessaApplicationAddressGenerator_GetActualHandlerType.htm)|  
(Переопределяет
[HostServiceAddressGenerator.GetActualHandlerType(String)](M_Tessa_Host_HostServiceAddressGenerator_GetActualHandlerType.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNextServiceAddress](M_Tessa_Host_HostServiceAddressGenerator_GetNextServiceAddress.htm)|
Возвращает адрес сервиса  
(Унаследован от
[HostServiceAddressGenerator](T_Tessa_Host_HostServiceAddressGenerator.htm))  
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
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)
