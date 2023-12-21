# Conflict - класс
Represents a conflict in a meeting time suggestion.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Conflict : ComplexProperty
VB __Копировать
     Public NotInheritable Class Conflict
    	Inherits ComplexProperty
C++ __Копировать
     public ref class Conflict sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type Conflict = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ Conflict
##  __Свойства
[ConflictType](P_Tessa_Exchange_WebServices_Data_Conflict_ConflictType.htm)|
Gets the type of the conflict.  
---|---  
[FreeBusyStatus](P_Tessa_Exchange_WebServices_Data_Conflict_FreeBusyStatus.htm)|
Gets the free/busy status of the conflicting attendee. The value of this
property is only meaningful when ConflictType is equal to
ConflictType.IndividualAttendee.  
[NumberOfMembers](P_Tessa_Exchange_WebServices_Data_Conflict_NumberOfMembers.htm)|
Gets the number of users, resources, and rooms in the conflicting group. The
value of this property is only meaningful when ConflictType is equal to
ConflictType.GroupConflict.  
[NumberOfMembersAvailable](P_Tessa_Exchange_WebServices_Data_Conflict_NumberOfMembersAvailable.htm)|
Gets the number of members who are available (whose status is Free) in the
conflicting group. The value of this property is only meaningful when
ConflictType is equal to ConflictType.GroupConflict.  
[NumberOfMembersWithConflict](P_Tessa_Exchange_WebServices_Data_Conflict_NumberOfMembersWithConflict.htm)|
Gets the number of members who have a conflict (whose status is Busy, OOF or
Tentative) in the conflicting group. The value of this property is only
meaningful when ConflictType is equal to ConflictType.GroupConflict.  
[NumberOfMembersWithNoData](P_Tessa_Exchange_WebServices_Data_Conflict_NumberOfMembersWithNoData.htm)|
Gets the number of members who do not have published free/busy data in the
conflicting group. The value of this property is only meaningful when
ConflictType is equal to ConflictType.GroupConflict.  
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
