# GroupMemberCollection - класс
Represents a collection of members of GroupMember type.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class GroupMemberCollection : ComplexPropertyCollection<GroupMember>
VB __Копировать
     Public NotInheritable Class GroupMemberCollection
    	Inherits ComplexPropertyCollection(Of GroupMember)
C++ __Копировать
     public ref class GroupMemberCollection sealed : public ComplexPropertyCollection<GroupMember^>
F# __Копировать
     [<SealedAttribute>]
    type GroupMemberCollection = 
        class
            inherit ComplexPropertyCollection<GroupMember>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[ComplexPropertyCollection](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm)<[GroupMember](T_Tessa_Exchange_WebServices_Data_GroupMember.htm)> __ GroupMemberCollection
##  __Конструкторы
[GroupMemberCollection](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection__ctor.htm)|
Initializes a new instance of the GroupMemberCollection class.  
---|---  
## __Свойства
[Count](P_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Count.htm)|
Gets the total number of properties in the collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
---|---  
[Item](P_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Item.htm)|
Gets the property at the specified index.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
##  __Методы
[Add](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_Add.htm)|  Adds
a member to the collection.  
---|---  
[AddContactEmailAddress](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddContactEmailAddress.htm)|
Adds a member that is linked to a specific e-mail address of a contact.  
[AddContactGroup](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddContactGroup.htm)|
Adds a member linked to a Contact Group.  
[AddDirectoryContact(String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddDirectoryContact.htm)|
Adds a member linked to an Active Directory contact.  
[AddDirectoryContact(String,
String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddDirectoryContact_1.htm)|
Adds a member linked to an Active Directory contact.  
[AddDirectoryPublicFolder](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddDirectoryPublicFolder.htm)|
Adds a member linked to a mail-enabled Public Folder.  
[AddDirectoryUser(String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddDirectoryUser.htm)|
Adds a member linked to an Active Directory user.  
[AddDirectoryUser(String,
String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddDirectoryUser_1.htm)|
Adds a member linked to an Active Directory user.  
[AddOneOff(String,
String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddOneOff.htm)|
Adds a one-off member.  
[AddOneOff(String, String,
String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddOneOff_1.htm)|
Adds a one-off member.  
[AddPersonalContact(ItemId)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddPersonalContact.htm)|
Adds a member linked to a contact's first available e-mail address.  
[AddPersonalContact(ItemId,
String)](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddPersonalContact_1.htm)|
Adds a member linked to a specific contact's e-mail address.  
[AddPublicGroup](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddPublicGroup.htm)|
Adds a member linked to a Public Group.  
[AddRange](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_AddRange.htm)|
Adds multiple members to the collection.  
[Clear](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_Clear.htm)|
Clears the collection.  
[Contains](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Contains.htm)|
Determines whether a specific property is in the collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
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
[Find](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_Find.htm)|
Finds the member with the specified key in the collection. Members that have
not yet been saved do not have a key.  
[GetEnumerator](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_GetEnumerator.htm)|
Gets an enumerator that iterates through the elements of the collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
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
[IndexOf](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_IndexOf.htm)|
Searches for a specific property and return its zero-based index within the
collection.  
(Унаследован от
[ComplexPropertyCollection<TComplexProperty>](T_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_Remove.htm)|
Removes a member from the collection.  
[RemoveAt](M_Tessa_Exchange_WebServices_Data_GroupMemberCollection_RemoveAt.htm)|
Removes a member at the specified index.  
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
