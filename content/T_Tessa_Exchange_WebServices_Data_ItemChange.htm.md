# ItemChange - класс
Represents a change on an item as returned by a synchronization operation.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ItemChange : Change
VB __Копировать
     Public NotInheritable Class ItemChange
    	Inherits Change
C++ __Копировать
     public ref class ItemChange sealed : public Change
F# __Копировать
     [<SealedAttribute>]
    type ItemChange = 
        class
            inherit Change
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Change](T_Tessa_Exchange_WebServices_Data_Change.htm) __ ItemChange
##  __Свойства
[ChangeType](P_Tessa_Exchange_WebServices_Data_Change_ChangeType.htm)|  Gets
the type of the change.  
(Унаследован от [Change](T_Tessa_Exchange_WebServices_Data_Change.htm))  
---|---  
[IsRead](P_Tessa_Exchange_WebServices_Data_ItemChange_IsRead.htm)|  Gets the
IsRead property for the item that the change applies to. IsRead is only valid
when ChangeType is equal to ChangeType.ReadFlagChange.  
[Item](P_Tessa_Exchange_WebServices_Data_ItemChange_Item.htm)|  Gets the item
the change applies to. Item is null when ChangeType is equal to either
ChangeType.Delete or ChangeType.ReadFlagChange. In those cases, use the ItemId
property to retrieve the Id of the item that was deleted or whose IsRead
property changed.  
[ItemId](P_Tessa_Exchange_WebServices_Data_ItemChange_ItemId.htm)|  Gets the
Id of the item the change applies to.  
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
