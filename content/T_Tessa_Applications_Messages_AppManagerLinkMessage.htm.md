# AppManagerLinkMessage - класс
Сообщение содержащее аргументы ссылки обрабатываемое диспетчером приложений
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    public sealed class AppManagerLinkMessage : ApplicationLinkMessage
VB __Копировать
    <DataContractAttribute>
    Public NotInheritable Class AppManagerLinkMessage
    	Inherits ApplicationLinkMessage
C++ __Копировать
    [DataContractAttribute]
    public ref class AppManagerLinkMessage sealed : public ApplicationLinkMessage
F# __Копировать
     [<SealedAttribute>]
    [<DataContractAttribute>]
    type AppManagerLinkMessage = 
        class
            inherit ApplicationLinkMessage
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm) __[ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm) __ AppManagerLinkMessage
##  __Конструкторы
[AppManagerLinkMessage(ILink)](M_Tessa_Applications_Messages_AppManagerLinkMessage__ctor_1.htm)|
Initializes a new instance of the AppManagerLinkMessage class. Initializes a
new instance of the
[ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm)
class.  
---|---  
[AppManagerLinkMessage(String, String, String, String,
Int32)](M_Tessa_Applications_Messages_AppManagerLinkMessage__ctor.htm)|
Initializes a new instance of the AppManagerLinkMessage class. Initializes a
new instance of the
[ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm)
class.  
## __Свойства
[Alias](P_Tessa_Applications_Messages_AppManagerLinkMessage_Alias.htm)|  Gets
Псевдоним приложения  
---|---  
[InstanceName](P_Tessa_Applications_Messages_AppManagerLinkMessage_InstanceName.htm)|
Gets Экземпляр сервиса  
[LinkArguments](P_Tessa_Applications_Messages_ApplicationLinkMessage_LinkArguments.htm)|
Gets Параметры ссылки  
(Унаследован от
[ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm))  
[ProcessId](P_Tessa_Applications_Messages_AppManagerLinkMessage_ProcessId.htm)|
Gets or sets Идентификатор процесса  
[ServerCode](P_Tessa_Applications_Messages_AppManagerLinkMessage_ServerCode.htm)|
Gets Код сервиса  
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
[ToString](M_Tessa_Applications_Messages_ApplicationLinkMessage_ToString.htm)|
Возвращает объект
[String](https://learn.microsoft.com/dotnet/api/system.string), который
представляет текущий объект
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[ApplicationLinkMessage](T_Tessa_Applications_Messages_ApplicationLinkMessage.htm))  
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
