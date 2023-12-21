# OofSettings - класс
Represents a user's Out of Office (OOF) settings.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class OofSettings : ComplexProperty
VB __Копировать
     Public NotInheritable Class OofSettings
    	Inherits ComplexProperty
C++ __Копировать
     public ref class OofSettings sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type OofSettings = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ OofSettings
##  __Конструкторы
[OofSettings](M_Tessa_Exchange_WebServices_Data_OofSettings__ctor.htm)|
Initializes a new instance of OofSettings.  
---|---  
## __Свойства
[AllowExternalOof](P_Tessa_Exchange_WebServices_Data_OofSettings_AllowExternalOof.htm)|
Gets a value indicating the authorized external OOF notifications.  
---|---  
[Duration](P_Tessa_Exchange_WebServices_Data_OofSettings_Duration.htm)|  Gets
or sets the duration of the OOF status when State is set to
OofState.Scheduled.  
[ExternalAudience](P_Tessa_Exchange_WebServices_Data_OofSettings_ExternalAudience.htm)|
Gets or sets a value indicating who should receive external OOF messages.  
[ExternalReply](P_Tessa_Exchange_WebServices_Data_OofSettings_ExternalReply.htm)|
Gets or sets the OOF response sent to addresses outside the user's domain or
trusted domain.  
[InternalReply](P_Tessa_Exchange_WebServices_Data_OofSettings_InternalReply.htm)|
Gets or sets the OOF response sent other users in the user's domain or trusted
domain.  
[State](P_Tessa_Exchange_WebServices_Data_OofSettings_State.htm)|  Gets or
sets the user's OOF state.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
