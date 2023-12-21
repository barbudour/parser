# PersonaEmailAddress - класс
Represents an e-mail address.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PersonaEmailAddress : ComplexProperty, 
    	ISearchStringProvider
VB __Копировать
     Public NotInheritable Class PersonaEmailAddress
    	Inherits ComplexProperty
    	Implements ISearchStringProvider
C++ __Копировать
     public ref class PersonaEmailAddress sealed : public ComplexProperty, 
    	ISearchStringProvider
F# __Копировать
     [<SealedAttribute>]
    type PersonaEmailAddress = 
        class
            inherit ComplexProperty
            interface ISearchStringProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ PersonaEmailAddress
Implements
    [ISearchStringProvider](T_Tessa_Exchange_WebServices_Data_ISearchStringProvider.htm)
##  __Конструкторы
[PersonaEmailAddress()](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddress__ctor.htm)|
Creates a new instance of the PersonaEmailAddress class.  
---|---  
[PersonaEmailAddress(String)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddress__ctor_1.htm)|
Creates a new instance of the
[EmailAddress](T_Tessa_Exchange_WebServices_Data_EmailAddress.htm) class.  
[PersonaEmailAddress(String,
String)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddress__ctor_2.htm)|
Creates a new instance of the PersonaEmailAddress class.  
## __Свойства
[Address](P_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_Address.htm)|
Email address accessors. The type of the Address property must match the
specified routing type. If RoutingType is not set, Address is assumed to be an
SMTP address.  
---|---  
[Id](P_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_Id.htm)|
PersonaEmailAddress Id accessors  
[MailboxType](P_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_MailboxType.htm)|
Mailbox type accessors  
[Name](P_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_Name.htm)|  Name
accessors  
[OriginalDisplayName](P_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_OriginalDisplayName.htm)|
Original display name accessors  
[RoutingType](P_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_RoutingType.htm)|
Routing type accessors. If RoutingType is not set, Address is assumed to be an
SMTP address.  
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
[ToString](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_ToString.htm)|
Returns a [String](https://learn.microsoft.com/dotnet/api/system.string) that
represents the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[ Implicit(String to
PersonaEmailAddress)](M_Tessa_Exchange_WebServices_Data_PersonaEmailAddress_op_Implicit.htm)|
Defines an implicit conversion from a string representing an SMTP address to
PeronaEmailAddress.  
---|---  
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
