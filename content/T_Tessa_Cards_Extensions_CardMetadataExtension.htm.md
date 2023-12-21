# CardMetadataExtension - класс
Базовый класс для расширения, выполняемого при построении метаинформации по
типам карточек [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm). Для того,
чтобы использовать вспомогательные свойства и методы получения метаинформации
по типам карточек, используйте базовый класс
[CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardMetadataExtension : ICardMetadataExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class CardMetadataExtension
    	Implements ICardMetadataExtension, IExtension
C++ __Копировать
     public ref class CardMetadataExtension abstract : ICardMetadataExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardMetadataExtension = 
        class
            interface ICardMetadataExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataExtension
Derived
[Tessa.Cards.Extensions.CardTypeMetadataExtension](T_Tessa_Cards_Extensions_CardTypeMetadataExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineCardMetadataExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineCardMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.FileSignaturesMetadataExtension](T_Tessa_Extensions_Platform_Shared_Cards_FileSignaturesMetadataExtension.htm)
[Tessa.Extensions.Platform.Shared.Roles.RoleDeputiesManagementMetadataExtension](T_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementMetadataExtension.htm)
Implements
    [ICardMetadataExtension](T_Tessa_Cards_Extensions_ICardMetadataExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardMetadataExtension](M_Tessa_Cards_Extensions_CardMetadataExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardMetadataExtension  
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
[ModifyMetadata](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyMetadata.htm)|
Изменяет метаинформацию по типам карточек после её построения.  
[ModifyTypes](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyTypes.htm)|
Изменяет типы карточек, по которым затем будет строиться метаинформация.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
