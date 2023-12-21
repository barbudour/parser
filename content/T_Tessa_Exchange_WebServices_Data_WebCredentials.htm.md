# WebCredentials - класс
WebCredentials wraps an instance of ICredentials used for password-based
authentication schemes such as basic, digest, NTLM, and Kerberos
authentication.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebCredentials : ExchangeCredentials
VB __Копировать
     Public NotInheritable Class WebCredentials
    	Inherits ExchangeCredentials
C++ __Копировать
     public ref class WebCredentials sealed : public ExchangeCredentials
F# __Копировать
     [<SealedAttribute>]
    type WebCredentials = 
        class
            inherit ExchangeCredentials
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ExchangeCredentials](T_Tessa_Exchange_WebServices_Data_ExchangeCredentials.htm) __ WebCredentials
##  __Конструкторы
[WebCredentials()](M_Tessa_Exchange_WebServices_Data_WebCredentials__ctor.htm)|
Initializes a new instance of the WebCredentials class to use the default
network credentials.  
---|---  
[WebCredentials(ICredentials)](M_Tessa_Exchange_WebServices_Data_WebCredentials__ctor_1.htm)|
Initializes a new instance of the WebCredentials class using specified
credentials.  
[WebCredentials(String,
String)](M_Tessa_Exchange_WebServices_Data_WebCredentials__ctor_2.htm)|
Initializes a new instance of the WebCredentials class.  
[WebCredentials(String, String,
String)](M_Tessa_Exchange_WebServices_Data_WebCredentials__ctor_3.htm)|
Initializes a new instance of the WebCredentials class.  
## __Свойства
[Credentials](P_Tessa_Exchange_WebServices_Data_WebCredentials_Credentials.htm)|
Gets the Credentials from this instance.  
---|---  
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
