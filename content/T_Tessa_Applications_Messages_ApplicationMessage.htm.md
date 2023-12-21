# ApplicationMessage - класс
Базовый класс сообщения, которое может быть передано запущенному приложению
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    public abstract class ApplicationMessage
VB __Копировать
    <DataContractAttribute>
    Public MustInherit Class ApplicationMessage
C++ __Копировать
    [DataContractAttribute]
    public ref class ApplicationMessage abstract
F# __Копировать
     [<AbstractClassAttribute>]
    [<DataContractAttribute>]
    type ApplicationMessage = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationMessage
Derived
[Tessa.Applications.Messages.ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm)
[Tessa.Applications.Messages.ApplicationStartMessage](T_Tessa_Applications_Messages_ApplicationStartMessage.htm)
[Tessa.Applications.Messages.RegistrationConfirmationMessage](T_Tessa_Applications_Messages_RegistrationConfirmationMessage.htm)
[Tessa.Applications.Messages.ShellActivateApplicationMessage](T_Tessa_Applications_Messages_ShellActivateApplicationMessage.htm)
[Tessa.Applications.Messages.ShellHideApplicationMessage](T_Tessa_Applications_Messages_ShellHideApplicationMessage.htm)
##  __Конструкторы
[ApplicationMessage](M_Tessa_Applications_Messages_ApplicationMessage__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationMessage  
---|---  
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
[ToString](M_Tessa_Applications_Messages_ApplicationMessage_ToString.htm)|
Возвращает объект
[String](https://learn.microsoft.com/dotnet/api/system.string), который
представляет текущий объект
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
