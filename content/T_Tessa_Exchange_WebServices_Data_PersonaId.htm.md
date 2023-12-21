# PersonaId - класс
Represents the Id of a Persona.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PersonaId : ServiceId
VB __Копировать
     Public NotInheritable Class PersonaId
    	Inherits ServiceId
C++ __Копировать
     public ref class PersonaId sealed : public ServiceId
F# __Копировать
     [<SealedAttribute>]
    type PersonaId = 
        class
            inherit ServiceId
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm) __ PersonaId
##  __Конструкторы
[PersonaId](M_Tessa_Exchange_WebServices_Data_PersonaId__ctor.htm)|  Creates a
new instance of PersonaId.  
---|---  
## __Свойства
[ChangeKey](P_Tessa_Exchange_WebServices_Data_ServiceId_ChangeKey.htm)|  Gets
the change key associated with the Exchange object. The change key represents
the the version of the associated item or folder.  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
---|---  
[UniqueId](P_Tessa_Exchange_WebServices_Data_ServiceId_UniqueId.htm)|  Gets
the unique Id of the Exchange object.  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
##  __Методы
[Equals](M_Tessa_Exchange_WebServices_Data_ServiceId_Equals.htm)|  Determines
whether the specified
[Object](https://learn.microsoft.com/dotnet/api/system.object) is equal to the
current [Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Exchange_WebServices_Data_ServiceId_GetHashCode.htm)|
Serves as a hash function for a particular type.  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
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
[SameIdAndChangeKey](M_Tessa_Exchange_WebServices_Data_ServiceId_SameIdAndChangeKey.htm)|
Determines whether two ServiceId instances are equal (including ChangeKeys)  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
[ToString](M_Tessa_Exchange_WebServices_Data_PersonaId_ToString.htm)|  Gets a
string representation of the Persona Id.  
(Переопределяет
[ServiceId.ToString()](M_Tessa_Exchange_WebServices_Data_ServiceId_ToString.htm))  
##  __Операторы
[ Implicit(PersonaId to
String)](M_Tessa_Exchange_WebServices_Data_PersonaId_op_Implicit_1.htm)|
Defines an implicit conversion from PersonaId to a Id string.  
---|---  
[Implicit(String to
PersonaId)](M_Tessa_Exchange_WebServices_Data_PersonaId_op_Implicit.htm)|
Defines an implicit conversion from Id string to PersonaId.  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
