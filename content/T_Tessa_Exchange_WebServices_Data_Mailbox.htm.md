# Mailbox - класс
Represents a mailbox reference.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class Mailbox : ComplexProperty, ISearchStringProvider
VB __Копировать
     Public Class Mailbox
    	Inherits ComplexProperty
    	Implements ISearchStringProvider
C++ __Копировать
     public ref class Mailbox : public ComplexProperty, 
    	ISearchStringProvider
F# __Копировать
     type Mailbox = 
        class
            inherit ComplexProperty
            interface ISearchStringProvider
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ Mailbox
Implements
    [ISearchStringProvider](T_Tessa_Exchange_WebServices_Data_ISearchStringProvider.htm)
##  __Конструкторы
[Mailbox()](M_Tessa_Exchange_WebServices_Data_Mailbox__ctor.htm)|  Initializes
a new instance of the Mailbox class.  
---|---  
[Mailbox(String)](M_Tessa_Exchange_WebServices_Data_Mailbox__ctor_1.htm)|
Initializes a new instance of the Mailbox class.  
[Mailbox(String,
String)](M_Tessa_Exchange_WebServices_Data_Mailbox__ctor_2.htm)|  Initializes
a new instance of the Mailbox class.  
## __Свойства
[Address](P_Tessa_Exchange_WebServices_Data_Mailbox_Address.htm)|  Gets or
sets the address used to refer to the user mailbox.  
---|---  
[IsValid](P_Tessa_Exchange_WebServices_Data_Mailbox_IsValid.htm)|  True if
this instance is valid, false otherthise.  
[RoutingType](P_Tessa_Exchange_WebServices_Data_Mailbox_RoutingType.htm)|
Gets or sets the routing type of the address used to refer to the user
mailbox.  
## __Методы
[Equals](M_Tessa_Exchange_WebServices_Data_Mailbox_Equals.htm)|  Determines
whether the specified
[Object](https://learn.microsoft.com/dotnet/api/system.object) is equal to the
current [Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Exchange_WebServices_Data_Mailbox_GetHashCode.htm)|
Serves as a hash function for a particular type.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToString](M_Tessa_Exchange_WebServices_Data_Mailbox_ToString.htm)|  Returns a
[String](https://learn.microsoft.com/dotnet/api/system.string) that represents
the current [Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Операторы
[ Implicit(String to
Mailbox)](M_Tessa_Exchange_WebServices_Data_Mailbox_op_Implicit.htm)|  Defines
an implicit conversion between a string representing an SMTP address and
Mailbox.  
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
