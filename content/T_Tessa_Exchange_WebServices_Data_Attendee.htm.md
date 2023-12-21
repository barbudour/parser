# Attendee - класс
Represents an attendee to a meeting.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class Attendee : EmailAddress
VB __Копировать
     Public NotInheritable Class Attendee
    	Inherits EmailAddress
C++ __Копировать
     public ref class Attendee sealed : public EmailAddress
F# __Копировать
     [<SealedAttribute>]
    type Attendee = 
        class
            inherit EmailAddress
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm) __ Attendee
##  __Конструкторы
[Attendee()](M_Tessa_Exchange_WebServices_Data_Attendee__ctor.htm)|
Initializes a new instance of the Attendee class.  
---|---  
[Attendee(EmailAddress)](M_Tessa_Exchange_WebServices_Data_Attendee__ctor_4.htm)|
Initializes a new instance of the Attendee class from an EmailAddress.  
[Attendee(String)](M_Tessa_Exchange_WebServices_Data_Attendee__ctor_1.htm)|
Initializes a new instance of the Attendee class.  
[Attendee(String,
String)](M_Tessa_Exchange_WebServices_Data_Attendee__ctor_2.htm)|  Initializes
a new instance of the Attendee class.  
[Attendee(String, String,
String)](M_Tessa_Exchange_WebServices_Data_Attendee__ctor_3.htm)|  Initializes
a new instance of the Attendee class.  
## __Свойства
[Address](P_Tessa_Exchange_WebServices_Data_EmailAddress_Address.htm)|  Gets
or sets the actual address associated with the e-mail address. The type of the
Address property must match the specified routing type. If RoutingType is not
set, Address is assumed to be an SMTP address.  
(Унаследован от
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm))  
---|---  
[Id](P_Tessa_Exchange_WebServices_Data_EmailAddress_Id.htm)|  Gets or sets the
Id of the contact the e-mail address represents. When Id is specified, Address
should be set to null.  
(Унаследован от
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm))  
[LastResponseTime](P_Tessa_Exchange_WebServices_Data_Attendee_LastResponseTime.htm)|
Gets the date and time when the attendee last responded to a meeting
invitation or update.  
[MailboxType](P_Tessa_Exchange_WebServices_Data_EmailAddress_MailboxType.htm)|
Gets or sets the type of the e-mail address.  
(Унаследован от
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm))  
[Name](P_Tessa_Exchange_WebServices_Data_EmailAddress_Name.htm)|  Gets or sets
the name associated with the e-mail address.  
(Унаследован от
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm))  
[ResponseType](P_Tessa_Exchange_WebServices_Data_Attendee_ResponseType.htm)|
Gets the type of response the attendee gave to the meeting invitation it
received.  
[RoutingType](P_Tessa_Exchange_WebServices_Data_EmailAddress_RoutingType.htm)|
Gets or sets the routing type associated with the e-mail address. If
RoutingType is not set, Address is assumed to be an SMTP address.  
(Унаследован от
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm))  
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
[ToString](M_Tessa_Exchange_WebServices_Data_EmailAddress_ToString.htm)|
Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that
represents the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm))  
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
