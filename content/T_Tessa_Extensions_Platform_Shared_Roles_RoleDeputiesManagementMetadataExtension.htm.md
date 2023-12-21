# RoleDeputiesManagementMetadataExtension - класс
Расширение, добавляющее в тип карточки PersonalRole, секции и вкладку из
карточки RoleDeputiesManagement. На клиенте используется для добавления
информации в тип для превью карточки, при этом подразумевается, что доступна
полная метаинформация с сервера. На сервере используется для добавлении
информации в тип при построении.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Shared.Roles](N_Tessa_Extensions_Platform_Shared_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleDeputiesManagementMetadataExtension : CardMetadataExtension
VB __Копировать
     Public NotInheritable Class RoleDeputiesManagementMetadataExtension
    	Inherits CardMetadataExtension
C++ __Копировать
     public ref class RoleDeputiesManagementMetadataExtension sealed : public CardMetadataExtension
F# __Копировать
     [<SealedAttribute>]
    type RoleDeputiesManagementMetadataExtension = 
        class
            inherit CardMetadataExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm) __ RoleDeputiesManagementMetadataExtension
##  __Конструкторы
[RoleDeputiesManagementMetadataExtension()](M_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementMetadataExtension__ctor.htm)|
Инициализирует новый экземпляр класса RoleDeputiesManagementMetadataExtension  
---|---  
[RoleDeputiesManagementMetadataExtension(ICardMetadata)](M_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementMetadataExtension__ctor_1.htm)|
Инициализирует новый экземпляр класса RoleDeputiesManagementMetadataExtension  
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
(Унаследован от
[CardMetadataExtension](T_Tessa_Cards_Extensions_CardMetadataExtension.htm))  
[ModifyTypes](M_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementMetadataExtension_ModifyTypes.htm)|
Изменяет типы карточек, по которым затем будет строиться метаинформация.  
(Переопределяет
[CardMetadataExtension.ModifyTypes(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_CardMetadataExtension_ModifyTypes.htm))  
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
[Tessa.Extensions.Platform.Shared.Roles - пространство
имён](N_Tessa_Extensions_Platform_Shared_Roles.htm)
