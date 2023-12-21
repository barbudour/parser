# FolderId - класс
Represents the Id of a folder.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FolderId : ServiceId
VB __Копировать
     Public NotInheritable Class FolderId
    	Inherits ServiceId
C++ __Копировать
     public ref class FolderId sealed : public ServiceId
F# __Копировать
     [<SealedAttribute>]
    type FolderId = 
        class
            inherit ServiceId
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm) __ FolderId
##  __Конструкторы
[FolderId(String)](M_Tessa_Exchange_WebServices_Data_FolderId__ctor.htm)|
Initializes a new instance of the FolderId class. Use this constructor to link
this FolderId to an existing folder that you have the unique Id of.  
---|---  
[FolderId(WellKnownFolderName)](M_Tessa_Exchange_WebServices_Data_FolderId__ctor_1.htm)|
Initializes a new instance of the FolderId class. Use this constructor to link
this FolderId to a well known folder (e.g. Inbox, Calendar or Contacts).  
[FolderId(WellKnownFolderName,
Mailbox)](M_Tessa_Exchange_WebServices_Data_FolderId__ctor_2.htm)|
Initializes a new instance of the FolderId class. Use this constructor to link
this FolderId to a well known folder (e.g. Inbox, Calendar or Contacts) in a
specific mailbox.  
## __Свойства
[ChangeKey](P_Tessa_Exchange_WebServices_Data_ServiceId_ChangeKey.htm)|  Gets
the change key associated with the Exchange object. The change key represents
the the version of the associated item or folder.  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
---|---  
[FolderName](P_Tessa_Exchange_WebServices_Data_FolderId_FolderName.htm)|  Gets
the name of the folder associated with the folder Id. Name and Id are mutually
exclusive; if one is set, the other is null.  
[Mailbox](P_Tessa_Exchange_WebServices_Data_FolderId_Mailbox.htm)|  Gets the
mailbox of the folder. Mailbox is only set when FolderName is set.  
[UniqueId](P_Tessa_Exchange_WebServices_Data_ServiceId_UniqueId.htm)|  Gets
the unique Id of the Exchange object.  
(Унаследован от [ServiceId](T_Tessa_Exchange_WebServices_Data_ServiceId.htm))  
##  __Методы
[Equals](M_Tessa_Exchange_WebServices_Data_FolderId_Equals.htm)|  Determines
whether the specified
[Object](https://learn.microsoft.com/dotnet/api/system.object) is equal to the
current [Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[ServiceId.Equals(Object)](M_Tessa_Exchange_WebServices_Data_ServiceId_Equals.htm))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Exchange_WebServices_Data_FolderId_GetHashCode.htm)|
Serves as a hash function for a particular type.  
(Переопределяет
[ServiceId.GetHashCode()](M_Tessa_Exchange_WebServices_Data_ServiceId_GetHashCode.htm))  
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
[ToString](M_Tessa_Exchange_WebServices_Data_FolderId_ToString.htm)|  Returns
a [String](https://learn.microsoft.com/dotnet/api/system.string) that
represents the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[ServiceId.ToString()](M_Tessa_Exchange_WebServices_Data_ServiceId_ToString.htm))  
##  __Операторы
[ Implicit(String to
FolderId)](M_Tessa_Exchange_WebServices_Data_FolderId_op_Implicit.htm)|
Defines an implicit conversion between string and FolderId.  
---|---  
[Implicit(WellKnownFolderName to
FolderId)](M_Tessa_Exchange_WebServices_Data_FolderId_op_Implicit_1.htm)|
Defines an implicit conversion between WellKnownFolderName and FolderId.  
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
