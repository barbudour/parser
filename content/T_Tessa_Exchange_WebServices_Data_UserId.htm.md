# UserId - класс
Represents the Id of a user.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UserId : ComplexProperty
VB __Копировать
     Public NotInheritable Class UserId
    	Inherits ComplexProperty
C++ __Копировать
     public ref class UserId sealed : public ComplexProperty
F# __Копировать
     [<SealedAttribute>]
    type UserId = 
        class
            inherit ComplexProperty
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ UserId
##  __Конструкторы
[UserId()](M_Tessa_Exchange_WebServices_Data_UserId__ctor.htm)|  Initializes a
new instance of the UserId class.  
---|---  
[UserId(StandardUser)](M_Tessa_Exchange_WebServices_Data_UserId__ctor_2.htm)|
Initializes a new instance of the UserId class.  
[UserId(String)](M_Tessa_Exchange_WebServices_Data_UserId__ctor_1.htm)|
Initializes a new instance of the UserId class.  
## __Свойства
[DisplayName](P_Tessa_Exchange_WebServices_Data_UserId_DisplayName.htm)|  Gets
or sets the display name of the user.  
---|---  
[PrimarySmtpAddress](P_Tessa_Exchange_WebServices_Data_UserId_PrimarySmtpAddress.htm)|
Gets or sets the primary SMTP address or the user.  
[SID](P_Tessa_Exchange_WebServices_Data_UserId_SID.htm)|  Gets or sets the SID
of the user.  
[StandardUser](P_Tessa_Exchange_WebServices_Data_UserId_StandardUser.htm)|
Gets or sets a value indicating which standard user the user represents.  
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
##  __Операторы
[ Implicit(StandardUser to
UserId)](M_Tessa_Exchange_WebServices_Data_UserId_op_Implicit_1.htm)|
Implements an implicit conversion between StandardUser and UserId.  
---|---  
[Implicit(String to
UserId)](M_Tessa_Exchange_WebServices_Data_UserId_op_Implicit.htm)|
Implements an implicit conversion between a string representing a primary SMTP
address and UserId.  
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
