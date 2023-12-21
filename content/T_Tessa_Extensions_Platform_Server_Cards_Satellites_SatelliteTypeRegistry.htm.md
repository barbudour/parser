# SatelliteTypeRegistry - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards.Satellites](N_Tessa_Extensions_Platform_Server_Cards_Satellites.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SatelliteTypeRegistry : Registry<Guid, SatelliteTypeDescriptor>, 
    	ISatelliteTypeRegistry, IRegistry<Guid, SatelliteTypeDescriptor>
VB __Копировать
     Public NotInheritable Class SatelliteTypeRegistry
    	Inherits Registry(Of Guid, SatelliteTypeDescriptor)
    	Implements ISatelliteTypeRegistry, IRegistry(Of Guid, SatelliteTypeDescriptor)
C++ __Копировать
     public ref class SatelliteTypeRegistry sealed : public Registry<Guid, SatelliteTypeDescriptor^>, 
    	ISatelliteTypeRegistry, IRegistry<Guid, SatelliteTypeDescriptor^>
F# __Копировать
     [<SealedAttribute>]
    type SatelliteTypeRegistry = 
        class
            inherit Registry<Guid, SatelliteTypeDescriptor>
            interface ISatelliteTypeRegistry
            interface IRegistry<Guid, SatelliteTypeDescriptor>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Registry](T_Tessa_Platform_Registry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [SatelliteTypeDescriptor](T_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor.htm)> __ SatelliteTypeRegistry
Implements
    [ISatelliteTypeRegistry](T_Tessa_Extensions_Platform_Server_Cards_Satellites_ISatelliteTypeRegistry.htm), [IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [SatelliteTypeDescriptor](T_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeDescriptor.htm)>
##  __Конструкторы
[SatelliteTypeRegistry](M_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeRegistry__ctor.htm)|
Инициализирует новый экземпляр класса SatelliteTypeRegistry  
---|---  
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
[Get](M_Tessa_Platform_Registry_2_Get.htm)| Возвращает объект,
зарегистрированный в реестре по заданному идентификатору.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[GetAll](M_Tessa_Platform_Registry_2_GetAll.htm)| Возвращает все
зарегистрированные в реестре объекты.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetSatelliteHandler](M_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeRegistry_GetSatelliteHandler.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsDefined(TIdentifier)](M_Tessa_Platform_Registry_2_IsDefined.htm)|
Возвращает признак того, что в реестре был зарегистрирован объект по заданному
идентификатору.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[IsDefined(TItem)](M_Tessa_Platform_Registry_2_IsDefined_1.htm)| Возвращает
признак того, что заданный объект был зарегистрирован в реестре.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Register](M_Tessa_Platform_Registry_2_Register.htm)| Регистрирует объект по
его идентификатору. Метод замещает предыдущую регистрацию при её наличии.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[RegisterCore](M_Tessa_Platform_Registry_2_RegisterCore.htm)| Регистрирует
объект по его идентификатору. Метод замещает предыдущую регистрацию при её
наличии.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[RegisterNew](M_Tessa_Platform_Registry_2_RegisterNew.htm)|  Регистрирует
новый объект в реестре. Если элемент уже присутствует, то никаких действий не
производится.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Registry_2_TryGet.htm)|  Возвращает объект в
параметре result, зарегистрированный в реестре по заданному идентификатору.
Метод возвращает false, если объект отсутствует в реестре.  
(Унаследован от [Registry<TIdentifier,
TItem>](T_Tessa_Platform_Registry_2.htm))  
[TryGetExtendedAsync](M_Tessa_Extensions_Platform_Server_Cards_Satellites_SatelliteTypeRegistry_TryGetExtendedAsync.htm)|  
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
[Tessa.Extensions.Platform.Server.Cards.Satellites - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards_Satellites.htm)
